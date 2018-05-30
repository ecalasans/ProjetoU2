from Tkinter import *

principal = Tk()

principal.title("Projeto U2")
principal.geometry("200x100")

v = IntVar()

Radiobutton(principal, text = "Prolog", variable = v, value = 1).pack()
Radiobutton(principal, text = "Fuzzy", variable = v, value = 2).pack()

Button(principal, text = "Iniciar").pack(pady = 10)



principal.mainloop()

