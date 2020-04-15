# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 03:09:42 2019

@author: sudhe
"""

import spacy

nlp = spacy.load('en_coref_md')

doc = nlp(u'Phone area code will be valid only when all the below conditions are met. It cannot be left blank. It should be numeric. It cannot be less than 200. Minimum number of digits should be 3. ')

print(doc._.coref_clusters)

print(doc._.coref_resolved)