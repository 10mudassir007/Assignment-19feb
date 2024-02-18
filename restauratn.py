import csv


csv_file_path = 'c:/Users/mudda/OneDrive/Desktop/aaa.csv'


menu = {'Category':{},'Item':[],'Description':[],'Price':[]}
with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
    # Create a CSV reader object
    csv_reader = csv.reader(csvfile)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Each row is a list of values
        print(row)

        category = row[0]
        item = row[1]
        description = row[2]
        price = row[3]
        if category not in menu['Category']:
            menu['Category'][category] = []
        menu['Category'][category].append({'Item': item, 'Description': description, 'Price': price})
        menu['Item'].append(row[1])
        menu['Description'].append(row[2])
        menu['Price'].append(row[3])

while True:
    print('Available Categories:')
    for index, category in enumerate(menu['Category'], start=1):
        print(f'{index}. {category}')

    choice = int(input('Enter category (1-6) or 7 to Exit: '))
    if 1 <= choice <= 6:
        selected_category = list(menu['Category'])[choice - 1]
        print(f'Selected Category: {selected_category}')
        print(menu['Category'][selected_category])
    elif choice == 7:
        break
    else:
        print('Invalid choice. Please enter a number between 1 and 7.')