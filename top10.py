from tkinter import *
import xml.etree.ElementTree as ET
from tkinter import ttk
import aide
import acceuil
import gestiondesmots

treejoueur = ET.parse('xml/joueur.xml')
rootjoueur = treejoueur.getroot()
cptinsert = 0


# DEUX FONCTION
def two_funcs(*funcs):
    def two_funcs(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return two_funcs


class Top10:
    def __init__(self, rootwindow, joueur):
        self.window = Toplevel(rootwindow)
        self.rootwindow = rootwindow
        self.joueur = joueur

    def openWindow(self):
        self.window.title("Top 10")
        self.window.geometry("1024x768")
        self.window.minsize(480, 360)
        self.window.iconbitmap("img/logo.ico")
        self.window.config(background='#ccccff')


        # Menu Page de jeu
        pendumenu = Menu(self.window)
        first_menu = Menu(pendumenu, tearoff=0)
        first_menu.add_command(label="Quitter", command=self.window.destroy)
        first_menu.add_command(label="Acceuil", command=self.openacceuil)
        first_menu.add_command(label="Aide", command=self.openaidewindow)
        first_menu.add_command(label="Gestion des mots", command=self.opengestionmots)
        pendumenu.add_cascade(label="Menu", menu=first_menu)
        self.window.config(menu=pendumenu)

        label_titre = Label(self.window, text='Top 10', font=("Courrier", 40), bg="#ccccff", fg="black")
        label_titre.pack(pady=(100,0))

        # Remplissage de la liste avec toute les infos joueurs
        joueurliste = []
        for joueur_item in rootjoueur.findall('./player'):
            joueur_detail = {}
            for detail in joueur_item:
                joueur_detail[detail.tag] = detail.text.encode('UTF-8')
            joueurliste.append(joueur_detail)

        listedifffacile = list(filter(lambda x: x['difficulte'] == b'Facile', joueurliste))
        joueurlistetriefacile = sorted(listedifffacile, reverse=False, key=lambda i: i['score'])

        listediffnormal = list(filter(lambda x: x['difficulte'] == b'Normal', joueurliste))
        joueurlistetrienormal = sorted(listediffnormal, reverse=True, key=lambda i: i['score'])

        listediffdifficile = list(filter(lambda x: x['difficulte'] == b'Difficile', joueurliste))
        joueurlistetriedifficile = sorted(listediffdifficile, reverse=True, key=lambda i: i['score'])

        frametop10 = Frame(self.window)
        frametop10.pack(pady=100)
        treescroll = Scrollbar(frametop10)
        treescroll.pack(side=RIGHT, fill=Y)



        # DEFINIR LE TABLEAU
        Tableau = ttk.Treeview(frametop10, yscrollcommand=treescroll.set)

        # CONFIGURE SCROLLBAR
        treescroll.config(command=Tableau.yview)

        # DEFINIR LES COLONNES
        Tableau['columns'] = ('Pseudo', 'Score')

        # FORMATER LES COLONNES
        Tableau.column("#0", width=120, minwidth=25)
        Tableau.column('Pseudo', anchor=CENTER, width=80)
        Tableau.column('Score', anchor=W, width=120)

        # CREER HEADER
        Tableau.heading('#0', text="Niveau", anchor=W)
        Tableau.heading('Pseudo', text="Pseudo", anchor=W)
        Tableau.heading('Score', text="Score", anchor=W)

        # AJOUTER LES DONNÉES
        # Tableau.insert(parent='', index='end', iid=0, text='Facile', values=('Yann', 15))
        # Tableau.pack()

        nivparent = Tableau.insert(parent='', index='end', text='Facile')
        for key, value in zip(range(10), joueurlistetriefacile):
            Tableau.insert(parent=nivparent, index='end', text='',
                           values=(value['pseudo'].decode('UTF-8'), int(value['score'])))
        nivparent = Tableau.insert(parent='', index='end', text='Moyen')
        for key, value in zip(range(10), joueurlistetrienormal):
            Tableau.insert(parent=nivparent, index='end', text='',
                           values=(value['pseudo'].decode('UTF-8'), int(value['score'])))
        nivparent = Tableau.insert(parent='', index='end', text='Difficile')
        for key, value in zip(range(10), joueurlistetriedifficile):
            Tableau.insert(parent=nivparent, index='end', text='',
                           values=(value['pseudo'].decode('UTF-8'), int(value['score'])))
        Tableau.pack()

    def openacceuil(self):
        self.window.destroy()
        acceuil.Acceuil(self.rootwindow, self.joueur).openWindow()

    def openaidewindow(self):
        self.window.destroy()
        aide.Aide(self.rootwindow, self.joueur).openWindow()

    def opengestionmots(self):
        self.window.destroy()
        gestiondesmots.Gestionmot(self.rootwindow, self.joueur).openWindow()
