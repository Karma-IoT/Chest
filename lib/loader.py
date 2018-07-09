import importlib.util

base_dir = ''

def load( name, path ):
    #  print(name,path)
    spec = importlib.util.spec_from_file_location(name,base_dir + '/' + path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
