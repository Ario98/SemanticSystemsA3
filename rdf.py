from rdflib import Graph, URIRef, BNode, Literal
from rdflib.namespace import FOAF, RDF
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

    def execute_query(self):
        # -- QUERIES
        for query in os.listdir('input/query'):
            q = open('input/query/' + query).read()
            result = self.g.query(q)
            print("--- "+query+" ---")
            for row in result:
                print(row)


    def export_graph(self, export_type):
        self.export_type = export_type

        if self.export_type == '1':
            self.g.serialize(format="pretty-xml", destination="export/export.xml")
            return
        elif self.export_type == '2':
            self.g.serialize(format="turtle", destination= "export/export.ttl")
        else:
            print('Invalid input.')