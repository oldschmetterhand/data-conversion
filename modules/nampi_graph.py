"""The module for the Nampi_graph class.

Classes:
    Nampi_graph

"""
import uuid
from datetime import datetime
from typing import Dict, List, Optional, TypeVar, Union

from modules.nampi_ns import Nampi_ns
from rdflib import RDF, RDFS, XSD, BNode, Graph, Literal, Namespace, URIRef


class Nampi_graph:
    """A wrapper around the rdflib Graph class that makes frequent actions for the parser more concise."""

    graph: Graph

    def __init__(self) -> None:
        """Initialize the class."""
        self.graph = Graph()
        self.graph.bind("acts", Nampi_ns.acts)
        self.graph.bind("core", Nampi_ns.core)
        self.graph.bind("events", Nampi_ns.events)
        self.graph.bind("groups", Nampi_ns.groups)
        self.graph.bind("mona", Nampi_ns.mona)
        self.graph.bind("objects", Nampi_ns.objects)
        self.graph.bind("persons", Nampi_ns.persons)
        self.graph.bind("places", Nampi_ns.places)
        self.graph.bind("sources", Nampi_ns.sources)

    def __create_entity(self, ns: Namespace) -> URIRef:
        """Create an entity to be added to the graph. The URI is a combination of the provided namespace and random identifier."""
        return ns[str(uuid.uuid4())]

    @staticmethod
    def date_time_literal(date_string: str) -> Literal:
        """Transform a date string into an rdflib datetime literal.

        Parameters:
            date_string: The string in the format of "YYYY-MM-DD".

        Returns:
            A datetime Literal.
        """
        return Literal(datetime.strptime(date_string, "%Y-%m-%d"))

    @staticmethod
    def string_literal(string: str) -> Literal:
        """Transform a string into an rdflib literal.

        Parameters:
            string: The string to transform.

        Returns:
            A rdflib literal.
        """
        return Literal(string, datatype=XSD.string)

    def add(
        self,
        subj: Union[URIRef, BNode, Literal],
        pred: URIRef,
        obj: Union[URIRef, BNode, Literal],
    ) -> None:
        """Add a rdf triple to the graph.

        Parameters:
            subj: The subject, can be a full resource with an URIRef or a blank node.
            pred: The predicate of the triple, a URIRef.
            obj: The object, can be a full resource with an URIRef or a blank node.

        """
        self.graph.add((subj, pred, obj))

    def add_blind(self, type_uri: URIRef) -> BNode:
        """Add a blind node to the graph.

        Parameters:
            type_uri: The URI of the type for the blank node.

        Returns:
            The reference to the blank node.

        """
        node = BNode()
        self.add(node, RDF.type, type_uri)
        return node

    def add_resource(self, ns: Namespace, type_uri: URIRef) -> URIRef:
        """Add a resource to the graph.

        Parameters:
            ns: The namespace the resource will be added to. The full URI will be a combination of the namespace and a random identifier.
            type_uri: The URI of the resource type.

        Returns:
            The reference to the resource.
        """
        node = self.__create_entity(ns)
        self.add(node, RDF.type, type_uri)
        return node

    def add_labeled_resource(
        self, ns: Namespace, type_uri: URIRef, label: str
    ) -> URIRef:
        """Add a labeled resource to the graph if it doesn't already exist.

        The method tries to find a resource with the label in the graph and only creates a new one if it doesn't find anything.

        Parameters:
            ns: The namespace the resource will be added to. The full URI will be a combination of the namespace and a random identifier.
            type_uri: The URI of the resource type.
            label: The label of the resource.

        Returns:
            The reference to the resource.
        """
        query = 'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> SELECT ?subject WHERE {{ ?subject rdfs:label "{}"}}'.format(
            label
        )
        resources = self.graph.query(query)
        if len(resources) == 0:
            node = self.add_resource(ns, type_uri)
            self.add(node, RDFS.label, Literal(label))
            return node
        else:
            for row in resources:
                return row[0]
