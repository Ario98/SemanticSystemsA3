from click_shell import shell
import click
from rdf import rdf_module

# @click.group()  # no longer
@shell(prompt='my-app > ', intro='Starting my app...')
def my_app():
    print('Possible commands: loadontology, printontology')

@my_app.command()
def loadontology():
    rdf.load_ontology()
    print("Ontology loaded.")

@my_app.command()
def printontology():
    rdf.print_ontology()

@my_app.command()
def activatereasoner():
    print('1. RDFS_Semantics')
    print('2. RDFS_OWLRL_Semantics')
    reasoner = input("Enter reasoner:")
    rdf.activate_reasoner(reasoner)
    print("Reasoner {} activated.".format(reasoner))

@my_app.command()
@click.argument('name', type=str)
@click.argument('subclass', type=str, required=False)
def addclass(name, subclass):
    rdf.add_class(name, subclass)
    print('Class {} added.'.format(name))

@my_app.command()
def showqueries():
    rdf.show_queries()
    print("Showing query.")

@my_app.command()
def executequeries():
    rdf.execute_query()

@my_app.command()
def exportgraph():
    print('1. XML')
    print('2. Turtle')
    export_type = input("Enter export type:")
    rdf.export_graph(export_type)
    print("Export type {} finished.".format(export_type))

if __name__ == '__main__':
    rdf = rdf_module()
    my_app()
    
    