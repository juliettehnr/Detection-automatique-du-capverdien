# Importation des librairies
from translate.storage.tmx import tmxfile
from sklearn.model_selection import train_test_split
import pandas as pd 

# Création du dataframe
sentences_kea = []
sentences_pt = []

with open("./kea-pt.tmx", "rb") as file :
    tmx_file = tmxfile(file, "kea", "pt")
    
    for node in tmx_file.unit_iter():
        sentences_kea.append(node.source)
        sentences_pt.append(node.target)

data = [{'lang': 'kea', 'text' : phrase} for phrase in sentences_kea[:50000]]+ [{'lang' : 'pt', 'text' : phrase} for phrase in sentences_pt[:50000]]
df = pd.DataFrame(data)
df = df.sample(frac=1, random_state=42).reset_index(drop=True) #on mélange les données

# Split en train/test
df_train, df_test = train_test_split(
    df,
    test_size=0.2,
    random_state=42
)

# Création des fichiers CSV
df_train.to_csv(
    "train.csv",
    index=False,
    encoding="utf-8"
)

df_test.to_csv(
    "test.csv",
    index=False,
    encoding="utf-8"
)

# Vérification
"""
print(df.head())
print("Train :", len(df_train))
print("Test :", len(df_test))
print(df_train["lang"].value_counts())
print(df_test["lang"].value_counts())
"""
