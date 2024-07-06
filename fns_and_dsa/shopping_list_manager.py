def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View item")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to shopping list.")

        elif choice == "2":
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}'removed from the shopping list")
            else:
                print("{Item} cannot be found, try the correct input.")   



        elif choice == "3":
            if shopping_list:
                print("Current shopping list")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("shopping list is currenty empty")  
        elif choice == "4":
            print("Goodbye")
            break
        else:
            return "Invalid choice please try again."


if __name__ == "__main__":
    main()