from interfeis import *
path = "Sem8\\phone_book.txt"
from rabota_s_failom import create
create(path)

enter = 0

while enter != 4:
    enter = interface()
    
    if enter == 1:
        from rabota_s_failom import add_contact
        stroka = str(input("Введите ФИО и номер через пробел "))
        add_contact(path,stroka)
    elif enter == 2:
        from rabota_s_failom import show_all
        print(show_all(path))
    elif enter == 3:
        from rabota_s_failom import search
        stroka = str(input("Введите фамилию"))
        search(path, stroka)
    elif enter == 5:
        from rabota_s_failom import deletecontact
        stroka = str(input("Введите фамилию"))
        deletecontact(path, stroka)
    elif enter == 6:
        from rabota_s_failom import change_name
        old_name = str(input("Введите фамилию которую хотите заменить"))
        new_name = str(input("Введите новые данные "))
        change_name(path, old_name, new_name)


print("спасибо за работу")
