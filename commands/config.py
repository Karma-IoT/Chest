import click

@click.command()
def config():
    '''test'''
    pass

def inject(group):
    group.add_command(config)
    
