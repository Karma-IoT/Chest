import click
from lib import fetcher

@click.command()
def fetch():
    '''Fetch all dependencies.'''
    fetcher._fetch('.chest/target')

def inject(group):
    group.add_command(fetch)
    
