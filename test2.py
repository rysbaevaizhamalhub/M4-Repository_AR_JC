# Aizhamal, James
# Oct 17th, 2024

# write a program to print a number of options presented to the user
#  allow the user to select an option from the list.

while True:
    print("Please choose your option from the list below:")
    print("1. Learn Python")
    print("2. Learn Java")
    print("3. Go swimming")
    print("4. Have dinner")
    print("5. Go to bed")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '0':
        print("Exiting the program. Goodbye!")
        break
    elif choice == '1':
        print("You selected: Learn Python")
    elif choice == '2':
        print("You selected: Learn Java")
    elif choice == '3':
        print("You selected: Go swimming")
    elif choice == '4':
        print("You selected: Have dinner")
    elif choice == '5':
        print("You selected: Go to bed")
    else:
        print("Invalid choice, try again.")
