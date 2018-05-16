# Chiffre de Vigenère


le but de cette activité est d'écrire un programme pour chiffrer et déchiffrer des messages en utilisant le chiffrement de Vigenère. Cette activité se construit sur la précédente autour des chaines de caractères et du chiffre de césar.

## le principe du chiffre de Vigenère

Commençons par expliquer le principe du chiffre de Vigenère. Comme pour le chiffre de César, le principe va être d'effectuer un décalage des lettres mais ce décalage ne sera pas le même selon la position de la lettre dans le message original, il va en dépendre périodiquement selon un motif que l'on appelle la clé.

Prenons un exemple, admettons que l'on veuille chiffrer le message `'monmessagesecret'`, on choisit la clé `[1,4,3]`. Cela signifie qu'on va effectuer des décalages de 1,4,3,1,4,3,1,4,3, etc. Ainsi la première lettre `m` est décalé de 1, ce qui donne `n`, la seconde lettre `o` est décalée de 4, ce qui donne `s`, la troisième lettre est décalée de 3, ce qui donne `q`, la quatrième est à nouveau décalée de 1, ce qui donne `n` et ainsi de suite. Le message chiffré est au final `'nsqnivtejfwhdvhu'`, on peut visualiser cela dans le tableau suivant.


|message original|m|o|n|m|e|s|s|a|g|e|s|e|c|r|e|t|
|----------------|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|décalage        |1|4|3|1|4|3|1|4|3|1|4|3|1|4|3|1|
|message chiffré |n|s|q|n|i|v|t|e|j|f|w|h|d|v|h|u|


### Question 1

*Niveau 1 :* Commençons par programmer la fonction de chiffrage des messages (c'est l'opération que l'on effectue lorsque l'on veut envoyer un message). Programmer une fonction vigenere(message, cle) qui prend en arguments le message original (une chaine de caractères) et la clé (une liste d'entiers) et retourne le message chiffré par la chiffre de Vigenère.


### Question 2

*Niveau 1 :* Sur le même principe, on veut désormais effectuer l'opération inverse de déchiffrage (c'est l'opération que l'on effectue lorsque l'on veut lire un message chiffré que l'on reçoit). Programmer une fonction dechiffre_vigenere(message, cle) qui prend en arguments le message chiffré (une chaine de caractère) et la clé (une liste d'entiers) et retourne le message déchiffré.