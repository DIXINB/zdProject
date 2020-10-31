print('Run zdpr')
import click

@click.group()
def cli():
    pass

@click.command()
@click.argument('name')
def file(name):
    global NAME
    print(f'We will write {name}')  
    NAME=str(name)
    import zdpr.src.z1413n
@click.command()
@click.argument('name')
def view(name):
   global NAME
   print(f'You have selected file {name} for processing ')
   NAME=str(name)
   import zdpr.src.visualization.vizualize
@click.command()
@click.argument('name')
def test(name):
   global NAME
   print(f'Testing was done with {name} ')
   NAME=str(name)
   import zdpr.utest10e2
cli.add_command(file)   
cli.add_command(view)
cli.add_command(test)
cli()	