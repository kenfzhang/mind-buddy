import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Mindbuddy')
root.geometry('600x400')


def button_clicked():
    print('Button clicked')
    button.config(text="Wow!")


button = ttk.Button(root, text='Click Me', command=button_clicked)
button.pack()

root.mainloop()
