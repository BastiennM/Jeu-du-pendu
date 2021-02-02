from tkinter import *
import tkinter
from tkinter import ttk


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

        self.window.mainloop()


        main = Game()
        main.openWindow()
