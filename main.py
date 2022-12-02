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
    reasoner = input("Enter reasoner:")
    rdf.activate_reasoner(reasoner)
    print("Reasoner activated.")

@my_app.command()
def exportgraph():
    export_type = input("Enter export type:")
    rdf.export_graph(export_type)

if __name__ == '__main__':
    rdf = rdf_module()
    my_app()
    
    