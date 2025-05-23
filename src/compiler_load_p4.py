#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# SPDX-License-Identifier: Apache-2.0
# Copyright 2019 Eotvos Lorand University, Budapest, Hungary

import hlir16.hlir
from compiler_log_warnings_errors import *

import os
import os.path
import sys
import pkgutil
import importlib
import gzip

import pickle

import compiler_common
from p4Aggregator import P4Aggregator


# TODO also reload if (the relevant part of) the HLIR generator code has changed
def is_file_fresh(filename):
    global p4time
    filetime = os.path.getmtime(filename)
    return p4time < filetime


def is_cache_file_loadable(path):
    return path is not None and os.path.isfile(path) and is_file_fresh(path)


def import_modules(required_modules):
    for modname in required_modules:
        if not pkgutil.find_loader(modname):
            return None

    return [importlib.import_module(modname) for modname in required_modules]


def open_for_write(filename):
    # return open(filename, 'wb')
    return gzip.open(filename, 'wb')


def open_for_read(filename):
    # return open(filename, 'rb')
    return gzip.open(filename, 'rb')


def load_cache(filename, is_compressed, required_modules, loader):
    if not is_cache_file_loadable(filename):
        return None

    if import_modules(required_modules) is None:
        return None

    if is_compressed:
        try:
            with open_for_read(filename) as cache_file:
                return loader(cache_file, None)
        except Exception as e:
            print(f'The following exception occurred while loading cache file {filename}')
            print(e)
            return None


def write_cache(cache, required_modules, saver, data):
    if import_modules(required_modules) is None:
        return

    with open_for_write(cache) as cache_file:
        saver(data, cache_file)


def p4_to_json(files, arg):
    global args
    p4_filename, json_filename = arg
    p4_include_dirs = args['p4incdir']
    return hlir16.hlir.p4_to_json(p4_filename, json_filename, args['p4v'], args['p4c_path'], args['p4opt'], p4_include_dirs)


def load_simdjson(file, data):
    import simdjson
    if file is not None:
        args['verbose'] and print(f"Loading file using simdjson")
        return simdjson.load(file)

    with open(data, 'r') as f:
        return simdjson.load(f)


def load_orjson(file, data):
    import orjson
    if file is not None:
        args['verbose'] and print(f"Loading file using orjson")
        return orjson.load(file)

    with open(data, 'r') as f:
        return orjson.load(f)


def load_ujson(file, data):
    import ujson
    if file is not None:
        args['verbose'] and print(f"Loading file using ujson")
        return ujson.load(file)

    with open(data, 'r') as f:
        return ujson.load(f)


def load_json(file, data):
    import json
    if file is not None:
        args['verbose'] and print(f"Loading file using json")
        return json.load(file)

    with open(data, 'r') as f:
        return json.load(f)


class RecursionLimit():
    """Temporarily increase the standard recursion limit."""
    def __init__(self, limit):
        self.limit = limit

    def __enter__(self):
        self.old_limit = sys.getrecursionlimit()
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, traceback):
        sys.setrecursionlimit(self.old_limit)


def restrict_stages(stages):
    for stage in stages:
        if 'dependency' not in stage:
            yield stage
            continue

        if not os.path.isfile(stage['filename']):
            return

        filetime = os.path.getctime(stage['filename'])
        for dep in stage['dependency']:
            if filetime < os.path.getctime(dep):
                args['verbose'] and print(f"Dependency file {dep} is newer than {stage['filename']}, stage {stage['name']} has to be redone")
                return

        yield stage


def load_latest_stage_from_cache(stages):
    for stage_idx, stage in reversed(list(enumerate(restrict_stages(stages)))):
        for attrname, attrdefault in [('filename', None), ('is_valid', lambda x: True), ('msgfmt', ""), ('saver', None), ('is_compressed', stage_idx != 0)]:
            if attrname not in stage:
                stage[attrname] = attrdefault

        for required_modules, loader in stage['loaders']:
            loaded = load_cache(stage['filename'], stage['is_compressed'], required_modules, loader)
            if loaded and stage['is_valid'](loaded):
                args['verbose'] and print(stage['msgfmt'].format(stage['filename']))
                return stage_idx + 1, loaded

    return 0, None


def continue_stages(stages, stage_idx, data):
    for curr_stage_idx, stage in list(enumerate(stages))[stage_idx:]:
        compiler_common.current_compilation = { 'from': f"(cached) {stage['filename']}", 'to': "(generated content)", 'stage': stage }

        new_data = None
        last_exception = None
        for required_modules, loader in stage['loaders']:
            if import_modules(required_modules) is None:
                continue

            try:
                new_data = loader(None, data)
            except Exception as e:
                print(f'The following exception occurred while loading cache file {filename}')
                print(e)
                last_exception = e
                continue

            if new_data is not None:
                break

        if new_data is None:
            if last_exception is not None:
                raise last_exception
            raise Exception(f'Stage {stage["name"]} could not load data')

        data = new_data

        if 'saver' in stage and stage['saver'] is not None:
            required_modules, saver = stage['saver']
            write_cache(stage['filename'], required_modules, saver, data)
    return data


def load_hlir(filename, cache_dir_name, recompile=False):
    p4cache = os.path.join(cache_dir_name, os.path.basename(filename))

    stages = [
        stage_p4_to_json_file(filename, p4cache),
        stage_load_json(filename, p4cache),
        stage_json_to_hlir(filename, p4cache),
        stage_hlir_add_attributes(filename, p4cache),
        ]

    stage_idx, data = (0, None) if recompile else load_latest_stage_from_cache(stages)
    if stage_idx == 0:
        args['verbose'] and print(stages[0]['msgfmt'].format(filename))
        data = (filename, f"{p4cache}.json.cached")
    return continue_stages(stages, stage_idx, data)


def cache_loader(no_cache_loader):
    return ([], lambda file, data: pickle.load(file) if file is not None else no_cache_loader(data) if data is not None else None)


def cache_saver():
    return ([], lambda data, cache_file: cache_file.write(pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL)))


def stage_p4_to_json_file(filename, p4cache):
    return {
        'name': 'stage_p4_to_json_file',
        'filename': filename,
        'msgfmt': "HLIR (uncached) {}",
        'dependency': [filename],
        # The P4C compiler creates the JSON file while "loading".
        'loaders': [([], p4_to_json)],
    }


def stage_load_json(filename, p4cache):
    return {
        'name': 'stage_load_json',
        'msgfmt': "HLIR (cached: JSON) {}",
        'filename': f"{p4cache}.json.cached",
        'loaders': [(['simdjson'], load_simdjson), (['orjson'], load_orjson), (['ujson'], load_ujson), ([], load_json)],
        # This detects if the loaded JSON does not contain "main".
        'is_valid': lambda json_root: json_root['Node_ID'] is not None,
    }


def stage_json_to_hlir(filename, p4cache):
    return {
        'name': 'stage_json_to_hlir',
        'msgfmt': "HLIR (cached: stage json_to_hlir) {}",
        'filename': f"{p4cache}.hlir.cached",
        'loaders': [cache_loader(lambda json_root: hlir16.hlir.walk_json_from_top(json_root))],
        'dependency': ["src/compiler.py", "src/compiler_load_p4.py", "src/compiler_exception_handling.py", "src/hlir16/hlir.py", "src/hlir16/hlir_attrs.py", "src/hlir16/p4node.py"],
        'saver': cache_saver(),
    }


def stage_hlir_add_attributes(filename, p4cache):
    return {
        'name': 'stage_hlir_add_attributes',
        'msgfmt': "HLIR (cached: stage hlir_add_attributes) {}",
        'filename': f"{p4cache}.hlir.attributed.cached",
        'loaders': [cache_loader(lambda hlir: hlir16.hlir_attrs.set_additional_attrs(hlir, filename, args['p4v']))],
        'saver': cache_saver(),
    }


def check_file_exists(filename):
    if os.path.isfile(filename) is False:
        print("FILE NOT FOUND: %s" % filename, file=sys.stderr)
        sys.exit(1)


def check_file_extension(filename):
    _, ext = os.path.splitext(filename)
    if ext not in {'.p4', '.p4_14'}:
        print("EXTENSION NOT SUPPORTED: %s" % ext, file=sys.stderr)
        sys.exit(1)


def load_from_p4(compiler_args, cache_dir_name):
    global args
    args = compiler_args

    filename = args['p4_file']

    global p4time
    p4time = os.path.getmtime(filename)

    check_file_exists(filename)
    check_file_extension(filename)

    with RecursionLimit(10000) as recursion_limit:
        hlir = load_hlir(filename, cache_dir_name, args['recompile'])
        
        if 'merge' in args:
            filename2 = args['merge'][0]
            args['p4incdir'] = args['p4incdir2']
            check_file_exists(filename2)
            check_file_extension(filename2)
            hlir2 = load_hlir(filename2, cache_dir_name, args['recompile'])
            hlirInject = load_hlir('./t4p4s/src/p4code/inject.p4','./t4p4s/src/p4code/cache', args['recompile'])
            merger = P4Aggregator(hlir,hlir2,hlirInject,args['SegmentID1'],args['SegmentID2'])
            merger.run()
            hlir = merger.getResult()

        if hlir is None:
            print(f"P4 compilation failed for file {os.path.basename(__file__)}", file=sys.stderr)
            sys.exit(1)

        return hlir
