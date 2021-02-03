
import top10
import aide
import gestiondesmots
import game
from tkinter import *
from tkinter import ttk


class acceuil:

    def __init__(self,player):
        self.window = Tk()
        self.player = player
    def openWindow(self):
        self.window.title("Acceuil")
        self.window.geometry("1024x768")
        self.window.minsize(1024, 768)
        self.window.maxsize(1024, 768)
       # self.window.iconbitmap("img/logo.ico")
        self.window.resizable(False, False)
        bg_acceuil = PhotoImage(file="img/acceuil.png")
        label_acceuil = Label(self.window, image=bg_acceuil)
        label_acceuil.place(x=0, y=0, relwidth=1, relheight=1)

        # Menu acceuil
        mainmenu = Menu(self.window)
        first_menu = Menu(mainmenu, tearoff=0)
        first_menu.add_command(label="Top 10", command=self.opentop10window)
        first_menu.add_command(label="Gestion des mots", command=self.opengestionmots)
        first_menu.add_command(label="Aide", command=self.openaidewindow)
        first_menu.add_command(label="Quitter", command=self.closeWindow)
        mainmenu.add_cascade(label="Menu", menu=first_menu)
        self.window.config(menu=mainmenu)

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
        acceuil_button = Button(frame_acceuilbuttonplay, borderwidth=0, text="Jouer", width=225, font=("Arial", 15),
                                bg="white",
                                fg="black", command=self.opengamewindow)
        acceuil_button.pack()
        acceuil_button = Button(frame_acceuilbuttontop10, borderwidth=0, text="Top 10", width=225, font=("Arial", 15),
                                bg="white", fg="black", command=self.opentop10window)
        acceuil_button.pack()
        acceuil_button = Button(frame_acceuilbuttongestionmot, borderwidth=0, text="Gestion des mots", width=225,
                                font=("Arial", 15), bg="white", fg="black", command=self.opengestionmots)
        acceuil_button.pack()
        acceuil_button = Button(frame_acceuilbuttonaide, borderwidth=0, text="Aide", width=225, font=("Arial", 15),
                                bg="white",
                                fg="black", command=self.openaidewindow)
        acceuil_button.pack()
        acceuil_button = Button(frame_acceuilbuttonquitter, borderwidth=0, text="Quitter", width=225,
                                font=("Arial", 15),
                                bg="white",
                                fg="black", command=self.closeWindow)
        acceuil_button.pack()

        # AFFICHAGE FRAME
        frame_acceuiltop.place(x=30, y=10, width=960, height=115)
        frame_acceuilbuttonplay.place(x=410, y=415, width=225, height=35)
        frame_acceuilbuttontop10.place(x=410, y=485, width=225, height=35)
        frame_acceuilbuttongestionmot.place(x=410, y=555, width=225, height=35)
        frame_acceuilbuttonaide.place(x=410, y=625, width=225, height=35)
        frame_acceuilpseudo.place(x=450, y=200, width=250)
        frame_acceuildifficulte.place(x=450, y=270, width=250)
        frame_acceuilbuttonquitter.place(x=790, y=670, width=70, height=35)

        self.window.mainloop()

    def closeWindow(self):
        self.window.destroy()

    def opengamewindow(self):
        self.closeWindow()
        game.Game().openWindow()

    def opentop10window(self):
        self.closeWindow()
        top10.Top10().openWindow()

    def openaidewindow(self):
        self.closeWindow()
        aide.Aide.openWindow()

    def opengestionmots(self):
        self.closeWindow()
        gestiondesmots.GestionMot.openWindow()


