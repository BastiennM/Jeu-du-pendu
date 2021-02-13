from tkinter import *
import xml.etree.ElementTree as ET
import unicodedata
import acceuil
import top10
import aide

tree = ET.parse('xml/mot.xml')
myroot = tree.getroot()


class Gestionmot:
    def __init__(self, rootwindow, joueur):
        self.window = Toplevel(rootwindow)
        self.rootwindow = rootwindow
        self.joueur = joueur

    def openWindow(self):
        self.window.title("Gestion Mot")
        self.window.geometry("1080x720")
        self.window.minsize(480, 360)
        self.window.iconbitmap("img/logo.ico")
        self.window.config(background='#f9791e')

        # Menu Page de jeu
        pendumenu = Menu(self.window)
        first_menu = Menu(pendumenu, tearoff=0)
        first_menu.add_command(label="Quitter", command=self.window.destroy)
        first_menu.add_command(label="Acceuil", command=self.openacceuil)
        first_menu.add_command(label="Top 10", command=self.opentop10window)
        first_menu.add_command(label="Aide", command=self.openaidewindow)
        pendumenu.add_cascade(label="Menu", menu=first_menu)
        self.window.config(menu=pendumenu)

        # CREATION LISTE MOT
        L = []
        for x in myroot.findall('mot'):
            nom = x.text
            print(nom)
            L.append(nom)
        # create frame and scrollbar
        frame_scrollist = Frame(self.window)
        scrollbar = Scrollbar(frame_scrollist, orient=VERTICAL)
        listbox = Listbox(frame_scrollist, width=50, yscrollcommand=scrollbar.set)

        # CONFIGURE SCROLLBAR
        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        frame_scrollist.pack()
        listbox.pack(pady=15)



        for item in L:
            listbox.insert(END, item)

        def delete():
            elementsupp = listbox.get(listbox.curselection())
            L.remove(elementsupp)
            new_field = ET.Element("words")
            for item in L:
                ET.SubElement(new_field, "mot").text = item
            tree1 = ET.ElementTree(new_field)
            tree1.write('xml/mot.xml', encoding='utf-8', xml_declaration=True)
            listbox.delete(ANCHOR)

        def add():
            content = newword.get()
            content = content.upper()
            content_no_accents = ''.join((c for c in unicodedata.normalize('NFD', content) if unicodedata.category(c) != 'Mn'))
            content_no_special = ''.join(e for e in content_no_accents if e.isalnum())
            listbox.insert(END, content_no_special)
            L.append(content_no_special)
            new_field = ET.Element("words")
            for item in L:
                ET.SubElement(new_field, "mot").text = item
            tree1 = ET.ElementTree(new_field)
            tree1.write('xml/mot.xml', encoding='utf-8', xml_declaration=True)

        # NOUVEAU MOT
        newword = Entry(self.window,width=50, background=None)
        newword.pack()
        btnadd = Button(self.window, text="Add", command=add)
        btnadd.pack()
        # DELETE
        btndelete = Button(self.window, text="Delete", command=delete)
        btndelete.pack()

    def opentop10window(self):
        self.window.destroy()
        top10.Top10(self.rootwindow, self.joueur).openWindow()

    def openaidewindow(self):
        self.window.destroy()
        aide.Aide(self.rootwindow, self.joueur).openWindow()

    def openacceuil(self):
        self.window.destroy()
        acceuil.Acceuil(self.rootwindow, self.joueur).openWindow()
