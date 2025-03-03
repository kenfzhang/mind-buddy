import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk
from tkinter import Label

root = tk.Tk()
root.title('Mindbuddy')
root.geometry('600x400')

# Load and convert the image
img = Image.open("gh-pfp.png")
img = ImageTk.PhotoImage(img)

label1 = Label(root, image=img)
label1.place(x=0, y=0)

label1.image = img


def button_clicked():
    print('Button clicked')
    button.config(text="Wow!")


button = ttk.Button(root, text='Click Me', command=button_clicked)
button.pack()

root.mainloop()
