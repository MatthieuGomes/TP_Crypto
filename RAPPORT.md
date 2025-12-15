# TP Crypto

## Exercice 1

### Question 1.1

Les hashs générés sont tous très différents à la moindre variation, que ce soit pour MD5 ou SHA-1. On constate également que les hashs produits par SHA-1 sont plus longs que ceux produits par MD5.



### Question 1.2

La taille du hash obtenu ne change pas quel que soit la taille du texte, il s'agit donc d'une compression

### Question 1.3

La moindre modification des paramètres d'entrés entraîne une réaction "avalanche" sur le reste du hash et en fait un complètement différent.

### Question 1.4

MD5 et SHA-1 ne sont plus sûr car il existe des attaques par collisions réussies sur ces messages

il est conseillé d'utiliser SHA-256

### Question 1.5

Une fonction de hachage salée ajoute une valeur aléatoire ou semi aléatoire (le sel) avant le hachage du mot de passe. Cela permet d'éviter les attaques par tables arc-en-ciel et rend plus difficile la découverte des mots de passe par force brute.



## Exercice 3

### Question 3.1
Avec un IC de 0.45, on peut estimer que le texte est chiffré avec un chiffre de Vigenère.

### Question 3.2
La clé la plus probable est de taille 7, avec un ic de 0.073

### Question 3.3
La clé la plus probable est "ENSEAIS"

### Question 3.4
Le texte déchiffré est :

FELICITATIONSPOURAVOIRTROUVELACLEDECHIFFREMENTVOUSAVEZREUSSICETEXERCICEDECRYPTOGRAPHIEFELICITATIONSENCOREUNEFOISPOURVOTRETRAVAILREMARQUABLEVOUSAVEZFAITPREUVEDEPERSEVERANCEETDELOGIQUEPOURDECODERCEMESSAGESECRETBRAVOPOURVOTREDETERMINATIONLACRYPTOGRAPHIEESTUNARTANCIENQUIREMONTEALANTIQUITEFELICITATIONSVOUSMAITRISEZMAINTENANTLESBASESDUCHIFFREMENTDEVIGENERECESYSTEMEAETEINVENTEAUSEIZIEMESIECLEBRAVOPOURAVOIRPERCECEMYSTERELACRYPTANALYSEDEMANDEDELAPATIENCEFELICITATIONSVOUSAVEZLESCOMPETENCESNECESSAIRESPOURCONTINUERDANSCETTEVOIEBRAVOENCORE

### Question 3.5
Car le chiffre de Vigenère n'est pas un chiffrage aléatoire et l'indice de coincidence permet de mettre en évidence les correspondance de fréquences

### Question 3.6

### Question 3.7

### Question 3.8

Comme son nom l'indique une cle one time pad est à utilisation unique, sinon il devient possible de déchiffrer le messsage 

### Question 3.9
Non la clé est à usage unique


