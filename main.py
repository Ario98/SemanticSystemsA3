from click_shell import shell
from rdf import rdf_module

# @click.group()  # no longer
@shell(prompt='my-app > ', intro='Starting my app...')
def my_app():
    pass

@my_app.command()
def loadontology():
    rdf.load_ontology()

@my_app.command()
def printontology():
    rdf.print_ontology()

if __name__ == '__main__':
    rdf = rdf_module()
    my_app()
    
    