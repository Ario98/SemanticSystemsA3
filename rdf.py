from rdflib import Graph, URIRef, BNode, Literal
from rdflib.namespace import FOAF, RDF
import pprint
import owlrl

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

    def activate_reasoner(self):
        # -- load ontology with deductive closure - RDFS only
        owlrl.DeductiveClosure(owlrl.RDFS_Semantics).expand(self.g)

        # -- load ontology with deductive closure - OWL2-RL + RDFS
        # owlrl.DeductiveClosure(owlrl.RDFS_OWLRL_Semantics).expand(g)

    def export_graph(self):
        self.g.serialize(format="turtle", destination="export/export.ttl")