from game import opengame
from top10 import opentop10
from aide import openaide
from gestiondesmots import opengestionmot
from tkinter import *
from tkinter import ttk
import xml.etree.ElementTree as ET

tree = ET.parse('joueur.xml')
myroot = tree.getroot()
cptnewjoueur = 0


# DEUX FONCTION

def two_funcs(*funcs):
    def two_funcs(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return two_funcs


class Acceuil:
    def __init__(self):
        self.window = Tk()

    def openWindow(self):
        self.window.title("Acceuil")
        self.window.geometry("1024x768")
        self.window.minsize(1024, 768)
        self.window.maxsize(1024, 768)
        self.window.iconbitmap("img/logo.ico")
        self.window.resizable(False, False)
        bg_acceuil = PhotoImage(file="img/acceuil.png")
        label_acceuil = Label(self.window, image=bg_acceuil)
        label_acceuil.place(x=0, y=0, relwidth=1, relheight=1)

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
            value = listedifficulte.get()
            return value

        def selectpseudo():
            pseudoplayer = pseudoEntry.get()
            return pseudoplayer

        listejoueur = []
        for x in myroot.findall('player'):
            nom = x.find('joueur').text
            diff = x.find("difficulte").text
            score = x.find("score").text
            listejoueur.append([])
            listejoueur[len(listejoueur) - 1].append(nom)
            listejoueur[len(listejoueur) - 1].append(diff)
            listejoueur[len(listejoueur) - 1].append(score)
        print(listejoueur)

        def creerjoueur():
            global cptnewjoueur
            listejoueur.append([])
            listejoueur[len(listejoueur) - 1].append(selectpseudo())
            listejoueur[len(listejoueur) - 1].append(selectdiff())
            listejoueur[len(listejoueur) - 1].append("0")
            new_field = ET.Element("PLAYER")
            print(listejoueur)
            for item in listejoueur:
                for i in range(0, 1):
                    groupe = ET.SubElement(new_field, "player")
                    ET.SubElement(groupe, "joueur").text = listejoueur[cptnewjoueur][0]
                    ET.SubElement(groupe, "difficulte").text = listejoueur[cptnewjoueur][1]
                    ET.SubElement(groupe, "score").text = listejoueur[cptnewjoueur][2]
                cptnewjoueur = cptnewjoueur + 1
            tree1 = ET.ElementTree(new_field)
            tree1.write('joueur.xml')

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
                                fg="black", command=self.openaidewindow)
        acceuil_button.pack()
        acceuil_button = Button(frame_acceuilbuttonquitter, borderwidth=0, text="Quitter", width=225,
                                font=("Arial", 15),
                                bg="white",
                                fg="black", command=self.closeWindow)
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

    def closeWindow(self):
        self.window.destroy()

    def opengamewindow(self):
        self.closeWindow()
        opengame()

    def opentop10window(self):
        self.closeWindow()
        opentop10()

    def openaidewindow(self):
        self.closeWindow()
        openaide()

    def opengestionmots(self):
        self.closeWindow()
        opengestionmot()

    def opentrans(self):
        self.closeWindow()
        opentrans()


main = Acceuil()
main.openWindow()
