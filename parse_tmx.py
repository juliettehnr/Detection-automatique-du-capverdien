from translate.storage.tmx import tmxfile
import pandas as pd 

sentences_kea = []
sentences_pt = []

with open("./kea-pt.tmx", "rb") as file :
    tmx_file = tmxfile(file, "kea", "pt")
    
    for node in tmx_file.unit_iter():
        sentences_kea.append(node.source)
        sentences_pt.append(node.target)

data = [{'lang': 'kea', 'text' : phrase} for phrase in sentences_kea]+ [{'lang' : 'pt', 'text' : phrase} for phrase in sentences_pt]
df = pd.DataFrame(data)

    


