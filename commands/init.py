import click

@click.command()
def init():
    '''Init project according by karma.toml'''
    pass

def inject(group):
    group.add_command(init)
    
