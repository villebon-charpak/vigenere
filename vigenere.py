#!/usr/bin/env python
# encoding : utf-8


# le but de cette activité est d'écrire un programme pour chiffrer et déchiffrer des messages en utilisant le chiffrement de Vigenère. Reportez-vous au fichier readme pour plus d'explications.

#####
# 1 #
#####

# Niveau 1 : Commençons par programmer la fonction de chiffrage des messages (c'est l'opération que l'on effectue lorsque l'on veut envoyer un message). Programmer une fonction vigenere(message, cle) qui prend en arguments le message original (une chaine de caractères) et la clé (une liste d'entiers) et retourne le message chiffré par la chiffre de Vigenère.


def vigenere(message, cle):
    # arguments :
    #       message : chaine de caractère contenant le message à chiffrer
    #       cle : liste d'entiers correspondant à la liste des décalages à effectuer
    # la fonction retourne une chaine de caractère qui correspond au message chiffré en utilisant le cle passée en argument
    
    pass # remplacer cette ligne par votre code

# test (décommenter pour tester)
# assert vigenere("monmessagesecret", [1,4,3]) == "nsqnivtejfwhdvhu"
    

#####
# 2 #
#####

# Niveau 1 : Sur le même principe, on veut désormais effectuer l'opération inverse de déchiffrage (c'est l'opération que l'on effectue lorsque l'on veut lire un message chiffré que l'on reçoit). Programmer une fonction dechiffre_vigenere(message, cle) qui prend en arguments le message chiffré (une chaine de caractère) et la clé (une liste d'entiers) et retourne le message déchiffré.


def dechiffre_vigenere(message, cle):
    # arguments :
    #       secret : chaine de caractère contenant le message chiffré
    #       cle : liste d'entiers correspondant à la liste des décalages qui ont été effectués pour chiffrer
    # la fonction retourne une chaine de caractère qui correspond au message original
    
    pass # remplacer cette ligne par votre code

# test (décommenter pour tester)
# assert vigenere("nsqnivtejfwhdvhu", [1,4,3]) == "monmessagesecret"

    
################
# Cryptanalyse #
################

# La question que l'on peut désormais se poser est de déchiffrer un message chiffré dont on ne connait pas la clé.


#####
# 3 #
#####

# Niveau 2 : Programmer une fonction frequence(texte) qui prend en argument une chaine de caractères et retourne un dictionnaire contenant le nombre de fois que chaque caractère apparait dans la chaine de caractère. Par exemple dans la chaine 'bienvenue', le caractère 'b' apparait 1 fois, le caractère 'i' apparait 1 fois, le caractère 'e' apparait 3 fois, le caractère 'n' apparait 2 fois, le caractère 'n' apparait 2 fois, le caractère 'v' apparait 1 fois, et le caractère 'u' apparait 1 fois. La fonction frequence('bienvenue') devrait donc repondre le dictionnaire

def frequence(texte):
    pass

# test (décommenter pour tester)
# assert frequence("bienvenue") == {'b' : 1, 'i' : 1, 'e' : 3, 'n' : 2, 'v' : 1, 'u' : 1}


#####
# 4 #
#####

# Niveau 2 : En utilisant la fonction frequence, programmer une fonction caractere_plus_frequent(texte) qui prend en argument une chaine de caractere retourne le caractère qui apparaît le plus de fois dans la chaîne de caractère. Par exemple, le caractère le plus fréquent dans la chaîne 'anticonstitutionnellement' est le 'n' (qui apparaît 5 fois dans la chaine).


def caractere_plus_frequent(texte):
    pass
    
# test (décommenter pour tester)
# assert caractere_plus_frequent("anticonstitutionnellement") == 'n'

#####
# 5 #
#####

# Niveau 2 :* En utilisant la fonction caractere_plus_frequent, programmer une fonction deviner_cle_cesar(message) qui prend en argument un message chiffré avec un code de César (une chaine de caractere) et retourne une clé probable pour le message (un entier) déterminée par analyse de fréquence.

def deviner_cle_cesar(message):
    pass


#####
# 6 #
#####

# Niveau 3 : Programmer une fonction deviner_cle_vigenere(message, longueur) qui prend en arguments le message chiffré (une chaine de caractère) et une longueur possible de clé (un entier) et retourne la clé la plus probable en utilisant une analyse de fréquence (liste d'entier).

def deviner_cle_vigenere(message, longueur):
    pass
      