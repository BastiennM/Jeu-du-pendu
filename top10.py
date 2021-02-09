from gestiondesmots import GestionMot
from aide import Aide
from tkinter import *


# DEUX FONCTION
def two_funcs(*funcs):
    def two_funcs(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return two_funcs

class Top10:
        def __init__(self):
            self.window = Tk()

        def openWindow(self):
            self.window.title("Top 10")
            self.window.geometry("1080x720")
            self.window.minsize(480, 360)
            #self.window.iconbitmap("img/logo.ico")
            self.window.config(background='#f9791e')

            # Menu Page de top 10
            pendumenu = Menu(self.window)
            first_menu = Menu(pendumenu, tearoff=0)
            first_menu.add_command(label="Acceuil")
            
            first_menu.add_command(label="Gestion des mots", command=two_funcs(self.window.destroy, GestionMot.openWindow(self)))
            first_menu.add_command(label="Aide",command=two_funcs(self.window.destroy, Aide.openWindow(self)))

            first_menu.add_command(label="Quitter", command=self.window.destroy)
            pendumenu.add_cascade(label="Menu", menu=first_menu)
            self.window.config(menu=pendumenu)
