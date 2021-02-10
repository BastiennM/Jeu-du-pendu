from tkinter import *
from aide import openaide
from top10 import opentop10


def opengestionmot():
    class gestionmot:
        def __init__(self):
            self.window = Tk()

        def openWindow(self):
            self.window.title("Gestion Mot")
            self.window.geometry("1080x720")
            self.window.minsize(480, 360)
            self.window.iconbitmap("img/logo.ico")
            self.window.config(background='#f9791e')

            # Menu Page aide
            pendumenu = Menu(self.window)
            first_menu = Menu(pendumenu, tearoff=0)
            first_menu.add_command(label="Acceuil")
            first_menu.add_command(label="Aide")
            first_menu.add_command(label="Top 10")
            first_menu.add_command(label="Quitter")
            pendumenu.add_cascade(label="Menu")
            self.window.config(menu=pendumenu)

    main = gestionmot()
    main.openWindow()
