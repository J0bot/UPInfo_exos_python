import math

def menu():
    print("\nChoose an options")
    print("1. Calculate the volume of a cone")
    print("2. Calculate the volume and surface of a sphere")
    print("3. Quit the program")
    try :
        choice = int(input("> "))
    except : 
       return 4
    #print(choice)
    return choice

def choice1():
    print("Calculer le volume d'un cone")
    r = input("Enter the radius : ")
    r = float(r)
    h = input("Enter the height : ")
    h = float(h)
    v = math.pi * r * r * h / 3
    print(f'Volume = {v:.2f} ')

def choice2():
    print("Calculer le volume et la surface d'une sphere")
    r = input("Enter the radius : ")
    r = float(r)

    s = 4*math.pi*r**2
    v = s*r/3
    print(f"Surface : {s:.2f}, Volume : {v:.2f}")
#main program

choice = 0

while True:
    choice = menu()
    print(choice)

    if choice == 1:
        choice1() 
    elif choice == 2:
        choice2()
    elif choice == 3:
        exit("Quitting the program...")
    else : 
        print("\nWrong stuff going on...\n")
