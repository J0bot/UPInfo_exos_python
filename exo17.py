"""
HEIG-VD
Auteur :        José Gasser
Date :          28.08.2024
Description :   Programme pour les tables de multiplication
"""
def exo2():

    for n in range(1,11):
        for i in range(1,11):
            print(f"{n} * {i:2d} = ",n*i)
        print("")

def exo3():
    n = int(input("Donnez un nombre :"))
    for i in range(1,11):
        print(f"{n} * {i:2d} = ", n*i)

exo3()
