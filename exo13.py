"""
HEIG-VD
Auteur :        José Gasser
Date :          24.08.2024
Description :   Calcul du volume d'un cône
"""
import math

# Fonction principale


def main():
    print("Calculer le volume d'un cone")
    r = input("Enter the radius in m: ")

    r = float(r)
    h = input("Enter the height in m : ")

    h = float(h)
    v = math.pi * r * r * h / 3
    print(f'Volume = {v:.2f} m³')


# main()
