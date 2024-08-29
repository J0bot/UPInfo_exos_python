"""
HEIG-VD
Auteur :        José Gasser
Date :          28.08.2024
Description :   Script pour acceder à tous les exos
"""

# importation des scripts
import exo12
import exo13
import exo16
import exo17

# print la liste d'exos


def show_exercices():
    print("\n1. Exo 12 : l'âge à la mort")
    print("2. Exo 13 : calcul du volume d'un cône")
    print("3. Exo 16 : contrôle du flux d'instructions")
    print("4. Exo 17 : table de multiplication, avec boucle for")
    # print("5. Exo 18 : boucle for et fonctions")
    # print("6. Exo 19 : devinette")
    print("0. Quitter\n")


# Fonction main, fait tourner tout le code


def main():
    print("Bienvenue sur le script qui gère tous les exercices !")
    while True:
        show_exercices()
        choix_exo = 0
        # Si l'input est incorrect on refait la demande
        try:
            choix_exo = int(input("Choisissez l'exercice : "))
        except:
            print("Valeur incorrecte")
            continue
        print("\n")

        # série de if et elif pour le choix de l'exo
        if choix_exo == 1:
            exo12.main()
        elif choix_exo == 2:
            exo13.main()
        elif choix_exo == 3:
            exo16.main()
        elif choix_exo == 4:
            exo17.main()
        elif choix_exo == 0:
            # quitter
            exit()
        else:
            continue


# invocation de la fonction main()
main()
