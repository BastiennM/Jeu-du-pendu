# coding=utf-8
from tkinter import *
from functools import partial

# creer une première fenetre
fenetre = Tk()

# personnaliser cette fenetre
fenetre.title("Page d'accueil")
fenetre.geometry("1080x720")
fenetre.minsize(480, 360)
fenetre.iconbitmap("logo.ico")
fenetre.config(background='#FF5733')

# Création du Frame 1
frame1 = LabelFrame(fenetre, height=70, width=1060)
frame1.place(x=20, y=20)
frame1.grid(row=0, column=0, padx=10, pady=10)

# Création des sous widgets du 1er Frame
tvaFrame = LabelFrame(frame1, text='TVA', borderwidth=2, width=120, height=100).place(x=30, y=30)
value = IntVar(fenetre, '5.50%')

# Création du Frame 2
frame2 = LabelFrame(fenetre, height=300, width=200)
frame2.place(x=20, y=20)
frame2.grid(row=1, column=0, padx=10, pady=10)

fenetre.mainloop()
