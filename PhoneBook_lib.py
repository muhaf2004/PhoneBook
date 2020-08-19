# *** PhoneBook ***
#
# tel - номер телефона, строка
# first_name - имя, строка
# last_name - фамилия, строка
# patronymic - отчество, строка
# address - адрес, строка
# {tel: [last_name, first_name, patronymic, address]}

def welcome():
    print("*******")
    print("*** PhoneBook - телефонный справочник ***")
    print("*******")


def menu():
    print("=== === ===")
    print("Режимы работы:")
    print("1. Показать все записи")
    print("2. Добавить запись")
    print("3. Редактировать запись")
    print("4. Удалить запись")
    print("5. Сохранить в файл")
    print("0. Выход")


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


def show(phone_book):
    print("--- Телефонный справочник ---")
    for tel in phone_book:
        value = phone_book[tel]
        temp = value[0] + " " + value[1] + " " + value[2] + ", " + value[3]
        print(tel, ':', temp)
    print("--- --- ---")


def input_record(phone_book):
    tel = input("Введите номер телефона: ")
    if tel in phone_book:
        print("# Такой номер уже существует #")
    else:
        value = input_data()
        phone_book[tel] = value
        print("# Запись успешно добавлена #")


def edit_record(phone_book):
    tel = input("Введите номер телефона: ")
    if tel in phone_book:
        temp = input_data()
        phone_book[tel] = temp
        print("# Запись успешно изменена #")
    else:
        print("# Вы ввели неправильный номер #")


def delete_record(phone_book):
    tel = input("Введите номер телефона для удаления: ")
    if tel in phone_book:
        phone_book.pop(tel)
        print("# Запись " + tel + " удалена #")
    else:
        print("# Вы ввели неправильный номер #")


def export_to_file(phone_book):
    with open("PhoneBook.csv", "w") as file:
        for tel in phone_book:
            value = phone_book[tel]
            temp = tel + ";" + value[0] + ";" + value[1] + ";" + value[2] + ";" + value[3] + "\n"
            file.write(temp)