import os
from lib import project
import shutil
import urllib.request
import tarfile
from lib import logger
import hashlib
import tempfile
import sys
import commands

def _get_name(obj):
    h = hashlib.sha256()
    if type(obj) == str:
        h.update(obj.encode())
        return h.hexdigest()[:8]
    else:
        try:
            h.update(obj['type'].encode())
            h.update(obj['info'].encode())
            return h.hexdigest()[:8]
        except Exception as e:
            print(e)
            logger.info('Abort! Dependencies only support string or table.')
            sys.exit(1)

def _deal_package(tmp):
    return project._find_package(tmp)

def _m_file(info, path):
    if os.path.isdir(info):
        p = _deal_package(info)
        shutil.copytree(p,path)
    else:
        try:
            tmp = tempfile.TemporaryDirectory()
            shutil.unpack_archive(info,tmp.name)
            p = _deal_package(tmp.name)
            shutil.move(p,path)
        except Exception as e:
            logger.info('Abort! Unsupport archive format.')
            sys.exit(1)


def _m_git(info, path):
    if shutil.which('git') == None:
        logger.info('[KBT] -- Abort! Can\'t find git. Please install git.')
        sys.exit(1)
    tmp = tempfile.TemporaryDirectory()
    os.system('git clone %s %s' % (info,tmp.name))
    p = _deal_package(tmp.name)
    shutil.copytree(p,path)

typer = {
        'git':_m_git,
        'file':_m_file,
        }

def _download(key,obj,path):
    if type(obj) == str:
        #download from github
        url = "https://codeload.github.com/%s/tar.gz/%s"%(key.replace('.','/'),obj)
        f = urllib.request.urlretrieve(url)[0]
        tmp = tempfile.TemporaryDirectory()
        tarfile.open(f).extractall(tmp.name)
        p = _deal_package(tmp.name)
        shutil.move(p,path)
    else:
        try:
            if obj['type'] in typer:
                typer[obj['type']](obj['info'], path)
            else:
                logger.info('Abort! Type %s not support.' % obj['type'])
                sys.exit(1)
        except Exception as e:
            logger.info('Abort! Dependencies only support string or table.')
            sys.exit(1)

def _fetch(target):
    def _d(key, value):
        # parse toml file and download
        ppath = project.project_root() + '/' + target + '/' + key + '-' + _get_name(value)
        if not os.path.exists(ppath):
            logger.info('Fetching %s ...' % key)
            _download(key,value,ppath)
        config = project.get_project_config(ppath)
        for k,v in config['dependencies'].items():
            _d(k,v)
    #parse toml file and call _d
    obj = project.get_config()
    for k,v in obj['dependencies'].items():
        _d(k,v)


