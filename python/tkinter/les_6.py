import tkinter as tk

def show_value():
    print('Флажок 18', over_flag1.get())
    print('Флажок 2', value_flag2.get())

def select_all():
    for check in [flag1, flag2, flag3]:
        check.select()

def deselect_all():
    for check in [flag1, flag2, flag3]:
        check.deselect()
        
def switch_all():
    for check in [flag1, flag2, flag3]:
        check.toggle()


win = tk.Tk()
win.title('lesson 6')
win.geometry('500x500+100+100')
over_flag1 = tk.StringVar() # Переменная из tkinter с строкой
over_flag1.set('No') # Устанавливаем значение по умолачанию для переменной over_flag1
value_flag2 = tk.IntVar() # Переменная из tkinter co строкой
value_flag2.set(1)

flag1 = tk.Checkbutton(win, text='Использовалось ли Вам 18?',  # Текст, какое окно 
                        variable=over_flag1,   # Говорим какой переменной надо присваивать.
                        offvalue='No', # Если значок выключен, переменная over_flag1 присваиваем "No"
                        onvalue='Yes') # Если значок включен, переменной over_flag1 присваиваем "Yes"
flag2 = tk.Checkbutton(win, text='Получать рекламу?', 
                        variable=value_flag2,
                        offvalue=0,
                        onvalue=1)
flag3 = tk.Checkbutton(win, text='Хотите подписатся на канал?', indicatoron=0)

flag1.grid(row=0, column=0, sticky='w')
flag2.grid(row=1, column=0, sticky='w')
flag3.grid(row=2, column=0, sticky='w')

tk.Button(win, text='select all', command=select_all).grid(row=3,column=0, sticky='we')
tk.Button(win, text='deselect all', command=deselect_all).grid(row=4,column=0, sticky='we')
tk.Button(win, text='switch_all', command=switch_all).grid(row=5,column=0, sticky='we')
tk.Button(win, text='show_value', command=show_value).grid(row=5,column=0, sticky='we')

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()
    
