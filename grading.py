grading_scale = {
    'A1': 90,
    'A': 80,
    'B': 70,
    'C': 60,
    'F':0,
}



marks = {}
for i in range(5):
    y = input('Enter subject name:')
    x = int(input(f'Enter marks in subject {i+1}:'))
    marks[y] = x

total = (sum(marks.values())/80) * 100

grade = 0

for j,k in grading_scale.items():
    if total >= k:
        grade = j
        break
print('Overall Grade : ',grade)
