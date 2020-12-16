"""
.. module:: DSO

 Translated by owl2rflib

 Translated to RDFlib from ontology http://www.semanticweb.org/directory-service-ontology#

 :Date 16/12/2020 18:17:12
"""
from rdflib import URIRef
from rdflib.namespace import ClosedNamespace

DSO =  ClosedNamespace(
    uri=URIRef('http://www.semanticweb.org/directory-service-ontology#'),
    terms=[
        # Classes
        'Deregister',
        'InfoAgent',
        'ServiceAgent',
        'SolverAgent',
        'Modify',
        'RegisterAction',
        'Search',
        'RegisterResult',
        'Register',
        # Object properties
        'AgentType',
        # Data properties
        'Uri',
        'Address',
        'Name'
    ]
)
