x = 'Hello world'
dic = {}
for i in x:
    if i not in dic:
        dic[i] = 0

for i in x:
    dic[i] += 1
print(dic.items())