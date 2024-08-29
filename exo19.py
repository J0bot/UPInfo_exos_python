"""
HEIG-VD
Auteur :        José Gasser
Date :          29.08.2024
Description :   Programme de devinette
"""

import random


def main():
    n = random.randint(0, 100)
    counter = 0
    while True:
        b = int(input("Entrez un nombre : "))
        counter += 1
        if b > n:
            print(f"{b} est trop haut !")
        elif b < n:
            print(f"{b} est trop petit !")
        elif b == n:
            print("BRAVO")
            print(f"Vous avez deviné en {counter} étapes")
            break


# main()
