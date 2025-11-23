def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()                  # Call display_menu
        choice = input("Enter your choice: ").strip()  # Choice input as number

        if choice == '1':
            item = input("Enter item to add: ").strip()
            shopping_list.append(item)
        elif choice == '2':
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
        elif choice == '3':
            print(shopping_list)
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
