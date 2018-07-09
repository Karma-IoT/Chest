import click
from lib import fetcher

@click.command()
def fetch():
    '''fetch all dependencies.'''
    fetcher._fetch('target')

def inject(group):
    group.add_command(fetch)
    
