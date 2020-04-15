# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:33:10 2019

@author: sudhe
"""

from SPARQLWrapper import SPARQLWrapper, JSON
import re

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
queryString="""
        SELECT ?label
        WHERE { <http://dbpedia.org/page/Apple_Inc.> dbo:board ?label }"""
sparql.setQuery(queryString)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print(results)