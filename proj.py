# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 19:55:37 2019

@author: sudhe
"""
import spacy
import networkx as nx
nlp=spacy.load('en_core_web_sm')

def My_Rank(article,req,lex=False):
    rank=0
    den=0
    n=len(article)
    for i in range(n):
        if req in article[i]:
            if(lex):
                rank+=(i+1)
                den+=n
            else:
                rank+=(n-i)
                den+=n
    if(rank==0):
        return 0
    return rank/den

articles=[]
x="myInput.txt"
y=open(x).read()
articles.append(y)

knowledgeBase={'Company':['Apple'],'keyPeople':['Tim Cook','Steve Jobs'],'products':['iMac','iPhone','iPod','iPad']}

lexrank=[]
posrank=[]
def weights(entity):
    return 1
myvalues=[]
for value in list(knowledgeBase.values()):
    for val in value:
        myvalues.append(val.lower())
for i, article in enumerate(articles):
    doc=nlp(article)
    sentences=[]
    start_sen=[]
    for sent in doc.sents:
        sentences.append(sent.text.lower())
        start_sen.append(sent.start)
    print(start_sen)
    #lexArticle=Int_Page_Rank(article)
#    print(lexArticle)
    for i in range(len(sentences)):
        print(i,sentences[i])
    for value in myvalues:
        #lexrank.append(My_Rank(lexArticle,value,True))
        posrank.append(My_Rank(sentences,value))
#print(lexrank)
print(posrank)