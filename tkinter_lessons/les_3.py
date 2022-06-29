import tkinter as tk
from tkinter.constants import DISABLED

win = tk.Tk()
win.geometry('400x400+100+100')
win.title('Третье окно')


def create_lavel():
    label = tk.Label(win,text='new')
    label.pack()
    
    
def foo():
    print('hello')
    if button3['state'] == tk.NORMAL:
        button3['state'] = tk.DISABLED
    else:
        button3['state'] = tk.NORMAL
    
count_of_push = 0

def counter():
    global count_of_push
    count_of_push += 1
    button4['text'] = f'Счетчик нажатий {count_of_push}'  # Передаем как словарь!!! 
    

button1 = tk.Button(win,   # Создаем класс кнопки и передаем ей окно
                    text='button1', # Текст кнопки
                    command=foo  # Передаем функию (и только функию!)
)

button2 = tk.Button(win,   
                    text='button2', 
                    command=create_lavel  # Передаем функию (и только функию! и без аргументов) можно лямду
)

button3 = tk.Button(win,   
                    text='button3', 
                    command=lambda: tk.Label(win,text='new from but3').pack()
)

button4 = tk.Button(win,   
                    text=f'Счетчик нажатий {count_of_push}', 
                    command=counter,
                    activebackground='blue',  # Цвет активно нажатой кнопки.
                    state=tk.DISABLED  # Заморозить кнопку (по умолчанию Normal)
)

button1.pack()  # Размещаем окно кнопки
button2.pack()  
button3.pack()  
button4.pack()  

win.mainloop()

