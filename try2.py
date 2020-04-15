# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 19:55:37 2019

@author: sudhe
"""
import spacy
import neuralcoref
import numpy as np
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity 

coref_nlp=spacy.load('en')
neuralcoref.add_to_pipe(coref_nlp)
nlp=spacy.load('en_core_web_sm')

# Extract word vectors

def My_Page_Rank(sentences):
    sentence_vectors=[]
    lexArticle=dict()
    for sentence in sentences:
        if len(sentence)!=0:
            v= sum([word_embeddings.get(w, np.zeros((300,))) for w in sentence.split()])/(len(sentence.split())+0.001)
        else:
            v=np.zeros((300,))
        sentence_vectors.append(v)
    sim_mat=np.zeros([len(sentences),len(sentences)])
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i!=j:
                sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1,300), sentence_vectors[j].reshape(1,300))[0,0]
    nx_graph=nx.from_numpy_array(sim_mat)
    scores=nx.pagerank(nx_graph)
    ranked_sentences=sorted((scores[i],s) for i,s in enumerate(sentences))

    for i in range(len(ranked_sentences)):
        lexArticle[i]=ranked_sentences[i][1]
    return lexArticle
def My_Lex_Rank(article,req):
    rank=0
    den=0
    n=len(article)
    for i in range(n):
        if req in article[i]:
            rank+=(i)
            den+=n
    if(rank==0):
        return 0
    return rank/den
def My_Pos_Rank(sent_art,coref_art,req):
    rank=0
    den=0
    n=len(sent_art)
    sentence=dict()
    for i in range(n):
        sentence[i]=True
        if req in sent_art[i]:
            rank+=(n-i)
            den+=n
            sentence[i]=False
    for key in list(coref_art.keys()):
        if req in key:
            for i in coref_art[key]:
                if(sentence[i]):
                    rank+=(n-i)
                    den+=n
                    sentence[i]=False
            break
    if(rank==0):
        return 0
    return rank/den

articles=[]
x="myInput.txt"
y=open(x).read()
articles.append(y)
#context manager, generator,
knowledgeBase={'Company':['Apple'],'keyPeople':['Tim Cook','Steve Jobs'],'products':['iMac','iPhone','iPod','iPad']}

lexrank=[]
posrank=[]
def weights(entity):
    return 1
myvalues=[]
for value in list(knowledgeBase.values()):
    for val in value:
        myvalues.append(val.lower())
for article in articles:
    doc=nlp(article)
    sentences=[]
    start_sen=dict()
    docc=coref_nlp(article)
    coref_art=dict()
    if(docc._.has_coref):
        temp=docc._.coref_clusters
        print(temp)
        for i in range(len(temp)):
            coref_art[temp[i][0].text.lower()]=[]
            for j in range(len(temp[i])-1):
                coref_art[temp[i][0].text.lower()].append(temp[i][j+1].start)
    for i,sent in enumerate(doc.sents):
        sentences.append(sent.text.lower())
        for j in range(sent.start,sent.end):
            start_sen[j]=i
    temp2=dict()
    for key in list(coref_art.keys()):
        temp2[key]=set()
        for coref in coref_art[key]:
            temp2[key].add(start_sen[coref])
    #print(start_sen)
    print(temp2)
    coref_art=temp2
    lexArticle=My_Page_Rank(sentences)#ranking sentences based on information
    print(lexArticle)
    for i in range(len(sentences)):
        print(i,sentences[i])
    for value in myvalues:
        lexrank.append(My_Lex_Rank(lexArticle,value))#pagerank 
        posrank.append(My_Pos_Rank(sentences,coref_art,value))#positional and coref rank combined
print(lexrank)
print(posrank)
