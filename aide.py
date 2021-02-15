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

        # CREATION FRAME
        frame_aide = Frame(self.window,background='#ccccff')
        frame_aide.place(x=25, y=20, width=980, height=710  )

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
