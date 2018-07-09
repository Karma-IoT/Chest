import click

@click.command()
def test():
    '''test'''
    pass

def inject(group):
    group.add_command(test)
    
