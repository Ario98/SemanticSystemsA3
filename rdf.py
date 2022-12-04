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
        # -- TODO: Allow the user to pick the reasoner.
        self.reasoner = reasoner

        print(self.reasoner)

        # -- load ontology with deductive closure - RDFS only
        owlrl.DeductiveClosure(owlrl.RDFS_Semantics).expand(self.g)

        # -- load ontology with deductive closure - OWL2-RL + RDFS
        # owlrl.DeductiveClosure(owlrl.RDFS_OWLRL_Semantics).expand(g)

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
        # -- TODO: Allow the user to pick the export file.
        self.g.serialize(format="turtle", destination="export/export.ttl")