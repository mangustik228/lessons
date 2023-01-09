import tkinter as tk

win = tk.Tk()
win.geometry('400x400+100+100')
win.title('lesson 5')

def get_entry():
    value = name.get() # Получить значение из Виджета get 
    if value:
        print(value)
    else:
        print('Empty entry')
        
def clean_entry():
    name.delete(0, 'end')  # Есть два аргумент first и end - c какой позиции удаляем и по какую, 0 -значит удаление с первой позиции, 
    
def submit():
    print(name.get())
    print(password.get())
# Создаем виджут Entry
name = tk.Entry(win) 
password = tk.Entry(win, show='*') 
tk.Label(win, text = 'Имя').grid(row=0, column=0, stick='w')
tk.Label(win, text = 'Пароль').grid(row=3, column=0, stick='w')

name.grid(row=0, column=1)  # Располагаем виджет в окне
password.grid(row=3, column=2)
tk.Button(win, text='Жмякнуть', command=get_entry).grid(row=1,column=0, stick='we')  # Создаем кнопку чтоб получить значение
tk.Button(win, text='Выкинуть', command=clean_entry).grid(row=1,column=1, stick='we')  # Создаем кнопку чтоб очистить
tk.Button(win, text='Позать пароль', command=submit).grid(row=2,column=1, stick='we')  # Создаем кнопку чтоб очистить
tk.Button(win, text='Поздороваться', command=lambda: name.insert(0, 'hello'))\
    .grid(row=2,column=0, stick='we')  # Создаем кнопку вставить занчение в entry

win.grid_columnconfigure(0, minsize=100) 
win.grid_columnconfigure(1, minsize=150)
win.mainloop()