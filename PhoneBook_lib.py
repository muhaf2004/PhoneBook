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


def welcome():
    print("*******")
    print("*** PhoneBook - телефонный справочник ***")
    print("*******")


def menu():
    print("Режимы работы:")
    print("1. Показать все записи")
    print("2. Добавить запись")
    print("3. Редактировать запись")
    print("4. Удалить запись")
    print("5. Сохранить в файл")
    print("0. Выход")


def show(phone_book):
    for tel in phone_book:
        value = phone_book[tel]
        temp = value[0] + " " + value[1] + " " + value[2] + ", " + value[3]
        print(tel, ':', temp)