# Chiffre de Vigenère


Le but de cette activité est d'écrire un programme pour chiffrer et déchiffrer des messages en utilisant le chiffrement de Vigenère. Cette activité se construit sur la précédente autour des chaines de caractères et du chiffre de césar.

## Principe du chiffre de Vigenère

Commençons par expliquer le principe du chiffre de Vigenère. Comme pour le chiffre de César, le principe va être d'effectuer un décalage des lettres mais ce décalage ne sera pas le même selon la position de la lettre dans le message original, il va en dépendre périodiquement selon un motif que l'on appelle la clé.

Prenons un exemple, admettons que l'on veuille chiffrer le message `'monmessagesecret'`, on choisit la clé `[1,4,3]`. Cela signifie qu'on va effectuer des décalages de 1,4,3,1,4,3,1,4,3, etc. Ainsi la première lettre `m` est décalée de 1, ce qui donne `n`, la seconde lettre `o` est décalée de 4, ce qui donne `s`, la troisième lettre `n` est décalée de 3, ce qui donne `q`, la quatrième `m` est à nouveau décalée de 1, ce qui donne `n` et ainsi de suite. Le message chiffré est au final `'nsqnivtejfwhdvhu'`, on peut visualiser cela dans le tableau suivant :


| message original | m | o | n | m | e | s | s | a | g | e | s | e | c | r | e | t |
| -----------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| décalage         | 1 | 4 | 3 | 1 | 4 | 3 | 1 | 4 | 3 | 1 | 4 | 3 | 1 | 4 | 3 | 1 |
| message chiffré  | n | s | q | n | i | v | t | e | j | f | w | h | d | v | h | u |



### Question 1

*Niveau 1 :* Commençons par programmer la fonction de chiffrage des messages (c'est l'opération que l'on effectue lorsque l'on veut envoyer un message). Programmer une fonction `vigenere(message, cle)` qui prend en arguments le message original (une chaine de caractères) et la clé (une liste d'entiers) et retourne le message chiffré par la chiffre de Vigenère.


### Question 2

*Niveau 1 :* Sur le même principe, on veut désormais effectuer l'opération inverse de déchiffrage (c'est l'opération que l'on effectue lorsque l'on veut lire un message chiffré que l'on reçoit). Programmer une fonction `dechiffre_vigenere(message, cle)` qui prend en arguments le message chiffré (une chaine de caractère) et la clé (une liste d'entiers) et retourne le message déchiffré.

## Cryptanalyse du chiffre de Vigenère

Une fois que l'on a programmé notre fonction de chiffrage et déchiffrage, nous possédons un moyen d'échanger des communications chiffrées entre deux personnes. Pour cela, il suffit de se mettre d'accord au préalable sur une clé secrète, et chacun peut envoyer une recevoir des messages en utilisant les fonctions `vigenere(message, cle)` et `dechiffre_vigenere(message, cle)`. Mais on peut se demander si ce protocole de communication est bien sécurisé. Supposons qu'une personne qui ne connaisse pas la clé secrète intercepte le message chiffré. Peut-elle deviner le message original ?

La question qui se pose donc est de déchiffrer un message chiffré dont on ne connait pas la clé. Il suffirait de deviner la clé pour y arriver, ce qui est souvent possible en pratique. Procédons par étape pour s'en apperçevoir.

## Analyse de fréquence


Admettons dans un premier temps que l'on connaisse la longueur de la clé. Nous avions vu que pour le chiffre de César, il était possible de deviner la clé (le décalage) de plusieurs moyens : essais par force brute, analyse de fréquences. Le chiffre de Vigenère possède la même faiblesse : dès lors qu'on connaît la longueur de la clé, il ne reste plus qu'à faire des analyses de fréquences sur chacune des portions de message qui ont été chiffrées avec le même décalage.

### Dictionnaire en Python

Pour aborder les analyses de fréquences, il peut être utile de faire quelques rappels sur une structure de données en Python qui s'appelle un dictionnaire (*dictionnary* en anglais). Un dictionnaire (aussi parfois appelée tableau associatif) est une structure de donnée similaire à un tableau de valeurs, mais dans lequel les indices ne sont pas pas nécessairement des entiers consécutifs (ils peuvent par exemple être des chaines de caractères). Les indices sont appelées des clés (*key* en anglais). On peut définir un dictionnaire entre accolades.

```python
mon_dictionnaire = {"chat" : "cat", "chien" : "dog", "oiseau" : "bird",  "poisson" : "fish"}
```

#### Lire, modifier, ajouter une valeur

On peut lire, modifier ou ajouter une valeur du dictionnaire en utilisant une syntaxe similaire à celle pour un tableau


```python
mon_dictionnaire["chat"] = "cat" # modifier une valeur
mon_dictionnaire["ornithorynque"] = "platypus"
print(mon_dictionnaire)
```

#### Parcourir un dictionnaire

Pour parcourir un dictionnaire, on peut utiliser une boucle for avec la syntaxe suivante

```python
for cle in mon_dictionnaire:
    print("la traduction en anglais de " + cle + " est " + mon_dictionnaire[cle])
```

#### La condition `in`

Pour vérifier si un élément fait partie des **clés** du dictionnaire, il suffit d'utiliser la condition `in`, le résultat de l'expression est `True` ou `False`.

```python
print("papillon" in mon_dictionnaire) # False
print("chien" in mon_dictionnaire) # True
```
### Question 3

*Niveau 2 :* Programmer une fonction `frequence(texte)` qui prend en argument une chaine de caractères et retourne un dictionnaire contenant le nombre de fois que chaque caractère apparait dans la chaine de caractère. Par exemple dans la chaine `'bienvenue'`, le caractère `'b'` apparait 1 fois, le caractère `'i'` apparait 1 fois, le caractère `'e'` apparait 3 fois, le caractère `'n'` apparait 2 fois, le caractère `'n'` apparait 2 fois, le caractère `'v'` apparait 1 fois, et le caractère `'u'` apparait 1 fois. La fonction `frequence('bienvenue')` devrait donc répondre le dictionnaire

`{'b' : 1, 'i' : 1, 'e' : 3, 'n' : 2, 'v' : 1, 'u' : 1}`

### Question 4

*Niveau 2 :* En utilisant la fonction `frequence`, programmer une fonction `caractere_plus_frequent(texte)` qui prend en argument une chaine de caractere retourne le caractère qui apparaît le plus de fois dans la chaîne de caractère. Par exemple, le caractère le plus fréquent dans la chaîne `'anticonstitutionnellement'` est le `'n'` (qui apparaît 5 fois dans la chaine).

### Question 5

*Niveau 2 :* En utilisant la fonction `caractere_plus_frequent`, programmer une fonction `deviner_cle_cesar(message)` qui prend en argument un message chiffré avec un code de César (une chaine de caractere) et retourne une clé probable pour le message (un entier) déterminée par analyse de fréquence.

### Question 6

*Niveau 3 :* Programmer une fonction `deviner_cle_vigenere(message, longueur)` qui prend en arguments le message chiffré (une chaine de caractère) et une longueur possible de clé (un entier) et retourne la clé la plus probable en utilisant une analyse de fréquence (liste d'entier).

## Deviner la longueur de la clé

*Niveau 4* : Il s'agit là de la partie la plus délicate et soumise à la chance mais il est bien souvent possible de deviner la longeur de la clé, pourvue que celle-ci soit assez courte et que le message soit assez long. L'idée repose sur le fait de chercher des séquence de symboles qui se répètent dans le message chiffré. Pourrez-vous déchiffrer le message suivants ?

```python
message_secret = '#Pk#gnljlui&gi&Ymmhrîui&hwz#yt#w\x7fvxîpi&gi&floijxhqkqx&ssr|erslgeízlu{h0&f”kvx&xr&floijxhqkqx&sex#w{ewzlx{wmuq0&peov${qi&pîsh$rhxzui&gy&piyvemh$ioeou$vhyz/$yxm|drz#wg#tuvmzlst#hgqw&firxm3fm2#îzui&uisspgfík#tgu$jhw&oizwvkv$jljlìvkqxkv0&fstwvglvkpitw$æ#yt#w\x7fvxîpi&gi&floijxhqkqx&pstrerslgeízlu{h$irqsh$rh$ikmlivk#hk#Gïvex#,wx+oo${wmrlwk#gksitgetw$irqsh$irqvrwgqx/1$Ihxzh$sìxnrhk#vïvmywi&dmtvm&ã$r*etdp\x7fvi&gi&ivïtykqgkv0&fi&tyo#iyw${q$gyetwemh$jìgovml#w{u$rhw&floijxhqkqxy#quqsgotndfïwmwxiy1$Ihtkqhgqx&oi&floijxh$jh$\\lkkqìxh$g#ízì$vhviì$vdv&oi&peprv&sv{vwohr&Ivohhxlgn#Ogvmynm&tyo#e&syhomï#wg#qïwlugi&hr&4<<62&Lp&q“uijxh$voyy#hksyov$ihxzh$ïsswxi&dyixrk#wïfyxlxï1\x0e\x10Lp&hwz#rupqï#eoqwo#e{#|o{i&vmîfpk#it#vïiíxhrih$gx$jltrrqgwi&gy&{zoh$ylìioi&Epglwk#hk#Zojitëvk/$wxm&oi&gíiumz#,oqxïjvï#ä&xr&floijxhqkqx&sp{v$irqvoi~h-&getv$yrr&wvglxï#hkv$ikmlivkv$vdv{#it#5;;:4#St#xxry|h$kq$ldmz#hïmä&xrk#qïwlugi&gi&floijxhqkqx&drgosmxi&getv${q$iryxw$zueowí&gi&Jmuyet#Fgwxovxg#Fkopgvs&sexx$kq$78791'
```
