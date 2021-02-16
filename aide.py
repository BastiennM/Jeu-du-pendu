from tkinter import *
import acceuil
import top10
import game
import gestiondesmots


# DEUX FONCTION
def two_funcs(*funcs):
    def two_funcs(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return two_funcs


class Aide:
    def __init__(self, rootwindow, joueur):
        self.window = Toplevel(rootwindow)
        self.rootwindow = rootwindow
        self.joueur = joueur

    def openWindow(self):
        self.window.title("Aide")
        self.window.geometry("1024x768")
        self.window.minsize(480, 360)
        self.window.iconbitmap("img/logo.ico")

        # Menu Page aide
        pendumenu = Menu(self.window)
        first_menu = Menu(pendumenu, tearoff=0)
        first_menu.add_command(label="Quitter", command=self.window.destroy)
        first_menu.add_command(label="Acceuil", command=self.openacceuil)
        first_menu.add_command(label="Top 10", command=self.opentop10)
        first_menu.add_command(label="Jeu", command=self.opengamewindow)
        first_menu.add_command(label="Gestion des mots", command=self.opengestiondesmots)
        pendumenu.add_cascade(label="Menu", menu=first_menu)
        self.window.config(menu=pendumenu)

        # CREATION ET PLACE FRAME
        frame_aide = Frame(self.window, background='#ccccff')
        frame_aide.place(x=0, y=0, width=1024, height=768)
        frame_Tt = Frame(self.window, background='#ccccff')
        frame_Tt.place(x=20, y=35, width=1000, height=700)

        label_title = Label(frame_Tt,
                            text="Voici la page aide",
                            font=("Arial", 27), bg="#ccccff", fg="black")
        label_title.pack()
        label_subtitle = Label(frame_Tt,text='Si vous avez quleques problèmes, les réponses sont ici',font=("Arial", 20), bg="#ccccff", fg="black")
        label_subtitle.pack()
        label_dif = Label(frame_Tt, text="\n\nLa difficulté :", font=("Arial", 17), bg="#ccccff", fg="black")
        label_dif.pack()
        label_expDIf = Label(frame_Tt,
                             text="Elle correspond au nombre de points bonus. Plus la difficulté est élevée plus il y aura de point bonus.",
                             font=("Arial", 10), bg="#ccccff", fg="black")
        label_expDIf.pack()
        label_Faci = Label(frame_Tt,
                           text="Facile : 5 points bonus \nMoyen : 10 points bonus\nDifficile : 15 points bonus\n\n",
                           font=("Arial", 10), bg="#ccccff", fg="black")
        label_Faci.pack()
        label_score = Label(frame_Tt, text="Le score :", font=("Arial", 17), bg="#ccccff", fg="black")
        label_score.pack()
        label_expSco = Label(frame_Tt,
                             text="Vous commencez la partie avec les points attribués en fonction de la difficulté que vous avez choisi.\n +1 point par lettre du mot\n-1 point par lettre n'appartenant pas au mot\n",
                             font=("Arial", 10), bg="#ccccff", fg="black")
        label_expSco.pack()
        label_P5 = Label(frame_Tt, text="Si votre score atteint 0 ou que le pendu est complété vous perdez",
                         font=("Arial", 13), bg="#ccccff", fg="black")
        label_P5.pack()
        label_top10 = Label(frame_Tt, text="\nLe top 10 :", font=("Arial", 17), bg="#ccccff", fg="black")
        label_top10.pack()
        label_expTop10 = Label(frame_Tt,
                             text="Dans l'onglet Top10, sont affichés les 10 meilleurs joueurs en fonction de leur score",
                             font=("Arial", 10), bg="#ccccff", fg="black")
        label_expTop10.pack()
        label_gestMot = Label(frame_Tt, text="\nLa gestion des mots :", font=("Arial", 17), bg="#ccccff", fg="black")
        label_gestMot.pack()
        label_expGestMot = Label(frame_Tt,
                             text="Dans l'onglet Gestion des mots, sont affichés les mots contenus dans le jeu.\nIl est possible d'en rajouter ou bien d'en supprimer",
                             font=("Arial", 10), bg="#ccccff", fg="black")
        label_expGestMot.pack()
        label_Mess = Label(frame_Tt, text="\nA vous de jouer !!!", font=("Arial", 17), bg="#ccccff", fg="black")
        label_Mess.pack()

    def openacceuil(self):
        self.window.destroy()
        acceuil.Acceuil(self.rootwindow, self.joueur).openWindow()

    def opentop10(self):
        self.window.destroy()
        top10.Top10(self.rootwindow, self.joueur).openWindow()

    def opengamewindow(self):
        self.window.destroy()
        game.Game(self.rootwindow, self.joueur).openWindow()

    def opengestiondesmots(self):
        self.window.destroy()
        gestiondesmots.Gestionmot(self.rootwindow, self.joueur).openWindow()
