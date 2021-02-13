import game
import top10
import aide
import gestiondesmots
from tkinter import *
from tkinter import ttk
import xml.etree.ElementTree as ET


tree = ET.parse('xml/joueur.xml')
myroot = tree.getroot()
cptnewjoueur = 0


# DEUX FONCTION

def two_funcs(*funcs):
    def two_funcs(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return two_funcs


class Acceuil:
    def __init__(self,rootwindow,joueur):
        self.rootwindow=rootwindow
        self.window = Toplevel(rootwindow)
        self.joueur = joueur

    def openWindow(self):
        bg_acceuil = PhotoImage(file="img/acceuil.png")
        label_acceuil = Label(self.window, image=bg_acceuil)
        label_acceuil.place(x=0, y=0, relwidth=1, relheight=1)
        self.window.title("Acceuil")
        self.window.geometry("1024x768")
        self.window.minsize(1024, 768)
        self.window.maxsize(1024, 768)
        self.window.iconbitmap("img/logo.ico")
        self.window.resizable(False, False)


        # CRÉATION FRAME
        frame_acceuilpseudo = Frame(self.window, background="white")
        frame_acceuildifficulte = Frame(self.window, background="white")
        frame_acceuiltop = Frame(self.window, background="#ccccff")
        frame_acceuilbuttonplay = Frame(self.window)
        frame_acceuilbuttontop10 = Frame(self.window)
        frame_acceuilbuttongestionmot = Frame(self.window)
        frame_acceuilbuttonaide = Frame(self.window)
        frame_acceuilbuttonquitter = Frame(self.window)

        # TEXTE
        label_title = Label(frame_acceuiltop, text="Bienvenue sur le jeu du", font=("Arial", 30), bg="#ccccff",
                            fg="black")
        label_title.pack()
        label_subtitle = Label(frame_acceuiltop, text="PENDU", font=("Courrier", 40), bg="#ccccff", fg="black")
        label_subtitle.pack()

        def toggle_state(*_):
            if pseudoEntry.var.get():
                acceuil_buttonplay['state'] = 'normal'
            else:
                acceuil_buttonplay['state'] = 'disabled'

        # ZONE DE SAISIE PSEDUO

        pseudoEntry = Entry(frame_acceuilpseudo, width=50, background=None)
        pseudoEntry.pack()
        pseudoEntry.var = StringVar()
        pseudoEntry['textvariable'] = pseudoEntry.var
        pseudoEntry.var.trace_add('write', toggle_state)

        # CHOIX DE DIFFICULTÉ
        optionsdifficulte = ["Facile", "Normal", "Difficile"]
        listedifficulte = ttk.Combobox(frame_acceuildifficulte, values=optionsdifficulte, width=34,
                                       justify="center")
        listedifficulte.current(0)
        listedifficulte.pack()

        def selectdiff():
            value = listedifficulte.current()
            return value

        def selectpseudo():
            pseudoplayer = pseudoEntry.get()
            return pseudoplayer

        joueurliste = []
        for joueur_item in myroot.findall('./player'):
            joueur_detail = {}
            for detail in joueur_item:
                joueur_detail[detail.tag] = detail.text.encode('UTF-8')
            joueurliste.append(joueur_detail)

        def creerjoueur():
            self.joueur.pseudo = selectpseudo()
            self.joueur.difficulte = selectdiff()
            self.joueur.score = 0
            print(self.joueur)

        # BUTTONS
        acceuil_buttonplay = Button(frame_acceuilbuttonplay, borderwidth=0, text="Jouer", state='disabled', width=225,
                                    font=("Arial", 15),
                                    bg="white",
                                    fg="black", command=two_funcs(creerjoueur, self.opengamewindow))
        acceuil_buttonplay.pack()
        acceuil_button = Button(frame_acceuilbuttontop10, borderwidth=0, text="Top 10", width=225, font=("Arial", 15),
                                bg="white", fg="black", command=self.opentop10window)
        acceuil_button.pack()
        acceuil_button = Button(frame_acceuilbuttongestionmot, borderwidth=0, text="Gestion des mots", width=225,
                                font=("Arial", 15), bg="white", fg="black", command=self.opengestionmots)
        acceuil_button.pack()
        acceuil_button = Button(frame_acceuilbuttonaide, borderwidth=0, text="Aide", width=225, font=("Arial", 15),
                                bg="white",
                                fg="black")
        acceuil_button.pack()
        acceuil_button = Button(frame_acceuilbuttonquitter, borderwidth=0, text="Quitter", width=225,
                                font=("Arial", 15),
                                bg="white",
                                fg="black", command=self.window.destroy)
        acceuil_button.pack()

        # AFFICHAGE FRAME
        frame_acceuiltop.place(x=30, y=20, width=960, height=115)
        frame_acceuilbuttonplay.place(x=410, y=425, width=225, height=35)
        frame_acceuilbuttontop10.place(x=410, y=495, width=225, height=35)
        frame_acceuilbuttongestionmot.place(x=410, y=565, width=225, height=35)
        frame_acceuilbuttonaide.place(x=410, y=635, width=230, height=30)
        frame_acceuilpseudo.place(x=450, y=210, width=250)
        frame_acceuildifficulte.place(x=450, y=280, width=250)
        frame_acceuilbuttonquitter.place(x=790, y=680, width=70, height=35)

        self.window.mainloop()

    def opengamewindow(self):
        self.window.destroy()
        game.Game(self.rootwindow,self.joueur).openWindow()

    def opentop10window(self):
        self.window.destroy()
        top10.Top10(self.rootwindow, self.joueur).openWindow()

    def openaidewindow(self):
        self.window.destroy()
        aide.Aide(self.rootwindow, self.joueur).openWindow()

    def opengestionmots(self):
        self.window.destroy()
        gestiondesmots.Gestionmot(self.rootwindow,self.joueur).openWindow()
