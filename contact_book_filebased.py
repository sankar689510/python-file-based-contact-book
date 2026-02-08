contacts = {}
try:
    with open("contact.txt", "r") as file:
        for line in file:
            name, number = line.strip().split(",")
            contacts[name] = number
except FileNotFoundError:
    pass


def save_contacts():
    with open("contact.txt", "w") as file:
        for name, number in contacts.items():
            file.write(f"{name},{number}\n")


def add_contact():
    name = input("enter the name:")
    while True:
        number = input("enter the number:")
        if number.isdigit() and len(number) == 10:
            break
        else:
            print("Invalid Number")
    contacts[name] = number
    save_contacts()
    print("contact added successfully")


def view_contacts():
    if not contacts:
        print("There is no contact saved")
    else:
        print("----Saved contacts----")
        for name, number in contacts.items():
            print(name, ":", number)


def show_menu():
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3.search contacts")
    print("4. Exit")


def search_contact():
    cnt_name = input("enter the name:-")
    if cnt_name in contacts:
        print("The number is:-", contacts[cnt_name])
    else:
        print("contact not found")


while True:
    show_menu()
    choice = input("enter a number(1-4):-")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("Exiting contact book...")
        break
    else:
        print("Invalid Number Please Try Again")
