def menu():
    print("Choose an options")
    print("1. Calculate the volume of a cone")
    print("2. Calculate the volume and surface of a sphere")
    print("3. Quit the program")
    choice = input("> ")
    #print(choice)
    return choice

#main program

choice = menu()
print(choice)

if choice == '1':
    print("Choice 1")
elif choice == '2':
    print("Choice 2")
elif choice == '3':
    exit("Quitting the program...")
else : 
    print("Wrong stuff going on...")
