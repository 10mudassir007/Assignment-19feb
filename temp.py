convertors = {'Celsius':(9/5),'Farhenheit':(5/9)}

x = int(input('Enter choice \n1.Celsius to Farhanheit\n2.Farhenheit to Celsius\n'))
y = int(input('Enter temperature to convert:'))

if x == 1:
    converted_temp = convertors['Celsius'] * y + 32
elif x == 2:
    converted_temp = convertors['Farhenheit'] * y - 32
print('Converted Temperature:',round(converted_temp,2))