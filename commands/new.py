import click
import os
import toml
from lib import config as gc

@click.command()
@click.argument('name',default='')
def new(name):
    '''New project configure file.'''
    f = ''
    if name == '':
        name = os.path.basename(os.getcwd())
        f = open('karma.toml', 'w+')
    else:
        os.mkdir(name)
        f = open(name + '/karma.toml', 'w+')

    config = {}
    
    project = {}
    
    iname = input('Chest name: (%s) '% name)
    project['name'] = name if iname == '' else iname

    package = gc.get('user.package')
    ipackage = input('package name: (%s) '% package)
    project['package'] = package if ipackage == '' else ipackage

    iversion = input('version: (0.1.0) ')
    project['version'] = '0.1.0' if iversion == '' else iversion

    maintainer = gc.get('user.maintainer')
    imaintainer = input('maintainer: (%s) '% maintainer)
    project['maintainer'] = maintainer if imaintainer == '' else imaintainer
    
    iupstream = input('upstream: () ')
    project['upstream'] = '' if iupstream == '' else iupstream



    config['project'] = project

    toml.dump(config, f)
    f.close()

    



def inject(group):
    group.add_command(new)
    
