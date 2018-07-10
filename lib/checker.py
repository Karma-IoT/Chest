from lib import project
from lib import fetcher
import sys
from lib import logger

def _cmp(a,b):
    for x in a:
        if ( not x in b ) or ( not 'general' in b ):
            logger.info('Abort! Dependencies is not satisfied')
            sys.exit(1)
    return True


def _run(path,target,target_arch='',target_platfrom=''):
    print(path,target_arch,target_platfrom)
    arch = project.get_project_config(path)['project']['arch']
    platfrom = project.get_project_config(path)['project']['platform']
    dependencies = project.get_project_config(path)['dependencies']
    if target_arch != '':
        _cmp(target_arch,arch)
    if target_platfrom !='':
        _cmp(target_platfrom,platfrom)
    for k,v in dependencies.items():
        ppath = project.project_root() + '/' + target + '/' + k + '-' + fetcher._get_name(v)
        _run(ppath, target, arch, platfrom)

def _check(target):
    root = project.project_root()
    _run(root,target)

