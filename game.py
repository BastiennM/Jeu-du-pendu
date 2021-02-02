from tkinter import *
from top10 import opentop10
from aide import openaide
from gestiondesmots import opengestionmot

# DECLARATION DES VARIABLES POUR LA FONCTION SCORE
limite_perdu = 5
end = False
cpt_perdu = 0


# DEUX FONCTION
def two_funcs(*funcs):
    def two_funcs(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return two_funcs


def opengame():
    class Game:
        def __init__(self):
            self.window = Tk()

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

            # Menu Page de jeu
            pendumenu = Menu(self.window)
            first_menu = Menu(pendumenu, tearoff=0)
            first_menu.add_command(label="Acceuil")
            first_menu.add_command(label="Top 10", command=opentop10)
            first_menu.add_command(label="Gestion des mots", command=two_funcs(self.window.destroy, opengestionmot))
            first_menu.add_command(label="Aide", command=openaide)
            first_menu.add_command(label="Quitter", command=self.window.destroy)
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
            frame_mot.place(x=23, y=160, width=390, height=330)
            frame_dessin.place(x=610, y=160, width=390, height=330)
            frame_clavier1.place(x=80, y=570, width=900, height=70)
            frame_clavier2.place(x=196, y=650, width=800, height=70)

            # # AFFICHAGE PSEUDO
            # label_pseudo = Label(frame_topbanner, text="", font=("Arial", 30), bg="#ccccff", fg="black")
            # pseudoJeu = pseudoEntry.get()
            # label_pseudo.config(text="A toi de jouer " + pseudoJeu + " !")
            # label_pseudo.pack()

            # AFFICHAGE DIFFICULTE
            # label_difficulte = Label(frame_topbanner, text="", font=("Arial", 10), bg="#ccccff", fg="black")
            # modeJeu = listedifficulte.get()
            # label_difficulte.config(text="Difficulté : " + modeJeu)
            # label_difficulte.pack()

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

            # FONCTION MODIF LETTRE SI VRAI OU FAUX
            def maj_mot_en_progres(mot_en_progres, lettre, secret):
                n = len(secret)
                for i in range(n):
                    if secret[i] == lettre:
                        mot_en_progres[i] = lettre
                        if mot_en_progres == list(secret):
                            annonce["text"] = "Gagné !"

            # FONCTION SCORE
            def score(lettre):
                global cpt_perdu, end
                if lettre not in secret:
                    cpt_perdu += 1
                    print(cpt_perdu)
                    if cpt_perdu >= limite_perdu:
                        annonce["text"] = "Perdu !"
                        end = True
                elif mot_en_progres == list(secret):
                    annonce["text"] = "Gagné !"
                    end = True

            # FONCTIONS RECUP LETTRE
            def choisir_lettre(event):
                mon_btn = event.widget
                lettre = mon_btn["text"]
                maj_mot_en_progres(mot_en_progres, lettre, secret)
                lbl["text"] = " ".join(mot_en_progres)
                score(lettre)

            # MOT
            secret = "SAPINS"
            longsecret = len(secret)
            mot_en_progres = list("_" * longsecret)
            stars = " ".join(mot_en_progres)

            # AFFICHAGE DES LETTRES
            lbl = Label(frame_mot, text=stars, font="Times 15 bold")
            lbl.pack(padx=20, pady=20)

            # AFFICHAGE DEFAITE / VICTOIRE
            annonce = Label(frame_mot, width=8, font="Times 15 bold")
            annonce.pack(padx=5, pady=5)

            # CREATION ET AFFICHAGE CLAVIER => Jouer avec le style du bouton (relief) + la couleur lorsque il est cliqué (présent ou non dans le mot)
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
            self.window.mainloop()

    main = Game()
    main.openWindow()
