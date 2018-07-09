from lib import loader
import click
import os

@click.group()
def karma():
    pass

class Commands:
    def __init__(self):
        self._commands = []
        for f in os.listdir(loader.base_dir + '/commands'):
            if os.path.splitext(f)[1] == '.py':
                command = loader.load(os.path.splitext(f)[1],'commands/'+f)
                self._commands.append(command)

    def reg(self):
        for x in self._commands:
            x.inject(karma)

    def main(self):
        karma()

