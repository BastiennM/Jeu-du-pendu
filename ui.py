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
    first_menu.add_command(label="Top 10", command=show_top10)
    first_menu.add_command(label="Gestion des mots", command=two_funcs(jeu_window.destroy, acceuil.deiconify))
    first_menu.add_command(label="Aide", command=show_aide)
    first_menu.add_command(label="Quitter", command=quitter)
    pendumenu.add_cascade(label="Menu", menu=first_menu)
    jeu_window.config(menu=pendumenu)


# <======================================================== PAGE JEU ========================================================>
# <======================================================== PAGE TOP10 ========================================================>
def show_top10():
    top10_window = tkinter.Toplevel(acceuil)
    top10_window.title("Top 10")
    top10_window.geometry("1080x720")
    top10_window.minsize(480, 360)
    top10_window.iconbitmap("img/logo.ico")
    top10_window.config(background='#FF5733')
    acceuil.withdraw()

    # Menu Page de jeu
    pendumenu = tkinter.Menu(top10_window)
    first_menu = tkinter.Menu(pendumenu, tearoff=0)
    first_menu.add_command(label="Acceuil", command=two_funcs(top10_window.destroy, acceuil.deiconify))
    first_menu.add_command(label="Gestion des mots", command=two_funcs(top10_window.destroy, show_gestion))
    first_menu.add_command(label="Aide", command=two_funcs(top10_window.destroy, show_aide))
    first_menu.add_command(label="Quitter", command=quitter)
    pendumenu.add_cascade(label="Menu", menu=first_menu)
    top10_window.config(menu=pendumenu)


# <======================================================== PAGE TOP10 ========================================================>
# <======================================================== PAGE GESTION DES MOTS ========================================================>
def show_gestion():
    gestion_window = tkinter.Toplevel(acceuil)
    gestion_window.title("Gestion des mots")
    gestion_window.geometry("1080x720")
    gestion_window.minsize(480, 360)
    gestion_window.iconbitmap("img/logo.ico")
    gestion_window.config(background='#FF5733')
    acceuil.withdraw()

    # Menu Page de jeu
    pendumenu = tkinter.Menu(gestion_window)
    first_menu = tkinter.Menu(pendumenu, tearoff=0)
    first_menu.add_command(label="Acceuil", command=two_funcs(gestion_window.destroy, acceuil.deiconify))
    first_menu.add_command(label="Top 10", command=two_funcs(gestion_window.destroy, show_top10))
    first_menu.add_command(label="Aide", command=two_funcs(gestion_window.destroy, show_aide))
    first_menu.add_command(label="Quitter", command=quitter)
    pendumenu.add_cascade(label="Menu", menu=first_menu)
    gestion_window.config(menu=pendumenu)


# <======================================================== PAGE GESTION DES MOTS ========================================================>
# <======================================================== PAGE AIDE ========================================================>
def show_aide():
    aide_window = tkinter.Toplevel(acceuil)
    aide_window.title("Aide")
    aide_window.geometry("1080x720")
    aide_window.minsize(480, 360)
    aide_window.iconbitmap("img/logo.ico")
    aide_window.config(background='#FF5733')
    acceuil.withdraw()

    # Menu Page de jeu
    pendumenu = tkinter.Menu(aide_window)
    first_menu = tkinter.Menu(pendumenu, tearoff=0)
    first_menu.add_command(label="Acceuil", command=two_funcs(aide_window.destroy, acceuil.deiconify))
    first_menu.add_command(label="Top 10", command=two_funcs(aide_window.destroy, show_top10))
    first_menu.add_command(label="Gestion des mots", command=two_funcs(aide_window.destroy, show_gestion))
    first_menu.add_command(label="Quitter", command=quitter)
    pendumenu.add_cascade(label="Menu", menu=first_menu)
    aide_window.config(menu=pendumenu)


# <======================================================== PAGE AIDE ========================================================>
# <======================================================== FONCTIONS ========================================================>

# <======================================================== PAGE ACCEUIL ========================================================>
acceuil = Tk()
acceuil.title("Page d'accueil")
acceuil.geometry("1920x1080")
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
acceuil.config(menu=mainmenu)

# CRÉATION FRAME
frame = Frame(acceuil, bg='#ff5733')

# TEXTE
label_title = Label(frame, text="Bienvenue sur le jeu du", font=("Courrier", 30), bg="#FF5733", fg="white")
label_title.pack()
label_subtitle = Label(frame, text="PENDU", font=("Courrier", 40), bg="#FF5733", fg="white")
label_subtitle.pack()

# BUTTONS
menu_button = Button(frame, text="Jouer", height="2", font=("Arial", 15), bg="white", fg="#FF5733", command=show_jeu)
menu_button.pack(pady="15", fill=X)
menu_button = Button(frame, text="Top 10", height="2", font=("Arial", 15), bg="white", fg="#FF5733", command=show_top10)
menu_button.pack(pady="15", fill=X)
menu_button = Button(frame, text="Gestion des mots", height="2", font=("Arial", 15), bg="white", fg="#FF5733",command=show_gestion)
menu_button.pack(pady="15", fill=X)
menu_button = Button(frame, text="Aide", height="2", font=("Arial", 15), bg="white", fg="#FF5733", command=show_aide)
menu_button.pack(pady="15", fill=X)
menu_button = Button(frame, text="Quitter", height="2", font=("Arial", 15), bg="white", fg="#FF5733", command=quitter)
menu_button.pack(pady="15", fill=X)

# CANVAS

# canvas = Canvas(width=400, height=250, bg="blue")
# canvas.pack(pady=20)
#
# photoacceuil = PhotoImage(file="img/acceuil.png")
# canvas.create_image(200, 25, image=photoacceuil, anchor=N)

# AFFICHAGE FRAME
frame.pack(expand=YES)
# AFFICHAGE PAGE ACCEUIL
acceuil.mainloop()
