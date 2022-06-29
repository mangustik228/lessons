import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry('500x500+100+100')
win.title('lesson 7 Combobox')
weekdays = ('monday', 'tuesday', 'wednesday',
            'thuesday', 'friday', 'saturday', 'sunday')
list_int = [1, 2, 3, 4, 5]


def show_day():
    print(combo.get(), combo_int.get())


def set_day():
    combo.set('friday')


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self):  # чудо метод для изменения отображения класса
        return f'Point {self.x} / {self.y}'


tk.Label(win, text='Выберите из меню').pack()
combo = ttk.Combobox(win, values=weekdays)
combo_int = ttk.Combobox(win, values=list_int)
combo_point = ttk.Combobox(win, values=[Point(2, 5), Point(3, 4)])
ttk.Button(win, text='Жахнуть', command=show_day).pack()
ttk.Button(win, text='Жахнуть так жахнуть', command=set_day).pack()
combo.current(3)  # число являеется индексом который передаем
combo_int.current(1)
combo.pack()
combo_int.pack()
combo_point.pack()
win.mainloop()
