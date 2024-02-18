import string

password_criteria = {
    'length': 8,               
    'lowercase': True,          
    'uppercase': True,          
    'numbers': True,            
    'symbols': True             
}
password_correct = ''
while True:
    password = input('Enter password')
    for i in password:
        if i.isdigit() or i.islower() or i.upper() or i in string.punctuation:
            if len(password) >= password_criteria['length']:
                password_correct = 'Password is correct'
            
        else:
            password_correct = 'Incorrect format'
    break


print(password_correct)