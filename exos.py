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
import exo18
import exo19

# print la liste d'exos


def show_exercices():
    """
    Affiche le menu avec la liste des exercices disponibles.
    """
    print("\n1. Exo 12 : l'âge à la mort")
    print("2. Exo 13 : calcul du volume d'un cône")
    print("3. Exo 16 : contrôle du flux d'instructions")
    print("4. Exo 17 : table de multiplication, avec boucle for")
    print("5. Exo 18 : boucle for et fonctions")
    print("6. Exo 19 : devinette")
    print("0. Quitter\n")


# Fonction main, fait tourner tout le code


def main():
    """
    Fonction principale qui permet à l'utilisateur de choisir et d'exécuter un exercice.
    """
    print("Bienvenue sur le script qui gère tous les exercices !")
    while True:
        show_exercices()
        choix_exo = 0
        # Validation de l'entrée utilisateur
        try:
            choix_exo = int(input("Choisissez l'exercice : "))
        except:
            print("Valeur incorrecte")
            continue
        print("\n")

        # Appel de la fonction principale de l'exercice choisi
        if choix_exo == 1:
            exo12.main()
        elif choix_exo == 2:
            exo13.main()
        elif choix_exo == 3:
            exo16.main()
        elif choix_exo == 4:
            exo17.main()
        elif choix_exo == 5:
            exo18.main()
        elif choix_exo == 6:
            exo19.main()
        elif choix_exo == 0:
            # Quitter le programme
            print("Au revoir...")
            exit()
        else:
            continue


# Invocation de la fonction main pour démarrer le programme
if __name__ == "__main__":
    main()
