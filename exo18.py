import math


def factoriel(n):
    resultat = math.factorial(n)

    # Construire l'expression détaillée
    expression = " × ".join(str(i) for i in range(n, 0, -1))

    # Afficher le résultat complet
    print(f"{n}! = {expression} = {resultat}")


def main():
    print("Bienvenue dans boucle for et fonctions")
    factoriel(int(input("Entrez le nombre n que vous voulez : ")))
