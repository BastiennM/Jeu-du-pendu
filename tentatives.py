import tkinter as tk
import time
import random

# on créeeeeeez la fenetre tkinter
color = "white"
fenetre = tk.Tk()
fenetre.geometry("600x300")
fenetre.title("Jeu du juste prix")
fenetre.resizable(width=False, height=False)
fenetre.config(bg=color)

nombre_hasard = random.randint(1, 100)

# compteur tentatives
tentatives = 25

def essai(event=None):

    global entree_proposition, nombre_hasard, tentatives, tentativestxtvar, infovar

    # recolter la proposition
    proposition = entree_proposition.get()

    # verification
    if proposition.isdigit():
        # transformation de proposition en entier
        # cast
        nombre_proposition = int(proposition)

        # verifier si le nombre proposition est plus petit que le nombre à trouver
        if nombre_proposition < nombre_hasard:
            infovar.set("C'est plus")
        elif nombre_proposition > nombre_hasard:
            infovar.set("C'est moins")
        else:
            infovar.set("C'est gagné")
            time.sleep(2)
            fenetre.destroy()
            quit()

        tentatives -= 1 # enlever 1 tentative
        tentativestxtvar.set(f"{tentatives} tentatives")

    else:
        infovar.set("Tu dois entrer un nombre")

# ajouter une variable stockant le nombre de tentatives
tentativestxtvar = tk.StringVar()
tentativestxtvar.set("15 tentatives")

# ajouter nombre de tentatives
tentativestxt = tk.Label(fenetre, textvariable=tentativestxtvar, bg=color)
tentativestxt.place(x=500, y=20)

# ajouter un intitulé pour afficher des informations
infovar = tk.StringVar()
infovar.set("Bonne chance...")
info = tk.Label(fenetre, textvariable=infovar, bg=color)
info.place(x=250, y=220)

# boite
frame = tk.Frame(fenetre)
frame.pack(expand=True)

# ajouter une entrée pour ecrire
entree_proposition = tk.Entry(frame)
entree_proposition.bind('<Return>', essai)
entree_proposition.focus()
entree_proposition.pack()

# afficher
fenetre.mainloop()

