"""
.. module:: ACL

 Translated by owl2rflib

 Translated to RDFlib from ontology http://www.nuin.org/ontology/fipa/acl

 :Date 16/12/2020 18:22:11
"""
from rdflib import URIRef
from rdflib.namespace import ClosedNamespace

ACL =  ClosedNamespace(
    uri=URIRef('http://www.nuin.org/ontology/fipa/acl'),
    terms=[
        # Classes
        'SpeechAct',
        'FipaAclMessage',
        'KsMessage',
        # Object properties
        'sender',
        'receiver',
        'ontology',
        'reply_to',
        'performative',
        # Data properties
        'reply_by',
        'conversation_id',
        'encoding',
        'in_reply_to',
        'reply_with',
        'content',
        'language'
    ]
)
