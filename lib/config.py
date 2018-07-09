import toml
import os

dot_default = os.environ['CHEST_DOT_DEFAULT'] if 'CHEST_DOT_DEFAULT' in os.environ else '~/.chest'

def _init_default_dot(dot_default):
    # init toml file
    # init 
    pass

def get(key):
    if key == 'user.package':
        return 'tiannian'
    elif key == 'user.maintainer':
        return 'tiannian'

def set(key,value):
    pass

