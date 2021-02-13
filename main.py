import acceuil
from player import Joueur
import tkinter as tk

if __name__ == "__main__":
    rootWindow = tk.Tk()
    rootWindow.withdraw()
    joueur = Joueur()
    acceuil.Acceuil(rootWindow,joueur).openWindow()

