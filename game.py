from tkinter import *
import random
import xml.etree.ElementTree as ET

treemot = ET.parse('mot.xml')
rootmot = treemot.getroot()

treejoueur = ET.parse('joueur.xml')
rootjoueur = treejoueur.getroot()

# DECLARATION DES VARIABLES
limite_perdu = 11
end = False
cpt_perdu = 0
nro = 0
diff = "facile"


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

            # ETAPES PENDU
            etape1 = PhotoImage(file="img/etape1.png")
            label_etape1 = Label(self.window, image=etape1, borderwidth=0)
            etape2 = PhotoImage(file="img/etape2.png")
            label_etape2 = Label(self.window, image=etape2, borderwidth=0)
            etape3 = PhotoImage(file="img/etape3.png")
            label_etape3 = Label(self.window, image=etape3, borderwidth=0)
            etape4 = PhotoImage(file="img/etape4.png")
            label_etape4 = Label(self.window, image=etape4, borderwidth=0)
            etape5 = PhotoImage(file="img/etape5.png")
            label_etape5 = Label(self.window, image=etape5, borderwidth=0)
            etape6 = PhotoImage(file="img/etape6.png")
            label_etape6 = Label(self.window, image=etape6, borderwidth=0)
            etape7 = PhotoImage(file="img/etape7.png")
            label_etape7 = Label(self.window, image=etape7, borderwidth=0)
            etape8 = PhotoImage(file="img/etape8.png")
            label_etape8 = Label(self.window, image=etape8, borderwidth=0)
            etape9 = PhotoImage(file="img/etape9.png")
            label_etape9 = Label(self.window, image=etape9, borderwidth=0)
            etape10 = PhotoImage(file="img/etape10.png")
            label_etape10 = Label(self.window, image=etape10, borderwidth=0)
            etape11 = PhotoImage(file="img/etape11.png")
            label_etape11 = Label(self.window, image=etape11, borderwidth=0)
            perdu = PhotoImage(file="img/hor-removebg-preview.png")
            label_perdu = Label(self.window, image=perdu, borderwidth=0, bg="white")
            gagne = PhotoImage(file="img/victory.png")
            label_gagne = Label(self.window, image=gagne, borderwidth=0, bg="white")
            label_etape = [label_etape1, label_etape2, label_etape3, label_etape4, label_etape5, label_etape6,
                           label_etape7, label_etape8, label_etape9, label_etape10, label_etape11, label_perdu,
                           label_gagne]

            # AFFICHAGE FRAME
            frame_topbanner.place(x=40, y=20, width=940, height=65)
            frame_timer.place(x=448, y=115, width=130, height=68)

            listejoueur = []

            for x in rootjoueur.findall('player'):
                nom = x.find('joueur').text
                diff = x.find("difficulte").text
                score = x.find("score").text
                listejoueur.append([])
                listejoueur[len(listejoueur) - 1].append(nom)
                listejoueur[len(listejoueur) - 1].append(diff)
                listejoueur[len(listejoueur) - 1].append(score)
            print(listejoueur)

            # AFFICHAGE PSEUDO
            # label_pseudo = Label(frame_topbanner, text="", font=("Arial", 30), bg="#ccccff", fg="black")
            pseudoJeu = listejoueur[len(listejoueur) - 1][0]
            # print("listepourjeu", pseudoJeu)
            # label_pseudo.config(text="A toi de jouer " + pseudoJeu + " !")
            # label_pseudo.pack()

            # AFFICHAGE DIFFICULTE
            # label_difficulte = Label(frame_topbanner, text="", font=("Arial", 10), bg="#ccccff", fg="black")
            # modeJeu = listedifficulte.get()
            # label_difficulte.config(text="Difficulté : " + modeJeu)
            # label_difficulte.pack()

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
                        lbl["text"] = "".join(secret)
                        annonce["text"] = "Perdu !"
                        label_etape[11].place(x=640, y=230)
                        scorefinal()
                        frame_clavier1.place_forget()
                        frame_clavier2.place_forget()

            def lancerjeu():
                frame_clavier1.place(x=80, y=570, width=900, height=70)
                frame_clavier2.place(x=196, y=650, width=800, height=70)
                frame_mot.place(x=23, y=160, width=390, height=330)
                frame_dessin.place(x=610, y=160, width=390, height=330)

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
                            label_etape[12].place(x=700, y=210)

            # FONCTION GAGNE PERDU
            def score(lettre):
                global cpt_perdu, end
                if lettre not in secret:
                    cpt_perdu += 1
                    label_etape[cpt_perdu - 1].place(x=610, y=210)
                    if cpt_perdu == limite_perdu:
                        frame_clavier1.place_forget()
                        frame_clavier2.place_forget()
                        label_etape[11].place(x=670, y=210)
                        lbl["text"] = "".join(secret)
                        annonce["text"] = "Perdu !"
                        end = True
                        scorefinal()
                elif mot_en_progres == list(secret):
                    annonce["text"] = "Gagné !"
                    label_etape[12].place(x=670, y=210)
                    end = True
                    frame_clavier1.place_forget()
                    frame_clavier2.place_forget()
                    scorefinal()
                return cpt_perdu

            # FONCTIONS RECUP LETTRE
            def choisir_lettre(event):
                if end:
                    return
                mon_btn = event.widget
                lettre = mon_btn["text"]
                mon_btn["state"] = DISABLED
                maj_mot_en_progres(mot_en_progres, lettre, secret)
                lbl["text"] = " ".join(mot_en_progres)
                score(lettre)

            # GENERATION MOT
            L = []
            for x in rootmot.findall('liste'):
                nom = x.find('mot').text
                L.append(nom)
                # print(nom)
            secret = random.choice(L)
            longsecret = len(secret)
            mot_en_progres = list("_" * longsecret)
            stars = " ".join(mot_en_progres)

            # FONCTION SCORE FINAL
            def scorefinal():
                global end
                if end:
                    pointnbcoup = limite_perdu - cpt_perdu
                    pointlenmot = longsecret
                    pointbonusdiff = 5
                    calculscorefinal = pointnbcoup + pointlenmot + pointbonusdiff
                    labelscorefinal1 = Label(self.window, text="Votre score final est de :", font=("Times 15 bold", 30),
                                             bg="#ccccff", fg="black")
                    labelscorefinal1.place(x=240, y=620)
                    labelscorefinal2 = Label(self.window, text=calculscorefinal, font=("Times 15 bold", 30),
                                             bg="#ccccff", fg="black")
                    labelscorefinal2.place(x=680, y=620)
                    return calculscorefinal

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

            self.window.mainloop()

        def closeWindow(self):
            self.window.destroy()

    maingame = Game()
    maingame.openWindow()
