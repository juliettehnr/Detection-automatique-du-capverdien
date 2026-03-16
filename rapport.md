# Rapport - Écriture et Oral Multilingue

- Groupe : Maiwenn PLEVENAGE (IM) & Juliette HENRY (R&D)
- Langue : Le créole capverdien
- Outil : Détecteur de langue pour l’écrit

## I - Le créole capverdien

Les créoles sont des langues qui se créent par contact entre un superstrat
linguistique d’une population dominante et un substrat linguistique d’une autre population
dominée. Dans le cas du créole du Cap-Vert, le contact s’est fait entre les colons portugais
et les esclaves d’origine ouest-africaine au XVIe siècle.
On peut retrouver cette langue sous différentes appellations : créole capverdien,
capverdien (en français), kriolu, kabuverdianu, kriolu kabuverdianu (en créole capverdien),
crioulu cabo-verdiano, cabo-verdiano (en portugais). Son code ISO est kea. Elle est
aujourd’hui parlée par environ 900 000 personnes dans le monde, principalement au
Cap-Vert mais aussi dans les diasporas. Le Cap-Vert étant un archipel d’îles, chaque île
possède sa propre variation de la langue. On peut tout de même regrouper les différents
“dialectes” en deux groupes : les variations dialectales du Nord (les îles de Barlavento) et
celles du Sud (les îles de Sotavento).

Le Cap-Vert obtient son indépendance en 1975. La constitution de 1999 déclare le
portugais comme langue officielle du pays (article 9-1). Mais elle déclare aussi “la langue
maternelle capverdienne à parité avec la langue portugaise” (article 9-2), sans lui donner un
réel statut officiel. Les capverdiens vivent donc dans une situation de diglossie, où le créole
capverdien est parlée dans les relations quotidiennes (98% des capverdiens parlent le
créole) et le portugais est enseigné à l’école et utilisé dans l’administration. On ne peut donc considérer cette langue comme étant en danger (voir Fig.2), mais son statut ambigu freine son institutionnalisation.


Par exemple, le capverdien n’est pas standardisé à l’écrit. On peut néanmoins citer
le projet ALUPEC (Alfabeto Unificado para a Escrita do Caboverdiano) apparu en 1994 et
officiellement reconnu par le gouvernement en 2005. Son but n’est pas d’unifier
l’orthographe au Cap-Vert mais plutôt de proposer un alphabet phonétique que tout le
monde pourrait comprendre, où une lettre est égale à un phonème. Ainsi, l’orthographe du
capverdien reste sujette à beaucoup de variations insulaires, voire même individuelles.

Figure 2 : Vitalité de la langue selon ethnologue.com
Figure 1 : Niveau de ressources numériques du capverdien selon ethnologue.com

En août 2025, l’Institut Universitaire de Lisbonne a annoncé un projet en TAL en
partenariat avec l’Université du Cap-Vert : ORAL (kriOl(u) laRge lAnguage modeLs), visant à
développer des modèles de langue et des outils de traitement automatique pour le
capverdien. Ce projet a débuté en octobre 2025 et a plusieurs objectifs : en premier lieu, le
développement et la mise en accès libre de nombreuses ressources en capverdien. Cela
inclut des corpus parallèles capverdien-portugais, des corpus écrits et oraux dans les
variétés de Sao Vicente et Santiago, ainsi qu’un glossaire phonétique. Le second objectif est
de développer des outils numériques de TAL, tels que de la reconnaissance vocale pour le
capverdien, un chatbot/voicebot, ainsi que des LLMs pour la génération de texte et la
traduction capverdien-portugais. Toutes ces ressources et outils seront en accès
open-source et public. Avec ce projet, les institutions portugaises et capverdiennes espèrent
avancer vers une standardisation et une officialisation du créole capverdien.

## II - Outils existants

### A) Outils pour l’oral

Le modèle de langue MMS-1B-all propose la reconnaissance du capverdien à l’oral
(LID) et sa transcription à l’écrit (ASR). Le script LID n’a eu aucun problème pour détecter
notre fichier audio en capverdien et a bien affiché son code ISO kea. En revanche, le script
ASR a renvoyé un fichier contenant quelques erreurs, notamment de segmentation, selon la
personne native du capverdien qui nous a aidé dans notre projet :
mai galinha sta okupadu mai galinha sta ta spera pa se fidjus nas kantu ténpu ki el tenki
spera el ta konsigi bai pa fera mai galinha sta xintadu riba di se ovu el sta ta spera y spera
pa se fidju sai di ovu mai kabra ben ta pasa y el pirgunta mai galinha bu sta ta bai pa fera
ku mi galinha risponde-l sta okupadu ku nhas ovu u 2,-3ê-4 5 y 6a sa djaovu rodondu mai
porka tanbê ben ta pasa y el pirgunta mai galinha bu kra bai pa fera ku mi galinha
risponde-l l sta okupadu ku nhas ovu u,2-3-45 y 6ai sa dj ovu rodondu dipôs mai baka ben
ta pasa y el pirgunta mai galn bu sta ta bai pa fera ku mi mai galinha rispondel sta
okupadu ku nhas ovu mai galinha fika ta spera y spera el fika ta pirgunta se kabesa kantu
ténpu ki n ten ki spera pa m odja nhes fidju ki rapenti mai galinha xinti algun kuza kuza ki
sta ta kontise u 2-345 y 6a nase sais fidju mai galinha sta rei di kontenti ku se fidjus ki el
kre txeu nton mai galinha lenbra oji ten fera mai kabra mai porka mai baka dja bai pa fera
gosi mai galinha djas sta prontu el leba tudu se fidjus pa fera ku el u2-345 y 6a mai
galinha ku se 6ais fidju pasa sabe na fer mai galinha fla forti sadu bali pena spera

Table 1 : Résultat du test ASR

“tenki” devrait être séparé en deux mots : “ten” et “ki”. “risponde-l” devrait être “rispondel”.
On peut aussi noter que ces mots sont bien retranscris plus bas, on peut retrouver “ten ki”
ainsi que “rispondel” bien orthographiés. Par ailleurs, le modèle a du mal à retranscrire le
chiffre “6” en capverdien, et ajoute des lettres en plus. Mais globalement, selon la personne,
la transcription est plutôt correcte.

### B) Outils pour l’écrit 

Il existe peu d’outils pour traiter le capverdien oral et il en est de même pour l'écrit.
Aussi, la plupart des modèles sont fine-tunés à partir du portugais, et ne sont pas conçus à
la base pour le capverdien. Nous n’avons pas trouvé de traducteurs automatiques connus
(comme Google Traduction) qui proposaient le créole capverdien. Il existe cependant le site
Glosbe.com, un outil collaboratif où les utilisateurs peuvent référencer leurs propres phrases
et traductions. Le capverdien reste peu doté puisqu’il comprend 712 phrases pour la

traduction portugais-capverdien et 240 pour le français-capverdien (la majorité sont des
traductions de la bible). Notons cependant que Glosbe propose Glosbe Translate pour la
traduction automatique qui utilise les technologies MarianNMT et NLLB. Malheureusement,
nous n’avons pas pu évaluer la pertinence de ces traductions par notre amie, locutrice
native du créole capverdien.

Concernant les outils d’OCR, nous avons pu tester Tesseract avec l’image 1 ci-dessous.

Image 1 : Affiche en créole du Cap-Vert https://en.wikipedia.org/wiki/Cape_Verdean_Creole

Nous avons toutes les deux lancé le script sur cette même photo et nous avons cependant
obtenu des sorties différentes. (voir table 2).

#### Résultat Maïwenn

Verão já começá e maltas tem k'sabê

kem ta livre pa começa ta dá pik. Pa

isso nada mdjor do que um festa de

SEMÁFORO Ne

E

Tertulia dia 12 julho

De 18:00 a 00:00

L 100$00 com uireito a caipirinha

#### Résultat Juliette

Verão já começá e maltas tem K'sabê

Kem ta livre pa começa ta dá pik. Pa

isso nada major do que um festa de.

SEMÁFORO

Delanoaseno

TOOSDD ces eras camas

Table 2 : Résultats obtenus pour la tâche d’OCR avec Tesseract, où les bonnes retranscriptions sont
surlignées en vert et les mauvaises en rouge.

On peut constater que l’OCR fonctionne dans une certaine mesure, mais les
résultats sont inconsistants et imprécis. Nous n’expliquons pas cette différence dans nos
résultats, d’autant plus que nous n’avons pas apporté de modifications au script.

## III - Le corpus

La principale difficulté à laquelle nous avons fait face était la constitution de notre
corpus. En effet, le capverdien et le portugais étant en situation de diglossie, lorsque nous
cherchions des ressources sur les réseaux sociaux par exemple, il était courant que les
locuteurs aient recours au code-switching et mélangent le capverdien et le portugais dans
leurs posts et/ou vidéos. Il était donc nécessaire de faire attention à ne bien récupérer que
des données en capverdien. Nous avions trouvé quelques vidéos TikTok transcrites et
contes pour enfants récités. Quant à l’écrit, il existe des pages Facebook, quelques poèmes
et des commentaires sous les vidéos TikTok. Au final, les ressources en capverdien que
nous avons trouvées cumulent deux problèmes : leur quantité (très faible) et leur qualité
(textes très courts). Bien que nous disposions d’une personne locutrice du capverdien pour
nous aider, elle n’était pas tout le temps disponible pour vérifier chaque contenu que nous
aurions aimé intégrer à notre corpus. Nous avons donc fait le choix de nous tourner vers des
corpus déjà constitués, plutôt que de créer le nôtre.

Nous avons trouvé sur HuggingFace deux corpus multilingues contenant du capverdien :

- https://huggingface.co/datasets/WueNLP/sib-fleurs/viewer/kea_Latn
Le corpus sib-fleurs, qui est un corpus oral comprenant des enregistrements audio
ainsi que leur transcription manuelle et automatique et leur traduction (avec
Whisper).

- https://huggingface.co/datasets/HuggingFaceFW/fineweb-2
Le corpus fineweb-2, environ 2900 lignes scrappées sur internet

Nous avons également trouvé le corpus parallèle portugais-capverdien du projet No Language Left Behind (évoqué dans la partie II.B).

- https://opus.nlpl.eu/legacy/NLLB-v1.php :
Le corpus multilingue parallèle, existe pour kea-en (1,2M de lignes) et kea-pt (0,3M
de lignes), réalisé par datamining automatique.

Finalement, nous avons choisi de travailler sur le corpus parallèle NLLB kea-pt car il
était le plus fourni. De plus, il livrait également les phrases alignées en portugais, ce qui
nous arrangeait pour la tâche du classifieur en termes d’équilibre des données. Cependant
nous émettons des doutes quant à la qualité des alignements. Certaines phrases ont l’air
très correctes (1), mais d’autres semblent totalement différentes (2).

(1) <tuv xml:lang="kea"><seg>Kal ki intenson di Deus pa tera?</seg></tuv>
<tuv xml:lang="pt"><seg>Qual é o propósito de Deus para a Terra?</seg></tuv>

(2) <tuv xml:lang="kea"><seg>Má Muizes fla: 'Ka nhos xinti medu.</seg></tuv>
<tuv xml:lang="pt"><seg>Só acho que não é o caso.</seg></tuv>

Dans le cas (2), cependant, nous pouvons confirmer que la phrase étiquetée “kea”
est bien du capverdien et la phrase étiquetée “pt” est bien du portugais. Cela ne pose donc
pas de problème pour notre tâche de classification, en revanche ça poserait un gros
problème pour une tâche de traduction automatique.
Nous avons cependant constaté des phrases mal étiquetées en termes de langues (3).

(3) <tuv xml:lang="kea"><seg>tu té pa perdu jespere xd</seg></tuv>
<tuv xml:lang="pt"><seg>Para a Liberdade, com o DJ Alpiste</seg></tuv>

On peut voir clairement que la phrase étiquetée comme étant du capverdien est du
français. Cela constitue du bruit assez gênant pour notre classifieur, mais le corpus étant
volumineux, nous ne savons pas quelle est la proportion de ces erreurs. Ce genre d’erreurs
nous prouve que le créole capverdien a du mal à être automatiquement reconnu et cela
justifie d’autant plus notre choix de développer un outil pour la détection de langue.

## IV - Notre contribution : la détection du capverdien à l’écrit

### A) Notre intention

Pour ce projet, nous avons décidé de réaliser un classifieur permettant de distinguer
le portugais du capverdien. Nous avons choisi cette tâche car le capverdien étant une
langue avec une orthographe non standardisée, et n’étant pas locutrices natives de cette
langue, il nous aurait été compliqué de réaliser un étiqueteur automatique morphosyntaxique
par exemple. Nous avons aussi choisi cette tâche car nous avons pu tester la
reconnaissance du capverdien à l’oral, qui a bien fonctionné comme nous l’avons mentionné
dans la partie II.A, mais nous ne savions pas dans quelle mesure un outil serait capable de
différencier correctement le portugais du capverdien. Un bon outil de détection de langue
serait alors utile pour le prétraitement d’un corpus multilingue contenant du portugais et du
capverdien, ce dont nous avons fait beaucoup affaire en cherchant à constituer notre propre
corpus puisque beaucoup de locuteurs du capverdien ont recours au code-switching même
à l’écrit.

### B) Développement de notre outil

Nous avons réalisé un classifieur à l’aide de la bibliothèque keras. Tout d’abord nous
avons réalisé un script permettant d’avoir une structure de données d’entrée utilisable par le
modèle. Ce script lit le fichier TMX grâce à la bibliothèque “translate.storage.tmx”, et permet
de récupérer facilement chaque paire de phrases avec leur code de langue respectives. Ce
script crée ensuite un DataFrame pandas avec deux colonnes : une colonne “lang”
comprenant le code iso de la phrase (kea ou pt donc), et une colonne “text” contenant la
phrase elle-même. Nous importons la fonction permettant de créer le DataFrame dans notre
script du classifieur. Cependant, les labels pour le modèle ont été changé de “kea” ou “pt” à
0 ou 1 avec LabelEncoder pour pouvoir utiliser une fonction de loss binaire. Ensuite nous
séparons les données en trois : un dataset train, validation et test. Nous avons opté pour
80% de train, 10% de validation et 10% de test. Ensuite, nous utilisons un Tokenizer pour
tokéniser les phrases et les transformer en suite d’entiers. Nous avons fixé le vocabulaire
maximum à 10000 termes et la longueur maximale des séquences à 50 tokens.
En ce qui concerne l’architecture du modèle, nous avons opté pour un RNN (réseau
de neurones récurrents) avec LSTM (long short-term memory). En entrée, nous avons donc
nos séquences de textes sous forme de séquences d’entier fixées à 50 tokens maximum.
Ensuite, nous avons une couche d’Embedding qui transforme les mots (représentés par des
entiers) en vecteurs de dimension 128 dans notre cas. La sortie de cette couche est ensuite
passée à la couche LSTM. Cette couche permet de mieux gérer les phrases longues, et
permet de garder l’ordre des mots et le contexte. La couche Dropout permet d’éviter
l’overfitting. Enfin nous avons notre couche dense de sortie, qui retourne une probabilité en
0 et 1. 1 correspond au portugais et 0 au capverdien. Le seuil de décision se situe à 0.5, ce
qui se situe donc en dessous sera classé comme du capverdien et ce qui se situe au-dessus
sera classé comme du portugais. Notre modèle repose sur une combinaison de couches
Embedding et LSTM qui permet de capturer à la fois les similarités lexicales et les
dépendances séquentielles (ordre des mots, contexte de la phrase) nécessaires à la
discrimination entre deux langues proches.
Voici le résumé de notre modèle :

### C) Résultats

Nous avons créé un script d’évaluation pour évaluer le modèle sur notre dataset de
test. Nous avons obtenu ces résultats de précision, rappel et f-mesure :

#### Capverdien :

précision : 0.98

rappel : 0.99

f-mesure : 0.99

#### Portugais

précision : 0.99

rappel :  0.98

f-mesure : 0.99

Ces résultats sont étonnamment très bons, malgré notre corpus de départ. On peut
constater que la précision est légèrement moins bonne pour le capverdien, ce qui signifie
que le modèle va avoir tendance à prendre du portugais pour du capverdien. A l’inverse, on
a donc un moins bon rappel pour le portugais.
Nous avons obtenu cette matrice de confusion :
On peut constater que notre modèle a prédit 45 phrases comme étant du portugais
qui étaient en réalité du capverdien, et 78 phrases comme étant du capverdien qui étaient
en réalité du portugais. Le modèle a donc étonnement tendance à classer “plus facilement”
une phrase en capverdien qu’en portugais. Voici des exemples d’erreur :

#### 1) 21o Eslovênia

langue réelle : pt

langue prédite : kea

#### 2) 38 รีวว ิ Meson de Deus

langue réelle : kea

langue prédite : pt

#### 3) balgen kiejtése kea balgen [de]

langue réelle : kea

langue prédite : pt

#### 4) Nefropatia diabética Barbalha CE

langue réelle : pt

langue prédite : kea

#### 5) auspiciosas ou enfrentando

langue réelle : pt

langue prédite : kea

#### 6) Ácidos voláteis

langue réelle : pt

langue prédite : kea
 
#### 7) Paraíso - Luiz Gê

langue réelle : kea 

langue prédite : pt
 
#### 8) Sssss Natasha

langue réelle : pt
  
langue prédite : kea
 
#### 9) Hospedagem Node.js

langue réelle : pt

langue prédite : kea

#### 10)(Secundário)

langue réelle : pt

langue prédite : kea

On peut voir que dans ces phrases il y a énormément de bruit. Il y a de la
ponctuation, des chiffres, même des lettres dans un autre alphabet. La troisième phrase
n’est ni du portugais ni du capverdien. La huitième phrase comprend du bruit et un nom
propre. Les phrases 4, 5, 6, 10 sont en portugais mais ont été classées en capverdien. On a
donc quelques erreurs dûes à la nature même de la phrase, qui est bruitée, ou trop courte,
ou dans une autre langue, ainsi que quelques réelles erreurs de classification.
Enfin, nous avons créé un petit script constituant une ébauche d’outil utilisant notre
modèle pour pouvoir prédire d’autres phrases données en entrée. La fonction s’appelle
“predict_language” et prend en entrée une phrase. La fonction retourne alors la langue
prédite par le modèle. Nous avons testé avec des phrases où nous étions sûres de la
langue. Par exemple, en donnant en entrée “N ta gosta di bo” qui est du capverdien et "Eu
gosto de você" qui est la même phrase en portugais (qui signifie “Je t’aime bien/Je
t’apprécie”) notre modèle prédit correctement la première phrase comme étant du
capverdien et la deuxième phrase comme étant du portugais. De plus, le modèle est très sûr
de lui. Voici les probabilités :
'kea', 7.468025e-05 pour la première phrase.
'pt', 0.9999348 pour la deuxième phrase.

Pour le capverdien, on est donc extrêmement proche de 0 : 0 représentant la classe
“parfaite” capverdien, et pour le portugais on est au contraire très proche de 1. Cela peut
montrer que malgré le bruit pouvant être présent dans notre corpus de départ, le modèle
arrive tout de même à généraliser et à très bien reconnaître le capverdien du portugais avec
des phrases bien orthographiées et sans bruit.

## Conclusion

Le créole capverdien peut largement être considéré comme une langue peu dotée au
vu de sa “rareté numérique”. Les corpus sur lesquels travailler sont peu nombreux et leur
qualité est discutable. Cela s’explique notamment par le manque d’investissements humains
et financiers que subissent les pays anciennement colonisés. Dans le cas des créoles, la
plupart des outils existants pour traiter ces langues sont avant tout pensés pour la langue
dominante, puis adaptés aux créoles.

C’est le cas du capverdien, dont les outils sont souvent dérivés de ceux du portugais.
Or, cette méthode n’est pas toujours efficace et révèle le besoin des langues minoritaires de
disposer d’outils de TAL pensés pour elles. Nous en avons eu la preuve avec les tests
d’OCR et d’ASR que nous avons effectués. Ce manque est aussi flagrant lorsqu’on examine
les corpus, notamment le corpus NLLB, qui contient des phrases françaises en langage
SMS. Il a été réalisé par datamining automatique, en s’appuyant entre autres sur des
techniques de détection de langue pour les langues moins dotées. Si l’outil de détection de
langue n’est pas précis, on se retrouve alors avec des corpus avec des erreurs comme le
corpus NLLB, où on retrouve des phrases étiquetées comme étant d’une langue incorrecte,
ce qui rend alors extrêmement difficile l’entraînement de modèles. Cette étape de détection
est donc non négligeable et a motivé notre choix de développer un outil spécifique pour
distinguer le portugais du capverdien. Nous pouvons rajouter qu’il est important de
constituer un corpus de bonne qualité, récolté manuellement, afin d’avoir un bon outil de
détection de langue qui permettra alors de récolter avec précision et automatiquement un
corpus plus volumineux pour entraîner des modèles plus lourds.

Notre outil de reconnaissance de la langue capverdienne fonctionne donc
relativement bien malgré la qualité discutable du corpus NLLB. Nous avons obtenu de très
bonnes f-mesure, et notre outil utilisant notre modèle fonctionne avec des données réelles.
Cependant, il est difficile de savoir dans quelle mesure notre modèle a des résultats significatifs étant donné notre corpus. Il faudrait idéalement nettoyer une partie du corpus
NLLB afin de constituer un gold standard sur lequel on pourrait réentraîner notre modèle, et
ainsi voir si nous obtenons toujours d’aussi bons résultats.

## Références

Notre Dépôt GiHub :
https://github.com/juliettehnr/Ecriture-multilingue-capverdien

Projet ORAL :
https://www.iscte-iul.pt/news/2820/iscte-launches-international-project-the-development-of-language-models-in-cape-verdean-creole#

Dataset NLLB :
https://opus.nlpl.eu/NLLB/corpus/version/NLLB

Holger Schwenk, Guillaume Wenzek, Sergey Edunov, Edouard Grave, Armand Joulin, and
Angela Fan. 2021. CCMatrix: Mining Billions of High-Quality Parallel Sentences on the Web.
In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics
and the 11th International Joint Conference on Natural Language Processing (Volume 1:
Long Papers), pages 6490–6500, Online. Association for Computational Linguistics.

Angela Fan, Shruti Bhosale, Holger Schwenk, Zhiyi Ma, Ahmed El-Kishky, Siddharth Goyal,
Mandeep Baines, Onur Celebi, Guillaume Wenzek, Vishrav Chaudhary, Naman Goyal, Tom
Birch, Vitaliy Liptchinsky, Sergey Edunov, Edouard Grave, Michael Auli, and Armand Joulin.
2021. Beyond english-centric multilingual machine translation. J. Mach. Learn. Res. 22, 1,
Article 107 (January 2021), 48 pages.

team, NLLB & Costa-jussa, Marta & Cross, James & Çelebi, Onur & Elbayad, Maha &
Heafield, Kenneth & Heffernan, Kevin & Kalbassi, Elahe & Licht, Daniel & Maillard, Jean &
Sun, Anna & Wang, Skyler & Wenzek, Guillaume & Youngblood, Al & Akula, Bapi & Barrault,
Loïc & Gonzalez, Gabriel & Hansanti, Prangthip & Wang, Jeff. (2022). No Language Left
Behind: Scaling Human-Centered Machine Translation. 10.48550/arXiv.2207.04672.

Jörg Tiedemann. 2012. Parallel Data, Tools and Interfaces in OPUS. In Proceedings of the
Eighth International Conference on Language Resources and Evaluation (LREC'12), pages
2214–2218, Istanbul, Turkey. European Language Resources Association (ELRA).
