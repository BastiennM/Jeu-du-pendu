from tkinter import *
import tkinter


# <======================================================== FONCTIONS ========================================================>
def two_funcs(*funcs):
    def two_funcs(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return two_funcs


def quitter():
    acceuil.quit()

# <======================================================== PAGE JEU ========================================================>
def show_jeu():
    jeu_window = tkinter.Toplevel(acceuil)
    jeu_window.title("Jeu du pendu")
    jeu_window.geometry("1080x720")
    jeu_window.minsize(480, 360)
    jeu_window.iconbitmap("img/logo.ico")
    jeu_window.config(background='#FF5733')
    acceuil.withdraw()

    # Menu Page de jeu

    pendumenu = tkinter.Menu(jeu_window)
    first_menu = tkinter.Menu(pendumenu, tearoff=0)
    first_menu.add_command(label="Acceuil", command=two_funcs(jeu_window.destroy, acceuil.deiconify))
    first_menu.add_command(label="Top 10")
    first_menu.add_command(label="Gestion des mots")
    first_menu.add_command(label="Aide", command=show_jeu)
    first_menu.add_command(label="Quitter", command=quitter)

    pendumenu.add_cascade(label="Menu", menu=first_menu)

    # boucle principale
    jeu_window.config(menu=pendumenu)
# <======================================================== PAGE JEU ========================================================>


# <======================================================== FONCTIONS ========================================================>

# <======================================================== PAGE ACCEUIL ========================================================>
acceuil = Tk()
acceuil.title("Page d'accueil")
acceuil.geometry("1080x720")
acceuil.minsize(480, 360)
acceuil.iconbitmap("img/logo.ico")
acceuil.config(background='#FF5733')

# Menu acceuil
mainmenu = tkinter.Menu(acceuil)
first_menu = tkinter.Menu(mainmenu, tearoff=0)
first_menu.add_command(label="Top 10")
first_menu.add_command(label="Gestion des mots")
first_menu.add_command(label="Aide", command=show_jeu)
first_menu.add_command(label="Quitter", command=quitter)
mainmenu.add_cascade(label="Menu", menu=first_menu)
# boucle principale
acceuil.config(menu=mainmenu)

# CRÉATION FRAME
frame = Frame(acceuil, bg='#ff5733')

# TEXTE
label_title = Label(frame, text="Bienvenue sur le jeu du", font=("Courrier", 30), bg="#FF5733", fg="white")
label_title.pack(expand=YES)
label_subtitle = Label(frame, text="PENDU", font=("Courrier", 40), bg="#FF5733", fg="white")
label_subtitle.pack(expand=YES)

# BUTTONS
menu_button = Button(frame, text="Jouer", height="2", font=("Arial", 15), bg="white", fg="#FF5733", command=show_jeu)
menu_button.pack(pady="15", fill=X)
menu_button = Button(frame, text="Top 10", height="2", font=("Arial", 15), bg="white", fg="#FF5733")
menu_button.pack(pady="15", fill=X)
menu_button = Button(frame, text="Gestion des mots", height="2", font=("Arial", 15), bg="white", fg="#FF5733")
menu_button.pack(pady="15", fill=X)
menu_button = Button(frame, text="Aide", height="2", font=("Arial", 15), bg="white", fg="#FF5733")
menu_button.pack(pady="15", fill=X)
menu_button = Button(frame, text="Quitter", height="2", font=("Arial", 15), bg="white", fg="#FF5733", command=quitter)
menu_button.pack(pady="15", fill=X)

# AFFICHAGE FRAME
frame.pack(expand=YES)
# AFFICHAGE PAGE ACCEUIL
acceuil.mainloop()
