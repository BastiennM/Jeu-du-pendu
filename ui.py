from tkinter import *
import tkinter.font as tkfont
# creer une première fenetre
window = Tk()

# personnaliser cette fenetre
window.title("Page d'accueil")
window.geometry("1080x720")
window.minsize(1080, 720)
window.iconbitmap("logo.ico")
window.config(background='black')

# ajouter un premier texte
label_title = Label(window, text="Bienvenu sur le site", font=("Montserrat", 40), bg='black', fg='white')
label_title.pack(expand=YES)

# ajouter un bouton
bouton=Button(
              text = "Liste des mots",
              font=tkfont.Font("Montserrat", "16"),
              activebackground='red',
              width=30,
              height=5)
bouton.pack(expand=YES)


# afficher
window.mainloop()

