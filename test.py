from game import *
from tkinter import *

top10_window = Tk()
top10_window.title("Top 10")
top10_window.geometry("1080x720")
top10_window.minsize(480, 360)
top10_window.iconbitmap("img/logo.ico")
top10_window.config(background='#f9791e')

def openwindow(self):
    self = Tk()
    self.title("Jeu du pendu")
    self.geometry("1024x768")
    self.minsize(1024, 768)
    self.maxsize(1024, 768)
    self.iconbitmap("img/logo.ico")
    self.resizable(False, False)
    bg_jeu = PhotoImage(file="img/jeupendu.png")
    label_jeu = Label(self, image=bg_jeu)
    label_jeu.place(x=0, y=0, relwidth=1, relheight=1)

def opengamewindow():
    game = Game()
    top10_window.destroy()
    openwindow(game)


btn_timer = Button(text="Commencer", command=opengamewindow)
btn_timer.pack()
top10_window.mainloop()
