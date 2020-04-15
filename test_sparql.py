from SPARQLWrapper import SPARQLWrapper, JSON
import re

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
properties=["keyPerson","industry","product","locationCity","service"]
#propertiesp=["founders","qoute",]
res=[]
i=0
for prop in properties:
    queryString="""
        SELECT ?label
        WHERE { <http://dbpedia.org/resource/Apple_Inc.> dbo:"""+prop+" ?label }"
    sparql.setQuery(queryString)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    values=[]
    for result in results["results"]["bindings"]:
        x=re.split("/",result["label"]["value"])
        values.append(x[len(x)-1])
    temp={}
    temp[prop]=values
    res.append(temp)
    i+=1
print(res)