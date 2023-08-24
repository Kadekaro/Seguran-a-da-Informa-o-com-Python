import webbrowser
from tkinter import *

root = Tk()

root.title('Abrir Brownser')
root.geometry('200x200')


def google():
    webbrowser.open('www.google.com')


Button(root, text='Abrir o Google', command=google).pack(pady=20)
root.mainloop()
