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
        # TODO: Fix
        self.domain = domain
        self.property = property
        self.range = range

        self.URIdomain = URIRef("http://semantics.id/ns/example/film#" + self.domain)
        self.URIproperty = URIRef("http://semantics.id/ns/example/film#" + self.property)
        self.URIrange = URIRef("http://semantics.id/ns/example/film#" + self.range)

        self.g.add((self.URIproperty, RDF.type ,OWL.ObjectProperty))
        self.g.add((self.URIproperty, RDFS.label, Literal(self.property)))
        self.g.add((self.URIproperty, RDFS.domain, self.domain))
        self.g.add((self.URIproperty, RDFS.range, self.range))

    def add_instance(self, objectName, instanceName):
        self.objectName = objectName
        self.instanceName = instanceName

        self.URIobjectName = URIRef("http://semantics.id/ns/example#" + self.objectName)
        self.URIinstanceName = URIRef("http://semantics.id/ns/example/film#fullName")

        self.g.add((self.URIobjectName, RDF.type, OWL.NamedIndividual))
        self.g.add((self.URIobjectName, self.instanceName, Literal(self.URIinstanceName)))