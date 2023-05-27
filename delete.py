 

data = [i.split() for i in open("test.txt", "r", encoding = 'utf-8')]
for i in data:
    print(*i, sep = " ")
famil = input('Человек на удаление: ')
for i in data:
    if famil in i:
        z = i
        print(z)
data.remove(z)
 
for i in data:
    print(*i, sep = " ")

data =  map(str, data)
print(type(data))
with open("test.txt", "w") as f:
    for i in data:
        f.write(i + '\n')