from PhoneBook_lib import *

phone_book = dict()

welcome()  # Ввод приветствия программы
import_from_file(phone_book)

while True:
    menu()  # Вывод пунктов меню
    choice = input("Введите режим работы: ")

    if choice == "1":  # Вывод на экран всех записей
        show(phone_book)
    elif choice == "2":  # Добавление записи
        input_record(phone_book)
    elif choice == "3":  # Редактирование записи
        edit_record(phone_book)
    elif choice == "4":  # Удаление записи
        delete_record(phone_book)
    elif choice == "5":  # Сохранение данных в файл
        export_to_file(phone_book)
    elif choice == "6":  # Очищение всего справочника
        phone_book.clear()
        log("Очищение всего справочника")
    elif choice == "0":  # Выход из программы
        print("До свидания")
        log("Выход из программы")
        break
    else:
        print("Неправильный режим")
        log("Неправильный режим")