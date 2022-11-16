import tkinter as tk
from tkinter import *
from tkinter import messagebox
from defs import *
import pygame


def close():  # для закрытия окна
    window.destroy()


def clicked():  # генератор ключа
    enter = str(arg_enter.get())
    try:
        if len(enter) != 6:
            tk.messagebox.showerror("Error", "Only 6 numbers!")
        else:
            key.configure(text=key_maker(enter), font=("Arial", 17), fg='#ffffff')
    except ValueError:
        tk.messagebox.showerror("Error", "Only numbers!")


window = tk.Tk()  # создание окна
window.title('Demon Slayer: Kimetsu no Yaiba')
window.geometry('850x360')
bg = tk.PhotoImage(file='tami.png')

frame = tk.Frame(window)  # выравнивание
frame.place(relx=0.5, rely=0.5, anchor='center')

label_bg = tk.Label(frame, image=bg)  # фоновая картинка
label_bg.place(x=0, y=0)

lbl_enter = tk.Label(frame, text='Введите DEC-число (6 знаков)', font=("Arial", 15), bg='#ffffff')  # приглашение
lbl_enter.grid(column=0, row=0, padx=5, pady=5)

arg_enter = tk.Entry(frame, width=10, font=("Arial", 15), fg='#999999')  # окно ввода
arg_enter.insert(0, '******')
arg_enter.grid(column=0, row=1, padx=5, pady=5)

btn = tk.Button(frame, text='Получить ключ!', font=("Arial", 15), command=clicked)  # кнопка активации генератора
btn.grid(column=50, row=0, padx=200, pady=10)

lbl_out = tk.Label(frame, text='Ключ:', font=("Arial", 15))
lbl_out.grid(column=50, row=3, padx=10, pady=20)

key = tk.Label(frame, text='XXXXX-XXXXX XXXX', font=("Arial", 17), bg='#9370DB', fg='#ffffff')  # вывод
key.grid(column=50, row=4, padx=10, pady=10)

pygame.mixer.init()
music = Button(window, text="Music", command=play) # включение музыки
music.pack(pady=10)

stop = Button(window, text="Stop", command=stop) # выключение музыки
stop.pack(pady=10)

exit = tk.Button(frame, text='Выйти', font=("Arial", 15), command=close)  # выход
exit.grid(column=0, row=8, padx=0, pady=50)

window.mainloop()
