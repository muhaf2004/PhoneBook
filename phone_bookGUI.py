from tkinter import *
import os

phone_book = dict()


def clear():
    input_tel.delete(0, END)
    input_last_name.delete(0, END)
    input_first_name.delete(0, END)
    input_patronymic.delete(0, END)
    input_address.delete(0, END)


def add():
    tel_ = input_tel.get()
    if tel_ in phone_book:
        label_info.config(text="Такой номер уже существует")
    else:
        value_ = list()
        value_.append(input_last_name.get())
        value_.append(input_first_name.get())
        value_.append(input_patronymic.get())
        value_.append(input_address.get())
        phone_book[tel_] = value_

        list_tel.insert(END, tel_)


def output_data(tel_):
    value_ = phone_book[tel_]
    last_name_ = value_[0]
    first_name_ = value_[1]
    patronymic_ = value_[2]
    address_ = value_[3]

    clear()
    input_tel.insert(0, tel_)
    input_last_name.insert(0, last_name_)
    input_first_name.insert(0, first_name_)
    input_patronymic.insert(0, patronymic_)
    input_address.insert(0, address_)


def select_list_tel(event):
    w = event.widget
    i = int(w.curselection()[0])
    tel_ = w.get(i)
    output_data(tel_)


def search():
    search_text = input_search.get()
    if search_text in phone_book:
        output_data(search_text)
    else:
        for key, item in phone_book.items():
            for val in item:
                if val == search_text:
                    output_data(key)
                else:
                    label_info.config(text="Ничег не найдено")


window = Tk()
window.title("PhoneBook")
window.geometry("500x300")

# Объявление элементов окна
label_tel = Label(text="Номер телефона")
input_tel = Entry()

label_last_name = Label(text="Фамилия")
input_last_name = Entry()

label_first_name = Label(text="Имя")
input_first_name = Entry()

label_patronymic = Label(text="Отчество")
input_patronymic = Entry()

label_address = Label(text="Адрес")
input_address = Entry()

button_add = Button(text="Добавить", command=add)
button_clear = Button(text="Очистить", command=clear)

label_list_tel = Label(text="Список телефонов")
list_tel = Listbox()

label_info = Label(text="Программа готова к работе")

label_search = Label(text="Поиск")
input_search = Entry()
button_search = Button(text="Найти", command=search)

# Позиционирование
label_search.grid(row=0, column=0, padx=10, pady=5, sticky="e")
input_search.grid(row=0, column=1, padx=10, pady=5)
button_search.grid(row=0, column=2, pady=5)

label_tel.grid(row=1, column=0, padx=10, pady=5, sticky="w")
input_tel.grid(row=1, column=1)

label_last_name.grid(row=2, column=0, padx=10, pady=5, sticky="w")
input_last_name.grid(row=2, column=1, padx=10)

label_first_name.grid(row=3, column=0, padx=10, pady=5, sticky="w")
input_first_name.grid(row=3, column=1)

label_patronymic.grid(row=4, column=0, padx=10, pady=5, sticky="w")
input_patronymic.grid(row=4, column=1, padx=10)

label_address.grid(row=5, column=0, padx=10, pady=5, sticky="w")
input_address.grid(row=5, column=1, pady=15)

button_add.grid(row=2, column=2, padx=10)
button_clear.grid(row=4, column=2, padx=10)

label_list_tel.grid(row=1, column=3)
list_tel.grid(row=2, column=3, rowspan=4, pady=15)

label_info.grid(row=6, column=0, columnspan=4, sticky="w")

list_tel.bind('<<ListboxSelect>>', select_list_tel)

if os.path.exists("PhoneBook.csv"):
    with open("PhoneBook.csv", "r") as file:
        lines = file.readlines()
        for line in lines:
            elements = line.split(";")
            tel = elements[0]
            last_name = elements[1]
            first_name = elements[2]
            patronymic = elements[3]
            address = elements[4]
            value = list()
            value.append(last_name)
            value.append(first_name)
            value.append(patronymic)
            value.append(address)
            phone_book[tel] = value
            list_tel.insert(END, tel)

window.mainloop()