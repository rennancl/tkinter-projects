import tkinter as tk
from tkinter import *


def get_text(root):
    row = Frame(root)
    lab = Label(row, width=22, text='Digite aqui o texto: ', anchor='w')
    text = Entry(row)
    text.insert(0,"")
    row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
    lab.pack(side = LEFT)
    text.pack(side = RIGHT, expand = YES, fill = X)
    return text

def create_output(output, text):
    text = text.get()
    output.delete(1.0,tk.END)
    output.insert(tk.END,text)

root = tk.Tk()
text = get_text(root)
output = tk.Text(root, height=3, width=40)
output.pack()

exit_button = Button(root, text = 'Sair', command = root.quit)
exit_button.pack(side = BOTTOM, padx = 5, pady = 5)

run_button = Button(root, text = 'Executar', command = lambda o=output, t=text: create_output(o, t))
run_button.pack(side = BOTTOM, padx = 5, pady = 5)

root.bind('<Return>', (lambda event, o=output, t=text: create_output(o, t)))
root.bind('<Escape>', (lambda event: root.quit()))

root.mainloop()