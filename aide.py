from tkinter import *


# DEUX FONCTION
def two_funcs(*funcs):
    def two_funcs(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return two_funcs


def openaide():
    class aide:
        def __init__(self):
            self.window = Tk()

        def openWindow(self):
            self.window.title("Aide")
            self.window.geometry("1080x720")
            self.window.minsize(480, 360)
            self.window.iconbitmap("img/logo.ico")
            self.window.config(background='#f9791e')

            # Menu Page aide
            pendumenu = Menu(self.window)
            first_menu = Menu(pendumenu, tearoff=0)
            first_menu.add_command(label="Quitter",command=self.window.destroy)
            pendumenu.add_cascade(label="Menu", menu=first_menu)
            self.window.config(menu=pendumenu)

    main = aide()
    main.openWindow()
