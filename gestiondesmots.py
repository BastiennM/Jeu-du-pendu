from tkinter import *
import xml.etree.ElementTree as ET
import unicodedata

tree = ET.parse('mot.xml')
myroot = tree.getroot()


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
            first_menu.add_command(label="Quitter", command=self.window.destroy)
            pendumenu.add_cascade(label="Menu")
            self.window.config(menu=pendumenu)

            # CREATION LISTE MOT
            L = []
            for x in myroot.findall('liste'):
                nom = x.find('mot').text
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
                new_field = ET.Element("word")
                for item in L:
                    groupe = ET.SubElement(new_field, "liste")
                    ET.SubElement(groupe, "mot").text = item
                tree1 = ET.ElementTree(new_field)
                tree1.write('mot.xml', encoding='utf-8', xml_declaration=True)
                listbox.delete(ANCHOR)

            def add():
                content = newword.get()
                content = content.upper()
                content_no_accents = ''.join((c for c in unicodedata.normalize('NFD', content) if unicodedata.category(c) != 'Mn'))
                content_no_special = ''.join(e for e in content_no_accents if e.isalnum())
                listbox.insert(END, content_no_special)
                L.append(content_no_special)
                print(L)
                new_field = ET.Element("word")
                for item in L:
                    groupe = ET.SubElement(new_field, "liste")
                    ET.SubElement(groupe, "mot").text = item
                tree1 = ET.ElementTree(new_field)
                tree1.write('mot.xml', encoding='utf-8', xml_declaration=True)

            # NOUVEAU MOT
            newword = Entry(self.window,width=50, background=None)
            newword.pack()
            btnadd = Button(self.window, text="Add", command=add)
            btnadd.pack()
            # DELETE
            btndelete = Button(self.window, text="Delete", command=delete)
            btndelete.pack()

    main = gestionmot()
    main.openWindow()
