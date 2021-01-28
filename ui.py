from tkinter import *
import tkinter
from tkinter import ttk


# <======================================================== FONCTIONS ========================================================>
# DEUX FONCTION
def two_funcs(*funcs):
    def two_funcs(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return two_funcs


# FONCTION QUITTER
def quitter():
    acceuil.quit()


# <======================================================= PAGE JEU ========================================================>

def show_jeu():
    jeu_window = tkinter.Toplevel(acceuil)
    jeu_window.title("Jeu du pendu")
    jeu_window.geometry("1024x768")
    jeu_window.minsize(1024, 768)
    jeu_window.maxsize(1024, 768)
    jeu_window.iconbitmap("img/logo.ico")
    jeu_window.resizable(False, False)
    label_jeu = Label(jeu_window, image=bg_jeu)
    label_jeu.place(x=0, y=0, relwidth=1, relheight=1)
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

    # CREATION FRAME
    frame_topbanner = Frame(jeu_window, background="#ccccff")
    frame_timer = Frame(jeu_window, background="white")
    frame_dessin = Frame(jeu_window, background="white")
    frame_mot = Frame(jeu_window, background="white")
    frame_clavier1 = Frame(jeu_window, background="#ccccff")
    frame_clavier2 = Frame(jeu_window, background="#ccccff")


    # AFFICHAGE FRAME
    frame_topbanner.place(x=40, y=20, width=940, height=65)
    frame_timer.place(x=448, y=115, width=130, height=68)
    frame_mot.place(x=23, y=160, width=390, height=330)
    frame_dessin.place(x=610, y=160, width=390, height=330)
    frame_clavier1.place(x=80, y=570, width=900, height=70)
    frame_clavier2.place(x=196, y=650, width=800, height=70)

    # AFFICHAGE PSEUDO
    label_pseudo = Label(frame_topbanner, text="", font=("Arial", 30), bg="#ccccff", fg="black")
    pseudoJeu = pseudoEntry.get()
    label_pseudo.config(text="A toi de jouer " + pseudoJeu + " !")
    label_pseudo.pack()

    # AFFICHAGE DIFFICULTE
    label_difficulte = Label(frame_topbanner, text="", font=("Arial", 10), bg="#ccccff", fg="black")
    modeJeu = listedifficulte.get()
    label_difficulte.config(text="Difficulté : " + modeJeu)
    label_difficulte.pack()

    # LABEL TIMER
    timer = Label(frame_timer, text="")
    timer.pack()

    # FONCTION TIMER
    def decompte(count=120):
        timer.config(text=str(count))
        if count > 0:
            frame_timer.after(1000, decompte, count - 1, )
        if count <= 0:
            timer.config(text="Temps écoulé, vous avez perdu !!")
        pts = 50
        if count == 90:
            pts = pts - 10
            print("Il vous reste", pts, "points")
        pts = pts - 10
        if count == 60:
            pts = pts - 10
            print("Il vous reste", pts, "points")
        pts = pts - 20
        if count == 30:
            pts = pts - 10
            print("Il vous reste", pts, "points")

    # BOUTTON TIMER
    btn_timer = Button(frame_timer, text="Commencer", command=decompte)
    btn_timer.pack()

    #FONCTIONS RECUP LETTRE
    def choisir_lettre(event):
        mon_btn = event.widget
        texte = mon_btn["text"]
        print("clic bouton : " + texte)

    #AFFICHAGE MASQUÉ
    lbl = Label(frame_mot, text="_ _ _ _ _ _ _ _ _", font="Times 15 bold")
    lbl.pack(padx=20, pady=20)

    #CREATION ET AFFICHAGE CLAVIER
    ALPHA = "ABCDEFGHIJQLMNO"
    BETA = "PQRSTUVWXYZ"
    for a in ALPHA:
        btn = Button(frame_clavier1, text=a,width=4, height=3)
        btn.pack(side=LEFT, pady=10, padx=10)
        btn.bind("<Button-1>", choisir_lettre)
    for b in BETA:
        btn = Button(frame_clavier2, text=b, width=4, height=3)
        btn.pack(side=LEFT, pady=10, padx=10)
        btn.bind("<Button-1>", choisir_lettre)


# <======================================================== PAGE JEU ========================================================>
# <======================================================== PAGE TOP10 ========================================================>
def show_top10():
    top10_window = tkinter.Toplevel(acceuil)
    top10_window.title("Top 10")
    top10_window.geometry("1080x720")
    top10_window.minsize(480, 360)
    top10_window.iconbitmap("img/logo.ico")
    top10_window.config(background='#f9791e')
    acceuil.withdraw()

    # Menu Page de top 10
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
    gestion_window.config(background=' #f9791e')
    acceuil.withdraw()

    # Menu Page de gestions de mots
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
    aide_window.config(background='#f9791e')
    acceuil.withdraw()

    # Menu Page aide
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
acceuil.geometry("1024x768")
acceuil.minsize(1024, 768)
acceuil.maxsize(1024, 768)
acceuil.iconbitmap("img/logo.ico")
acceuil.resizable(False, False)
bg_acceuil = PhotoImage(file="img/acceuil.png")
bg_jeu = PhotoImage(file="img/jeupendu.png")
label_acceuil = Label(acceuil, image=bg_acceuil)
label_acceuil.place(x=0, y=0, relwidth=1, relheight=1)

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
frame_acceuilpseudo = Frame(acceuil, background="white")
frame_acceuildifficulte = Frame(acceuil, background="white")
frame_acceuiltop = Frame(acceuil, background="#ccccff")
frame_acceuilbuttonplay = Frame(acceuil)
frame_acceuilbuttontop10 = Frame(acceuil)
frame_acceuilbuttongestionmot = Frame(acceuil)
frame_acceuilbuttonaide = Frame(acceuil)

# TEXTE
label_title = Label(frame_acceuiltop, text="Bienvenue sur le jeu du", font=("Arial", 30), bg="#ccccff", fg="black")
label_title.pack()
label_subtitle = Label(frame_acceuiltop, text="PENDU", font=("Courrier", 40), bg="#ccccff", fg="black")
label_subtitle.pack()

# ZONE DE SAISIE PSEDUO

pseudoEntry = Entry(frame_acceuilpseudo, width=50, background=None)
pseudoEntry.pack()

# CHOIX DE DIFFICULTÉ
optionsdifficulte = ["Facile", "Normal", "Difficile"]
listedifficulte = ttk.Combobox(frame_acceuildifficulte, values=optionsdifficulte, background=None, width=34,
                               justify="center")
listedifficulte.current(0)
listedifficulte.pack()

# BUTTONS
acceuil_button = Button(frame_acceuilbuttonplay, borderwidth=0, text="Jouer", width=225, font=("Arial", 15), bg="white",
                        fg="black", command=show_jeu)
acceuil_button.pack()
acceuil_button = Button(frame_acceuilbuttontop10, borderwidth=0, text="Top 10", width=225, font=("Arial", 15),
                        bg="white", fg="black", command=show_top10)
acceuil_button.pack()
acceuil_button = Button(frame_acceuilbuttongestionmot, borderwidth=0, text="Gestion des mots", width=225,
                        font=("Arial", 15), bg="white", fg="black", command=show_gestion)
acceuil_button.pack()
acceuil_button = Button(frame_acceuilbuttonaide, borderwidth=0, text="Aide", width=225, font=("Arial", 15), bg="white",
                        fg="black", command=show_aide)
acceuil_button.pack()
acceuil_button = Button(frame_acceuiltop, borderwidth=0, text="Quitter", width=225, font=("Arial", 15), bg="white",
                        fg="black", command=quitter)
acceuil_button.pack()

# AFFICHAGE FRAME
frame_acceuiltop.place(x=30, y=10, width=960, height=115)
frame_acceuilbuttonplay.place(x=410, y=415, width=225, height=35)
frame_acceuilbuttontop10.place(x=410, y=485, width=225, height=35)
frame_acceuilbuttongestionmot.place(x=410, y=555, width=225, height=35)
frame_acceuilbuttonaide.place(x=410, y=625, width=225, height=35)
frame_acceuilpseudo.place(x=450, y=200, width=250)
frame_acceuildifficulte.place(x=450, y=270, width=250)

# AFFICHAGE PAGE ACCEUIL
acceuil.mainloop()
