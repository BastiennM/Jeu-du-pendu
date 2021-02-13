from tkinter import *
import xml.etree.ElementTree as ET
from hangman import HangMan
import dumper
import acceuil
import top10
import gestiondesmots
import aide

treemot = ET.parse('xml/mot.xml')
rootmot = treemot.getroot()


treejoueur = ET.parse('xml/joueur.xml')
rootjoueur = treejoueur.getroot()

# DECLARATION DES VARIABLES
end = False
cpt_perdu = 0
nro = 0


# DEUX FONCTION
def two_funcs(*funcs):
    def two_funcs(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return two_funcs


class Game:
    def __init__(self, rootwindow, joueur):
        self.window = Toplevel(rootwindow)
        self.rootwindow = rootwindow
        self.joueur = joueur
        self.hangman = HangMan(self.joueur.difficulte)

    def openWindow(self):
        self.window.title("Jeu du pendu")
        self.window.geometry("1024x768")
        self.window.minsize(1024, 768)
        self.window.maxsize(1024, 768)
        self.window.iconbitmap("img/logo.ico")
        self.window.resizable(False, False)
        bg_jeu = PhotoImage(file="img/jeupendu.png")
        label_jeu = Label(self.window, image=bg_jeu)
        label_jeu.place(x=0, y=0, relwidth=1, relheight=1)

        # FONCTION POINT BONUS / LIMITE DE COUP / ET AFFICHAGE SELON DIFFICULTE
        label_etape = []
        etape_img = []
        etape_label = []
        for i in range(0, self.hangman.nombressaimax - 1):
            dumper.dump(i)
            etape_img.append(PhotoImage(file="img/etape" + str(i + 1) + ".png"))
            dumper.dump(etape_img[i])
            etape_label.append(Label(self.window, image=etape_img[i], borderwidth=0))
            label_etape.append(etape_label[i])

        perdu = PhotoImage(file="img/defaite.png")
        label_perdu = Label(self.window, image=perdu, borderwidth=0, bg="white")
        label_etape.append(label_perdu)
        temps_ecoule = PhotoImage(file="img/hor-removebg-preview.png")
        label_temps_ecoule = Label(self.window, image=temps_ecoule, borderwidth=0, bg="white")
        label_etape.append(label_temps_ecoule)
        gagne = PhotoImage(file="img/victory.png")
        label_gagne = Label(self.window, image=gagne, borderwidth=0, bg="white")
        label_etape.append(label_gagne)

        # Menu Page de jeu
        pendumenu = Menu(self.window)
        first_menu = Menu(pendumenu, tearoff=0)
        first_menu.add_command(label="Quitter", command=self.window.destroy)
        first_menu.add_command(label="Acceuil", command=self.openacceuil)
        first_menu.add_command(label="Top 10", command=self.opentop10)
        first_menu.add_command(label="Aide", command=self.openaide)
        first_menu.add_command(label="Gestion des mots", command=self.opengestiondesmots)
        pendumenu.add_cascade(label="Menu", menu=first_menu)
        self.window.config(menu=pendumenu)

        # CREATION FRAME
        frame_topbanner = Frame(self.window, background="#ccccff")
        frame_timer = Frame(self.window, background="white")
        frame_dessin = Frame(self.window, background="white")
        frame_mot = Frame(self.window, background="white")
        frame_clavier1 = Frame(self.window, background="#ccccff")
        frame_clavier2 = Frame(self.window, background="#ccccff")

        # AFFICHAGE FRAME
        frame_topbanner.place(x=40, y=20, width=940, height=65)
        frame_timer.place(x=448, y=115, width=130, height=68)

        joueurliste = []
        for joueur_item in rootjoueur.findall('./player'):
            joueur_detail = {}
            for detail in joueur_item:
                joueur_detail[detail.tag] = detail.text.encode('UTF-8')
            joueurliste.append(joueur_detail)

        # AFFICHAGE PSEUDO
        label_pseudo = Label(frame_topbanner, text="", font=("Arial", 30), bg="#ccccff", fg="black")
        pseudoJeu = self.joueur.pseudo
        label_pseudo.config(text="A toi de jouer " + pseudoJeu + " !")
        label_pseudo.pack()

        # AFFICHAGE DIFFICULTE
        label_difficulte = Label(frame_topbanner, text="", font=("Arial", 10), bg="#ccccff", fg="black")
        label_difficulte.config(text="Difficulté : " + self.hangman.getdifficultetext())
        label_difficulte.pack()

        # LABEL TIMER
        timer = Label(frame_timer, text="", background="white")
        timer.pack()

        # FONCTION TIMER
        def decompte(count=120):
            global end
            timer.config(text=str(count))
            if count > 0:
                frame_timer.after(1000, decompte, count - 1, )
                btn_timer["state"] = DISABLED
            if count <= 0:
                if not end:
                    label_perduhorloge = Label(self.window, text="Temps écoulé, vous avez perdu !!",
                                               font=("Courrier", 15), bg="white")
                    label_perduhorloge.place(x=640, y=180)
                    end = True
                    lbl["text"] = "".join(self.hangman.motadecouvrir)
                    annonce["text"] = "Perdu !"
                    label_temps_ecoule.place(x=640, y=230)
                    affichescorefinal()
                    frame_clavier1.place_forget()
                    frame_clavier2.place_forget()
                    creerjoueurXML()

        def lancerjeu():
            frame_clavier1.place(x=80, y=570, width=900, height=70)
            frame_clavier2.place(x=196, y=650, width=800, height=70)
            frame_mot.place(x=23, y=160, width=390, height=330)

        # BOUTTON TIMER
        btn_timer = Button(self.window, text="Commencer", command=two_funcs(decompte, lancerjeu))
        btn_timer.place(x=475, y=150)

        # FONCTION MODIF LETTRE SI VRAI OU FAUX
        def maj_mot_en_progres(mot_en_progres, lettre, secret):
            n = len(secret)
            for i in range(n):
                if secret[i] == lettre:
                    mot_en_progres[i] = lettre
                    if mot_en_progres == list(secret):
                        annonce["text"] = "Gagné !"
                        label_gagne.place(x=700, y=210)

        # FONCTION GAGNE PERDU
        def score(lettre):
            global end
            if lettre not in self.hangman.motadecouvrir:
                self.hangman.nombresessai += 1
                label_etape[self.hangman.nombresessai - 1].place(x=610, y=210)
                if self.hangman.nombresessai == self.hangman.nombressaimax:
                    frame_clavier1.place_forget()
                    frame_clavier2.place_forget()
                    label_perdu.place(x=620, y=210)
                    lbl["text"] = "".join(self.hangman.motadecouvrir)
                    annonce["text"] = "Perdu !"
                    end = True
                    affichescorefinal()
                    creerjoueurXML()
            elif mot_en_progres == list(self.hangman.motadecouvrir):
                annonce["text"] = "Gagné !"
                label_gagne.place(x=670, y=210)
                end = True
                frame_clavier1.place_forget()
                frame_clavier2.place_forget()
                affichescorefinal()
                creerjoueurXML()
            return cpt_perdu

        # FONCTIONS RECUP LETTRE
        def choisir_lettre(event):
            if end:
                return
            mon_btn = event.widget
            lettre = mon_btn["text"]
            mon_btn["state"] = DISABLED
            maj_mot_en_progres(mot_en_progres, lettre, self.hangman.motadecouvrir)
            lbl["text"] = " ".join(mot_en_progres)
            score(lettre)

        # Création tiret vide selon longueur mot
        mot_en_progres = list("_" * self.hangman.longueurmot)
        stars = " ".join(mot_en_progres)

        # FONCTION SCORE FINAL
        def affichescorefinal():
            global end
            if end:
                labelscorefinal1 = Label(self.window, text="Votre score final est de :", font=("Times 15 bold", 30),
                                         bg="#ccccff", fg="black")
                labelscorefinal1.place(x=240, y=620)
                labelscorefinal2 = Label(self.window, text=self.hangman.calc_score(), font=("Times 15 bold", 30),
                                         bg="#ccccff", fg="black")
                labelscorefinal2.place(x=680, y=620)

        # AFFICHAGE DES LETTRES
        lbl = Label(frame_mot, text=stars, font=("Times 15 bold", 30), background="white", fg="black")
        lbl.place(x=80, y=240)

        # AFFICHAGE DEFAITE / VICTOIRE
        annonce = Label(frame_mot, width=8, font=("Times 15 bold", 25), background="white", fg="red")
        annonce.place(x=80, y=150)

        # CREATION ET AFFICHAGE CLAVIER
        ALPHA = "ABCDEFGHIJQLMNO"
        BETA = "PQRSTUVWXYZ"

        for a in ALPHA:
            btn = Button(frame_clavier1, text=a, width=4, height=3)
            btn.pack(side=LEFT, pady=10, padx=10)
            btn.bind("<Button-1>", choisir_lettre)

        for b in BETA:
            btn = Button(frame_clavier2, text=b, width=4, height=3)
            btn.pack(side=LEFT, pady=10, padx=10)
            btn.bind("<Button-1>", choisir_lettre)

        def creerjoueurXML():
            self.joueur.pseudo = pseudoJeu
            self.joueur.difficulte = self.hangman.getdifficultetext()
            self.joueur.score = self.hangman.calc_score()
            elementplayer = ET.Element('player')
            for key, val in self.joueur.__dict__.items():
                child = ET.Element(key)
                child.text = str(val)
                elementplayer.append(child)
            rootjoueur.append(elementplayer)
            treejoueur.write('xml/joueur.xml')

        self.window.mainloop()

    def openacceuil(self):
        self.window.destroy()
        acceuil.Acceuil(self.rootwindow, self.joueur).openWindow()

    def opentop10(self):
        self.window.destroy()
        top10.Top10(self.rootwindow, self.joueur).openWindow()

    def openaide(self):
        self.window.destroy()
        aide.Aide(self.rootwindow, self.joueur).openWindow()

    def opengestiondesmots(self):
        self.window.destroy()
        gestiondesmots.Gestionmot(self.rootwindow, self.joueur).openWindow()
