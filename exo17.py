"""
HEIG-VD
Auteur :        José Gasser
Date :          28.08.2024
Description :   Programme pour les tables de multiplication
"""


def exoa():
    for i in range(1, 11):
        print(f"8 * {i:2d} = ", 8*i)


def exob():

    for n in range(1, 11):
        for i in range(1, 11):
            print(f"{n} * {i:2d} = ", n*i)
        print("")


def exoc():
    try:
        n = int(input("Donnez un nombre :"))
    except:
        print("Boo there's an error ! ")
    for i in range(1, 11):
        print(f"{n} * {i:2d} = ", n*i)


def main():
    print("Bienvenue sur l'exerice sur les multiplications !\n")
    choix = input("Exercice a, b ou c ?\n>")
    if choix == 'a':
        exoa()
    elif choix == 'b':
        exob()
    elif choix == 'c':
        exoc()
    else:
        print("valeur incorrecte :(")

# main()
# exoc()
