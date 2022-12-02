from click_shell import shell
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
    rdf.activate_reasoner()
    print("Reasoner activated.")

@my_app.command()
def exportgraph():
    rdf.export_graph()

if __name__ == '__main__':
    rdf = rdf_module()
    my_app()
    
    