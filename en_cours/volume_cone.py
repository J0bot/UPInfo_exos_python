# Nom du fichier : volume_cone.py
# Auteur : José Gasser
# Date : 23.08.2024 1739
# Version : 1.0

import math
import time


# constantes
PI = math.pi

# fonctions

# Effet cool quand on demarre le script


def typewriter_truc(texte, delay=0.1):
    for char in texte:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Prendre l'input de l'utilisateur, checker si ce qu'il donne est correct


def input_en_float(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Faut mettre un nombre valide 😀")


# Message de bienvenue
typewriter_truc("Bienvenue dans le calcul d'un volume !")

# grab le rayon
rayon = input_en_float("\nDonne le rayon (en m) : ")

# grab l'hauter
hauteur = input_en_float("\nDonne la hauteur (en m) : ")

# Calcul du volume
volume = (PI*(rayon**2)*hauteur)/3

# Effet cinématique
typewriter_truc("\nCalcul... 😇😇😇")

# Affichage de la solution
typewriter_truc(
    "\nCeci est le volume : {:.2f} mètres cubes".format(volume), 0.05)
