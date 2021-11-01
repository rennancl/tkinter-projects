from tkinter import *
from tkinter import filedialog

fields = ('Chave GCloud', 'Tamanho dos batches')

def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"0")
      row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
      lab.pack(side = LEFT)
      ent.pack(side = RIGHT, expand = YES, fill = X)
      entries[field] = ent
   return entries

root = Tk()
ents = makeform(root, fields)
root.bind('<Return>', (lambda event, e = ents: fetch(e)))

def file_opener():
   csv_file = filedialog.askopenfile(initialdir="/")
   print(csv_file)
   for i in csv_file:
      print(i)

def output():
    for k in ents:
        print(ents[k].get())
    root.quit()

b1 = Button(root, text ='Selecione o .csv de estabelecimentos', command=lambda:file_opener())
b1.pack(side = LEFT, padx = 5, pady = 5)
b2 = Button(root, text = 'Executar consultas', command = output)
b2.pack(side = LEFT, padx = 5, pady = 5)
b3 = Button(root, text = 'Sair', command = root.quit)
b3.pack(side = LEFT, padx = 5, pady = 5)
root.mainloop()