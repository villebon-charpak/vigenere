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
    

#####
# 2 #
#####

# Niveau 1 : Sur le même principe, on veut désormais effectuer l'opération inverse de déchiffrage (c'est l'opération que l'on effectue lorsque l'on veut lire un message chiffré que l'on reçoit). Programmer une fonction dechiffre_vigenere(message, cle) qui prend en arguments le message chiffré (une chaine de caractère) et la clé (une liste d'entiers) et retourne le message déchiffré.


def dechiffre_vigenere(secret, cle):
    # arguments :
    #       secret : chaine de caractère contenant le message chiffré
    #       cle : liste d'entiers correspondant à la liste des décalages qui ont été effectués pour chiffrer
    # la fonction retourne une chaine de caractère qui correspond au message original
    
    pass # remplacer cette ligne par votre code
    
