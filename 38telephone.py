# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

### РАБОТАЕТ ТОЛЬКО НА АНГЛ. РУССКИЙ РАБОТАЕТ С ПРОБЛЕМАМИ

def readfile():
    data = [i.split() for i in open("test.txt", "r", encoding = 'utf-8')]
    return data

def printinfo(data):
    for i in data:
        print(*i, sep = " ")

def search (data):
    start = -1
    famil = input('искомая Фамилия: ')
    for i in data:
        if famil in i:
            start = 0
            print(*i, sep = " ")
    if start: print('Такой фамилии не найдено')

def add_new (data):
    a = input("Введите фамилию (только на англ, русский язык не работает): ")
    b = input("Введите номер: ")
    with open('test.txt', 'a') as f:
        f.write(a +"    "+ b +'\n')
    return main()
    
def delete(): ### НЕ РАБОТАЕТ КАК НАДО
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
    return main()

def main():
    my_choice = -1
    data = readfile()
    while my_choice != 0:
        print("выберите одно из действий:")
        print("1 - вывести инфо на экран")
        print("2 - поиск по фамилии ### РАБОТАЕТ ТОЛЬКО НА АНГЛ. РУССКИЙ РАБОТАЕТ С ПРОБЛЕМАМИ")
        print("3 - добавить контакт ### РАБОТАЕТ ТОЛЬКО НА АНГЛ. РУССКИЙ РАБОТАЕТ С ПРОБЛЕМАМИ")
        print("4 - удалить контакт ### НЕ РАБОТАЕТ КАК НАДО(УДАЛЯЕТ ИЗ ФАЙЛА, НО ПОТОМ С НИМ НЕЛБЗЯ РАБОТАТЬ)")
        print("0 - выйти из программы")
        my_choice = int(input())
        if my_choice == 1:
            printinfo(data)
        elif my_choice == 2:
            search (data)
        elif my_choice == 3:
            add_new (data)
        elif my_choice == 4:
            delete (data)
      
    print("До свидания")

if __name__ == "__main__":
    main()