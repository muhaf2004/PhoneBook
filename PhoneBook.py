# *** PhoneBook ***
#
# tel - номер телефона, строка
# first_name - имя, строка
# last_name - фамилия, строка
# patronymic - отчество, строка
# address - адрес, строка
# {tel: [last_name, first_name, patronymic, address]}

from PhoneBook_lib import *
def input_data():
    temp = list()
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    address = input("Введите адрес: ")
    temp.append(last_name)
    temp.append(first_name)
    temp.append(patronymic)
    temp.append(address)
    return temp


phone_book = dict()

welcome()

while True:
    menu()
    choice = int(input("Введите режим работы: "))

    if choice == 1:
        print(phone_book)
    elif choice == 2:
        tel = input("Введите номер телефона: ")
        if tel in phone_book:
            print("Такой номер уже существует")
            continue
        else:
            value = input_data()
            phone_book[tel] = value
        value = input_data()
        phone_book[tel] = value
    elif choice == 3:  # TODO Редактирование записи
        print()
    elif choice == 4:
        tel = input("Введите номер телефона для удаления: ")
        if tel in phone_book:
            note = phone_book.pop(tel)
            print('Запись',note,'удалена')
        else:
            print("Вы ввели неправильный номер")
            continue
        print()
    elif choice == 0:  # TODO Выход
        print("До свидания")
        break
    else:
        print("Неправильный режим")
        continue