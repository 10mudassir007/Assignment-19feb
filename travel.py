# Dictionary to store categories and corresponding expenses
travel_expenses = {'Transportation': 0, 'Accommodation': 0, 'Food': 0}

# Display initial expenses
print("Initial Travel Expenses:")
for category, expense in travel_expenses.items():
    print(f"{category}: ${expense:.2f}")

# Allow users to input expenses for each category
for category in travel_expenses:
    expense = float(input(f"Enter {category} expense: $"))
    travel_expenses[category] += expense

# Display updated expenses
print("\nUpdated Travel Expenses:")
for category, expense in travel_expenses.items():
    print(f"{category}: ${expense:.2f}")
