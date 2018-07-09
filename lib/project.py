import os
from lib import logger
import sys
from functools import lru_cache
import toml

@lru_cache(maxsize=32)
def project_root():
    # Find project base dir
    project = os.path.abspath('.')
    dirname = project
    basename = os.path.split(project)[1]
    while not os.path.exists(dirname+'/karma.toml') and basename!='':
        dirname = os.path.split(dirname)[0]
        basename = os.path.split(dirname)[1]
    if basename == '':
        logger.info('Abort! Can\'t find karma.toml file.')
        sys.exit(1)
    project = dirname
    return project

@lru_cache(maxsize=32)
def get_config():
    root = project_root()
    return get_project_config(root)

@lru_cache(maxsize=32)
def get_project_config(path):
    try:
        config = toml.load(path+'/karma.toml')
        return config
    except Exception as e:
        logger.info('Abort! load config error')
        sys.exit(1)

def _find_package(path):
    if os.path.exists(path + '/karma.toml'):
        return path
    else:
        for x in os.listdir(path):
            return _find_package(os.path.join(path,x))


def _all_files(path,expect,result):
    r = os.listdir(path)
    for f in r:
        if f in expect:
            continue
        p = os.path.join(path,f)
        if os.path.isdir(p):
            _all_files(p,expect,result)
        else:
            ext = os.path.splitext(p)[1]
            result[ext] = os.path.relpath(p,project_root())

def all_files(path,expect):
    result = {}
    _all_files(path,expect,result)
    return result

def _load_files(path,ext,expect,result):
    r = os.listdir(path)
    for f in r:
        if f in expect:
            continue
        p = os.path.join(path,f)
        if os.path.isdir(p):
            _load_files(p,ext,expect,result)
        elif os.path.splitext(p)[1] in ext:
            result.append(p)


def load_files(path,ext,expect):
    result = []
    _load_files(path,ext,expect,result)
    return result
