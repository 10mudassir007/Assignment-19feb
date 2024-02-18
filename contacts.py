contacts = {}
while True:
    x = int(input('Enter option\n1.Add\n2.Search\n3.Update\n4.Exit\n'))
    if x == 1:
        name = input('Enter name: ')
        number = input('Enter number: ')
        contacts[name] = number
    elif x == 2:
        name = input('Enter name: ')
        if name in contacts:
            print(f'Number of {name}:',contacts[name])
        else:
            print('Contact not found')
    elif x == 3:
        name = input('Enter name: ')
        if name in contacts:
            number = input('Enter number: ')
            contacts[name] = number
        else:
            print('Contact not found')
    else:
        break
print(contacts)
    