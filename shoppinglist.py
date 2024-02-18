# Shopping List Program without Functions

# Initialize an empty shopping list dictionary
shopping_list = {}

while True:
    print("\nOptions:")
    print("1. Add item to the list")
    print("2. Remove item from the list")
    print("3. Check off item in the list")
    print("4. Display the current list")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        item = input("Enter the item to add: ")
        shopping_list[item] = False
        print(f"{item} added to the list.")

    elif choice == '2':
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            del shopping_list[item]
            print(f"{item} removed from the list.")
        else:
            print(f"{item} not found in the list.")

    elif choice == '3':
        item = input("Enter the item to check off: ")
        if item in shopping_list:
            shopping_list[item] = True
            print(f"{item} checked off.")
        else:
            print(f"{item} not found in the list.")

    elif choice == '4':
        print("\nCurrent Shopping List:")
        for item, status in shopping_list.items():
            print(f"[{'✔' if status else ' '}] {item}")

    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
