# Chiffre de Vigenère


le but de cette activité est d'écrire un programme pour chiffrer et déchiffrer des messages en utilisant le chiffrement de Vigenère. Cette activité se construit sur la précédente autour des chaines de caractères et du chiffre de césar.

## Principe du chiffre de Vigenère

Commençons par expliquer le principe du chiffre de Vigenère. Comme pour le chiffre de César, le principe va être d'effectuer un décalage des lettres mais ce décalage ne sera pas le même selon la position de la lettre dans le message original, il va en dépendre périodiquement selon un motif que l'on appelle la clé.

Prenons un exemple, admettons que l'on veuille chiffrer le message `'monmessagesecret'`, on choisit la clé `[1,4,3]`. Cela signifie qu'on va effectuer des décalages de 1,4,3,1,4,3,1,4,3, etc. Ainsi la première lettre `m` est décalée de 1, ce qui donne `n`, la seconde lettre `o` est décalée de 4, ce qui donne `s`, la troisième lettre `n` est décalée de 3, ce qui donne `q`, la quatrième `m` est à nouveau décalée de 1, ce qui donne `n` et ainsi de suite. Le message chiffré est au final `'nsqnivtejfwhdvhu'`, on peut visualiser cela dans le tableau suivant.


|message original|m|o|n|m|e|s|s|a|g|e|s|e|c|r|e|t|
|décalage        |1|4|3|1|4|3|1|4|3|1|4|3|1|4|3|1|
|message chiffré |n|s|q|n|i|v|t|e|j|f|w|h|d|v|h|u|


### Question 1

*Niveau 1 :* Commençons par programmer la fonction de chiffrage des messages (c'est l'opération que l'on effectue lorsque l'on veut envoyer un message). Programmer une fonction `vigenere(message, cle)` qui prend en arguments le message original (une chaine de caractères) et la clé (une liste d'entiers) et retourne le message chiffré par la chiffre de Vigenère.


### Question 2

*Niveau 1 :* Sur le même principe, on veut désormais effectuer l'opération inverse de déchiffrage (c'est l'opération que l'on effectue lorsque l'on veut lire un message chiffré que l'on reçoit). Programmer une fonction `dechiffre_vigenere(message, cle)` qui prend en arguments le message chiffré (une chaine de caractère) et la clé (une liste d'entiers) et retourne le message déchiffré.

## Cryptanalyse du chiffre de Vigenère

Une fois que l'on a programmé notre fonction de chiffrage et déchiffrage, nous possédons un moyen d'échanger des communications chiffrées entre deux personnes. Pour cela, il suffit de se mettre d'accord au préalable sur une clé secrète, et chacun peut envoyer une recevoir des messages en utilisant les fonctions `vigenere(message, cle)` et `dechiffre_vigenere(message, cle)`. Mais on peut se demander si ce protocole de communication est bien sécurisé. Supposons qu'une personne qui ne connaisse pas la clé secrète intercepte le message chiffré. Peut-elle deviner le message original ?

La question qui se pose donc est de déchiffrer un message chiffré dont on ne connait pas la clé. Il suffirait de deviner la clé pour y arriver.

## Anaylse de fréquence


Admettons dans un premier temps que l'on connaisse la longueur de la clé. Nous avions vu que pour le chiffre de César, il était possible de deviner la clé (le décalage) de plusieurs moyens : essais par force brute, analyse de fréquences.


### Question 3

*Niveau 2 :* Programmer une fonction `frequence(texte)` qui prend en argument une chaine de caractères et retourne un dictionnaire contenant le nombre de fois que chaque caractère apparait dans la chaine de caractère. Par exemple dans la chaine `'bienvenue'`, le caractère `'b'` apparait 1 fois, le caractère `'i'` apparait 1 fois, le caractère `'e'` apparait 3 fois, le caractère `'n'` apparait 2 fois, le caractère `'n'` apparait 2 fois, le caractère `'v'` apparait 1 fois, et le caractère `'u'` apparait 1 fois. La fonction `frequence('bienvenue')` devrait donc répondre le dictionnaire

`{'b' : 1, 'i' : 1, 'e' : 3, 'n' : 2, 'v' : 1, 'u' : 1}`

### Question 4

*Niveau 2 :* En utilisant la fonction `frequence`, programmer une fonction `caractere_plus_frequent(texte)` qui prend en argument une chaine de caractere retourne le caractère qui apparaît le plus de fois dans la chaîne de caractère. Par exemple, le caractère le plus fréquent dans la chaîne `'anticonstitutionnellement'` est le `'n'` (qui apparaît 5 fois dans la chaine).

### Question 5

*Niveau 2 :* En utilisant la fonction `caractere_plus_frequent`, programmer une fonction `deviner_cle_cesar(message)` qui prend en argument un message chiffré avec un code de César (une chaine de caractere) et retourne une clé probable pour le message (un entier) déterminée par analyse de fréquence.

### Question 6

*Niveau 3 :* Programmer une fonction `deviner_cle_vigenere(message, longueur)` qui prend en arguments le message chiffré (une chaine de caractère) et une longueur possible de clé (un entier) et retourne la clé la plus probable en utilisant une analyse de fréquence (liste d'entier).