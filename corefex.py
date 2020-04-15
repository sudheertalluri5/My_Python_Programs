# Load your usual SpaCy model (one of SpaCy English models)
import spacy

nlp = spacy.load('en')

# Add neural coref to SpaCy's pipe
import neuralcoref
neuralcoref.add_to_pipe(nlp)

# You're done. You can now use NeuralCoref as you usually manipulate a SpaCy document annotations.
doc = nlp(open('myInput.txt').read())

print(doc._.has_coref)
print(doc._.coref_clusters)
print(type(doc._.coref_clusters[0][1:]))
temp=doc._.coref_clusters
coref_art=dict()
for i in range(len(temp)):
    coref_art[temp[i][0].text.lower()]=[]
    for j in range(len(temp[i])-1):
        coref_art[temp[i][0].text.lower()].append(temp[i][j+1].start)                

