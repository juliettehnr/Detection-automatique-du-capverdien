# Detection de Langue : capverdien-portugais
Entrainement d'un classifieur pour la détection du créole capverdien

Ce projet s'inscrit dans le cours *Langue peu dotées* donné par Mme Ilaine WANG & Mme Johanna CORDOVA de l'INALCO.

## 📌 Objectif

- Développer un **classifieur de langue** qui identifie si une phrase donnée est en créole capverdien ou en portugais.
- Permettre une **détection automatique fiable** dans les corpus multilingues pour faciliter la constitution de ressources de meilleure qualité.

## 🧠 Approche Méthodologique

1. **Corpus utilisé**
   - Corpus parallèle provenant du projet *No Language Left Behind* (NLLB).
   - Données étiquetées pour capverdien (« kea ») et portugais (« pt »). 

2. **Prétraitement**
   - Extraction et structuration des données en DataFrame.
   - Transformation des textes en séquences entières à l’aide d’un tokenizer Keras.

3. **Modèle**
   - Architecture RNN (Long Short‑Term Memory, LSTM) construite avec Keras.
   - Comprend une couche *Embedding*, une couche *LSTM* et un dense de sortie binaire.
   - Sortie : proche de 0 pour capverdien, proche de 1 pour portugais.
  
## 📊 Résultats

Le modèle a obtenu d’excellentes performances sur le jeu de test, avec des scores de précision, de rappel et de F‑mesure **toujours ≥ 0,98** pour les deux langues. 

## 👥 Contributrices

- [Maiwenn PLEVENAGE](https://github.com/00parts)
- [Juliette HENRY](https://github.com/juliettehnr)
