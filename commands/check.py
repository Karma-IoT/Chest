import click
from lib import checker

@click.command()
def check():
    '''Check project dependenices'''
    checker._check('.chest/target')
def inject(group):
    group.add_command(check)
    
