from rdflib import Graph, URIRef, BNode, Literal
from rdflib.namespace import FOAF, RDF, OWL, RDFS
import pprint
import owlrl
import os

class rdf_module:

    def __init__(self):
        self.g = Graph()

    def load_ontology(self):
        # -- load ontology (file)
        self.g.parse("input/graph/film.ttl")

        # -- load instances (file)
        self.g.parse("input/graph/film-instances.ttl")

    def print_ontology(self):
        for stmt in self.g:
            print(stmt)

    def activate_reasoner(self, reasoner):
        self.reasoner = reasoner

        if self.reasoner == '1':
            owlrl.DeductiveClosure(owlrl.RDFS_Semantics).expand(self.g)
        elif self.reasoner == '2':
            owlrl.DeductiveClosure(owlrl.RDFS_OWLRL_Semantics).expand(self.g)
        else:
            print('Invalid input.')

    def show_queries(self):
        # -- QUERIES
        for query in os.listdir('input/query'):
            print(query)

    def execute_query(self, queryChoice):
        self.queryChoice = queryChoice
        query_list = []

        for query in os.listdir('input/query'):
            q = open('input/query/' + query).read()
            query_list.append(q)
        
        if self.queryChoice == 3:
            print('This is a construct query. Call executeconstructquery to execute it.')
            return
        else:
            result = self.g.query(query_list[self.queryChoice - 1])
            print("--- "+query+" ---")
            for row in result:
                print(row)

    def execute_construct_query(self):
        query_list = []

        for query in os.listdir('input/query'):
            q = open('input/query/' + query).read()
            query_list.append(q)

        result = self.g.query(query_list[2])
        print("--- "+query+" ---")
        for row in result:
            print(row)

        print('Saving the result as a Turtle file to the export folder.')
        result.serialize(format="turtle", destination= "export/constructResult.ttl")
 
    def export_graph(self, export_type):
        self.export_type = export_type

        if self.export_type == '1':
            self.g.serialize(format="pretty-xml", destination="export/export.xml")
            return
        elif self.export_type == '2':
            self.g.serialize(format="turtle", destination= "export/export.ttl")
        else:
            print('Invalid input.')

    def add_class(self, name, subclass):
        self.name = name
        self.subclass = subclass
        self.URIname = URIRef("http://semantics/id/ns/example/film#" + self.name)
    
        if self.subclass is None:
            self.g.add((self.URIname, RDF.type, OWL.Class))
        else:
            self.URIsubclass = URIRef("http://semantics.id/ns/example/film#" + self.subclass)
            self.g.add((self.URIname, RDFS.subClassOf, self.URIsubclass))

        self.g.add((self.URIname, RDFS.label, Literal(self.name)))

    def add_property(self, domain, property, range):
        propertyURI = URIRef("http://semantics.id/ns/example/film#" + property)
        domain = URIRef("http://semantics.id/ns/example/film#" + domain)
        range = URIRef("http://semantics.id/ns/example/film#" + range)

        self.g.add((propertyURI, RDF.type ,OWL.ObjectProperty))
        self.g.add((propertyURI, RDFS.label, Literal(property)))
        self.g.add((propertyURI, RDFS.domain, domain))
        self.g.add((propertyURI, RDFS.range, range))

    def add_instance(self, objectName, instanceName):
        URIobject = URIRef("http://semantics.id/ns/example#" + objectName)
        URIname = URIRef("http://semantics.id/ns/example/film#fullName")

        self.g.add((URIobject, RDF.type, OWL.NamedIndividual))
        self.g.add((URIobject, URIname, Literal(instanceName)))