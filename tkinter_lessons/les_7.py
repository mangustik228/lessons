import tkinter as tk

win = tk.Tk()

win.geometry('500x500+100+100')
win.title('lesson 7 Raddiobutton')



levels = {
    1: 'easy',
    2: 'middle',
    3: 'hard'
}
level_var = tk.IntVar()
level_text = tk.StringVar()
people_var = tk.IntVar()

def select_level():
    level = level_var.get()
    level_text.set(f'Вы выбрали {level} уровень.')
    print(levels[level])
    
def select_rase():
    people = people_var.get()
    people_var.set(f'Вы выбрали расу: {people}')
    

tk.Label(text='Выберите уровень сложности').pack()
for key in sorted(levels):
    tk.Radiobutton(text=levels[key], variable=level_var, value=key, command=select_level).pack()
tk.Label(textvariable=level_text).pack()
tk.Label(text='Выберите расу').pack()
tk.Radiobutton(text='elfs', variable=people_var, value=4, command=select_rase).pack()
tk.Radiobutton(text='humans', variable=people_var, value=5, command=select_rase).pack()
tk.Radiobutton(text='orks', variable=people_var, value=6, command=select_rase).pack()
tk.Label(textvariable=people_var).pack()

win.mainloop()