# *** PhoneBook ***
#
# tel - номер телефона, строка
# first_name - имя, строка
# last_name - фамилия, строка
# patronymic - отчество, строка
# address - адрес, строка
# {tel: [last_name, first_name, patronymic, address]}

from PhoneBook_lib import *

phone_book = dict()

welcome()

while True:
    menu()
    choice = int(input("Введите режим работы: "))

    if choice == 1:
        show(phone_book)
    elif choice == 2:
        tel = input("Введите номер телефона: ")
        if tel in phone_book:
            print("Такой номер уже существует")
            continue
        else:
            value = input_data()
            phone_book[tel] = value
    elif choice == 3:  # TODO Редактирование записи
        print()
    elif choice == 4:
        tel = input("Введите номер телефона для удаления: ")
        if tel in phone_book:
            note = phone_book.pop(tel)
            print('Запись', note, 'удалена')
        else:
            print("Вы ввели неправильный номер")
            continue
    elif choice == 5:
        with open("PhoneBook.csv", "w") as file:
            for tel in phone_book:
                value = phone_book[tel]
                temp = tel + ";" + value[0] + ";" + value[1] + ";" + value[2] + ";" + value[3] + "\n"
                file.write(temp)
    elif choice == 0:
        print("До свидания")
        break
    else:
        print("Неправильный режим")
        continue
