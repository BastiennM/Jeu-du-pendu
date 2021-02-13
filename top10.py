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


class Top10:
    def __init__(self):
        self.window = Tk()

    def openWindow(self):
        self.window.title("Top 10")
        self.window.geometry("1080x720")
        self.window.minsize(480, 360)
        self.window.iconbitmap("img/logo.ico")
        self.window.config(background='#f9791e')

        # Remplissage de la liste avec toute les infos joueurs
        joueurliste = []
        for joueur_item in rootjoueur.findall('./player'):
            joueur_detail = {}
            for detail in joueur_item:
                joueur_detail[detail.tag] = detail.text.encode('UTF-8')
            joueurliste.append(joueur_detail)

        listediffnormal = list(filter(lambda x: x['difficulte'] == b'Normal', joueurliste))
        joueurlistetrienormal = sorted(listediffnormal, reverse=True, key=lambda i: i['score'])

        listedifffacile = list(filter(lambda x: x['difficulte'] == b'Facile', joueurliste))
        joueurlistetriefacile = sorted(listedifffacile, reverse=False, key=lambda i: i['score'])


        listediffdifficile = list(filter(lambda x: x['difficulte'] == b'Difficile', joueurliste))
        joueurlistetriedifficile = sorted(listediffdifficile, reverse=True, key=lambda i: i['score'])


        # for x in rootjoueur.findall('player'):
        #     nom = x.find('joueur').text
        #     diff = x.find("difficulte").text
        #     score = x.find("score").text
        #     score = int(score)
        #     listejoueur.append([])
        #     listejoueur[len(listejoueur) - 1].append(nom)
        #     listejoueur[len(listejoueur) - 1].append(diff)
        #     listejoueur[len(listejoueur) - 1].append(score)
        #
        # def Sort(sub_li):
        #     sub_li.sort(key=lambda x: x[2])
        #     return sub_li

        # create frame and scrollbar
        frame_scrollist = Frame(self.window)
        scrollbar = Scrollbar(frame_scrollist, orient=VERTICAL)
        listbox = Listbox(frame_scrollist, width=50, yscrollcommand=scrollbar.set)

        # CONFIGURE SCROLLBAR
        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        frame_scrollist.pack()
        listbox.pack(pady=15)

        for key, value in zip(range(10), joueurlistetriefacile):
            print(key, value)
        for item in joueurlistetriefacile:
            global cptinsert
            listbox.insert(0, (joueurlistetriefacile[cptinsert]))
            cptinsert = cptinsert + 1
