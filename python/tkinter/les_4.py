import tkinter as tk

win = tk.Tk()
win.title('Четвертое приложение')
win.geometry('400x400+100+100')

btn1 = tk.Button(win,text='button1')
btn2 = tk.Button(win,text='button2')
btn3 = tk.Button(win,text="IT'S BIG BUTTON NUMBER 3")
btn4 = tk.Button(win,text='button4')
btn5 = tk.Button(win,text='button5')
btn6 = tk.Button(win,text='button6')
btn7 = tk.Button(win,text='button7')


# btn1.grid(row=0, column=0)
# btn2.grid(row=0, column=1, sticky='ns')
# btn3.grid(row=0, column=2)
# btn4.grid(row=1, column=0, columnspan=2, sticky='we') # объединить 2 колонки
# btn5.grid(row=1, column=2, sticky='e')
# btn6.grid(row=0, column=3, rowspan=2, stick='ns')  # sticky растягивает по сторонам света. почему то работает и stick & sticky

for i in range(5):
    for j in range(3):
        tk.Button(win, text=f'Hello {i}/{j}').grid(row=i,column=j)

win.grid_columnconfigure(0, minsize=100) # Минимальный размер нулевой колонки
win.grid_rowconfigure(0, minsize=50)  # Минимальный размер нулевой строки

win.mainloop()
