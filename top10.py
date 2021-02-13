from tkinter import *
import xml.etree.ElementTree as ET

treejoueur = ET.parse('joueur.xml')
rootjoueur = treejoueur.getroot()
cptinsert = 0


# DEUX FONCTION
def two_funcs(*funcs):
    def two_funcs(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return two_funcs


def opentop10():
    class top10:
        def __init__(self):
            self.window = Tk()

        def openWindow(self):
            self.window.title("Top 10")
            self.window.geometry("1080x720")
            self.window.minsize(480, 360)
            self.window.iconbitmap("img/logo.ico")
            self.window.config(background='#f9791e')

            listejoueur = []
            for x in rootjoueur.findall('player'):
                nom = x.find('joueur').text
                diff = x.find("difficulte").text
                score = x.find("score").text
                score = int(score)
                listejoueur.append([])
                listejoueur[len(listejoueur) - 1].append(nom)
                listejoueur[len(listejoueur) - 1].append(diff)
                listejoueur[len(listejoueur) - 1].append(score)
            print(len(listejoueur))

            def Sort(sub_li):
                sub_li.sort(key=lambda x: x[2])
                return sub_li

            # create frame and scrollbar
            frame_scrollist = Frame(self.window)
            scrollbar = Scrollbar(frame_scrollist, orient=VERTICAL)
            listbox = Listbox(frame_scrollist, width=50, yscrollcommand=scrollbar.set)

            # CONFIGURE SCROLLBAR
            scrollbar.config(command=listbox.yview)
            scrollbar.pack(side=RIGHT, fill=Y)
            frame_scrollist.pack()
            listbox.pack(pady=15)
            Sort(listejoueur)
            while len(listejoueur) > 10:
                listejoueur.pop()
            print(len(listejoueur))
            for item in listejoueur:
                global cptinsert
                listbox.insert(0, (listejoueur[cptinsert]))
                cptinsert = cptinsert + 1

    main = top10()
    main.openWindow()
