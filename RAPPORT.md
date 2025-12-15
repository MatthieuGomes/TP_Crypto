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


## Exercice 2   

### Question 2.1

* Emetteur : Google Trust Services
* Sujet : google.com
* Période de validité : du 24 novembre 2025 au 16 février 2026
* Clé publique : 
* Algorithme : eliptic curve 
* Algorithme de signature : SHA256 avec RSA Encryption
* Fingerprint :
    * SHA-1 :
    * SHA-256 : 

### Question 2.2

### Question 2.3

### Question 2.4 

### Question 2.5

### Question 2.6





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


## Exercice 4

### Question 4.1

les élements principaux d'un bloc bitcoin sont :
- le hash
- le nonce
- la racine de merkle
- le timestamp
- la version
- le hash du bloc précédent
- la difficulté
- les transactions

### Question 4.2

La taille moyenne d'un bloc bitcoin est d'environ 1 à 2 Mo, avec une limite maximale de 4 Mo pour les blocs SegWit.

### Question 4.3

En moyenne, un bloc contient environ 3000 à 4 000 transactions, mais ce nombre peut varier en fonction de la taille des transactions individuelles.


### Question 4.4

le block header est composé de plusieurs champs :
- version (4 bytes)
- hash du bloc précédent (32 bytes)
- racine de Merkle (32 bytes)
- timestamp (4 bytes)
- la cible de difficulté (4 bytes)
- nonce (4 bytes)

### Question 4.5

le previous block hash est le hash du bloc précédent dans la chaîne de blocs. Il permet de lier les blocs entre eux, assurant ainsi l'intégrité et la continuité de la blockchain.

### Question 4.6

Le champs nonce est un nombre arbitraire qui est utilisé une seule fois dans le processus de minage. Les mineurs modifient ce nombre pour trouver un hash de bloc qui satisfait les conditions de difficulté du réseau. c'est grossièrement la seed qui permet de générer différents hash.

### Question 4.7

Les étapes pour miner un bloc bitcoin sont les suivantes :
1. Rassembler les transactions en attente dans un bloc candidat.
2. Calculer la racine de Merkle des transactions.
3. Construire le block header avec les informations nécessaires.
4. Modifier le nonce et recalculer le hash du block header jusqu'à ce que le hash satisfasse les conditions de difficulté.
5. Une fois un hash valide trouvé, le bloc est diffusé au réseau pour validation et ajout à la blockchain.

### Question 4.8

Le minage d'un bloc bitcoin consiste à trouver un hash de bloc. En trouvant ce dernier, on assure la sécurité et l'intégrité de la blockchain, tout en validant les transactions contenues dans le bloc. Le minage est en fait la preuve de travail qui empêche les attaques et garantit que les mineurs investissent des ressources pour maintenir le réseau et cloture un bloc et donc de valider les transactions.

### Question 4.9

La difficulté de minage est ajustée toutes les 2016 blocs, soit environ toutes les deux semaines. L'objectif est de maintenir un temps moyen de 10 minutes entre la création de chaque bloc. Si les blocs sont minés plus rapidement que prévu, la difficulté augmente, et si ils sont minés plus lentement, la difficulté diminue.

### Question 4.10

Le hash d'un block doit contenir 19 zeros initiaux pour être considéré comme valide à l'heure actuelle.


### Question 4.11

50 BTC

## Question 4.12


Le bloc genesis est le premier bloc de la blockchain Bitcoin. Il a été créé par Satoshi Nakamoto le 3 janvier 2009 et marque le début de l'histoire de Bitcoin. Ce bloc est unique car il n'a pas de bloc précédent et contient un message spécial dans son coinbase.

### Question 4.13

"EThe Times 03/Jan/2009 Chancellor on brink of second bailout for banks" est le message inclus dans le bloc genesis de Bitcoin par Satoshi Nakamoto. Ce message fait référence à un article du journal The Times publié le 3 janvier 2009, qui évoque la situation économique et les mesures de sauvetage des banques.

### Question 4.14

Au bloc 210 000, la récompense de minage est de 25 bitcoins, alors qu'elle était de 50 bitcoins au bloc 209999 : c'est le premier halving de l'histoire de Bitcoin.

### Question 4.15

25 btc.

### Question 4.16

Le halving a lieu tous les 210 000 blocs.


### Question 4.17

tous les 4 ans

### Question 4.18

4 

### Question 4.19

3,125 BTC

### Question 4.20

~ 2100

### Question 4.21

21 millions de bitcoins

### Question 4.22

~ 15 mins

### Question 4.23

il ajuste la difficulté de minage pour maintenir un temps moyen de 10 minutes entre la création de chaque bloc. En s'adaptant aux variations de la puissance de calcul du réseau, il assure la stabilité et la sécurité de la blockchain Bitcoin.

### Question 4.24

tous les 2016 blocs

### Question 4.25

les blocs sont minés plus rapidement que prévu, la difficulté augmente au bout de 2016 blocs?

### Question 4.26

par 16 car nous sommes en exadecimale

### Question 4.27

il faut attendre plusieurs confirmations pour s'assurer que la transaction est bien enregistrée dans la blockchain et qu'elle n'est pas sujette à des modifications ou des annulations. Chaque confirmation correspond à l'ajout d'un nouveau bloc contenant la transaction, renforçant ainsi sa sécurité et son immutabilité. En général, plus une transaction a de confirmations, plus elle est considérée comme sûre.

### Question 4.28

au moins 6 confirmations sont recommandées pour les transactions importantes en bitcoin afin de garantir leur sécurité et leur immutabilité dans la blockchain.

### Question 4.29

Si un attaquant contrôle plus de 50 % de la puissance de calcul du réseau Bitcoin, il pourrait potentiellement mener une attaque de type "51 %". Cela lui permettrait de réorganiser la blockchain, d'annuler des transactions récentes et de dépenser deux fois les mêmes bitcoins (double spending). Cependant, une telle attaque serait extrêmement coûteuse et difficile à réaliser en raison de la taille et de la décentralisation du réseau Bitcoin.

### Question 4.30

 SHA-256

### Question 4.32

65*16=1040 bits

### Question 4.33

Ils commencent tous par 0000000000

### Question 4.34

la preuve de travail (Proof of Work) est un mécanisme de consensus utilisé dans les réseaux blockchain, comme Bitcoin, pour sécuriser le réseau et valider les transactions. Elle nécessite que les mineurs résolvent des problèmes mathématiques complexes en utilisant une puissance de calcul significative. Cette preuve de travail garantit que les mineurs investissent des ressources pour ajouter de nouveaux blocs à la blockchain, rendant ainsi les attaques coûteuses et difficiles à réaliser.

### Question 4.35

La condition mathématique pour qu'un hash de bloc soit valide dans le réseau Bitcoin est que le hash doit être inférieur à une certaine cible de difficulté.


### Question 4.36

