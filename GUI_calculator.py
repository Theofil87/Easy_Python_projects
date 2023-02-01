from tkinter import *

def szamol():
    szam1 = int(e1.get())
    szam2 = int(e2.get())
    operator = e3.get()
    if operator == "+":
        eredmeny = szam1 + szam2
    elif operator == "-":
        eredmeny = szam1 - szam2
    elif operator == "*":
        eredmeny = szam1 * szam2
    elif operator == "/":
        eredmeny = szam1 / szam2
    elif operator =="**":
        eredmeny = szam1 ** szam2
    else:
        eredmeny = "Érvénytelen művelet"
    e4.delete(0, END)
    e4.insert(0, eredmeny)

root = Tk()
root.title("Számológép")

l1 = Label(root, text="Szám 1:")
l2 = Label(root, text="Szám 2:")
l3 = Label(root, text="Művelet:")
l4 = Label(root, text="Eredmény:")

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)
l4.grid(row=3, column=0)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

gomb = Button(root, text="Számol", command=szamol)
gomb.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

root.mainloop()