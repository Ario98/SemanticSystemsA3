from click_shell import shell
import click
from rdf import rdf_module

@shell(prompt='semantic-systems-app > ', intro='Starting the app...')
def my_app():
    print('Possible commands: ')
    print("""

[] - denotes an input 

loadontology - loads the provided ontology in the input/graph folder
printology - prints the ontology.
activatereasoner - prints the available reasoners and then offers the input to user with numeric variables.
addclass [] - takes two inputs, the class name and subclass (optional).
addproperty [] - takes three inputs: domain, property and range.
addinstance [] - takes two inputs: object name and instance name.
showqueries - prints all available queries.
executequery [] - takes one input: an int variable from 1-3
executeconstructquery - executes the single construct query found in input/query and saves the result to the export folder.
exportgraph - saves the graph to a user chosen type.
exit - exits the app.

""")

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
@click.argument('domain',  type=str)
@click.argument('property', type=str)
@click.argument('range', type=str)
def addproperty(domain, property, range):
    rdf.add_property(domain, property, range)
    print('Property {} added.'.format(property))

@my_app.command()
@click.argument('objectname',  type=str)
@click.argument('instancename', type=str)
def addinstance(objectname, instancename):
    rdf.add_instance(objectname, instancename)
    print('Added {} instance.'.format(instancename))

@my_app.command()
def showqueries():
    print('Showing available queries:')
    rdf.show_queries()
    print("Call the function executequery with your chosen query to execute it. Example: executequery 1")

@my_app.command()
@click.argument('querychoice', type=int)
def executequery(querychoice):
    rdf.execute_query(querychoice)

@my_app.command()
def executeconstructquery():
    rdf.execute_construct_query()

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
    
    