import tkinter as tk
from tkinter.constants import LEFT
from typing import cast

win = tk.Tk()


# Создаем переменную label(не обязательно) - 


label_1 = tk.Label(win,  # win - в каком окне мы создаем
                   text='''Это текст который хочу вывести
это вторая строка этого текста
а это третья строка.вот!''',  
                   bg='red',  # bg= цвет бэкграунда 
                   fg='white',  # fg= fondground - цвет фона
                   font=('Arial', 15, 'bold'),  # Передаем кортежем переменные (шрифт/размер/тип)
                   padx=1,  # Отступ по x
                   pady=15,  # Важно что отсутупы внутри самого label
                   width=40,  # Ширина в количестве знаков!!! обрезает что есть
                   height=3,  # Тоже указывается по высоте
                   anchor='sw',  # Прикрепление по стороне света n=north, w=west, e=east, s=south, по умолчанию centre
                   relief=tk.RAISED,  # Отображение границ
                   bd=10,  # Изменение размера границы, по умолчанию 2
                   justify=tk.LEFT  # По какой границе ровнять текст
)






label_1.pack()  # необходимо закинуть label (могут быть и другие методы)

win.title('Второе окно')
win.geometry('800x500+100+100')
win.mainloop()

