from tkinter import *

# creer une première fenetre
fenetre = Tk()

# personnaliser cette fenetre
fenetre.title("Page d'accueil")
fenetre.geometry("1080x720")
fenetre.minsize(480, 360)
fenetre.iconbitmap("logo.ico")
fenetre.config(background='#FF5733')

#creer la frame
frame = Frame(fenetre, bg='#ff5733')

# ajouter un premier texte
label_title = Label(frame, text="Bienvenue sur le jeu du", font=("Courrier", 30), bg="#FF5733", fg="white")
label_title.pack(expand=YES)

# ajouter un second texte
label_subtitle = Label(frame, text="PENDU", font=("Courrier", 40), bg="#FF5733", fg="white")
label_subtitle.pack(expand=YES)

# ajouter un bouton
menu_button = Button(frame, text="Jouer",height="2", font=("Arial", 15), bg="white", fg="#FF5733")
menu_button.pack(pady="15", fill=X)

menu_button = Button(frame, text="Top 10",height="2", font=("Arial", 15), bg="white", fg="#FF5733")
menu_button.pack(pady="15", fill=X)

menu_button = Button(frame, text="Gestion des mots", height="2", font=("Arial", 15), bg="white", fg="#FF5733")
menu_button.pack(pady="15", fill=X)

menu_button = Button(frame, text="Aide",height="2", font=("Arial", 15), bg="white", fg="#FF5733")
menu_button.pack(pady="15", fill=X)

menu_button = Button(frame, text="Quitter",height="2", font=("Arial", 15), bg="white", fg="#FF5733")
menu_button.pack(pady="15", fill=X)

#ajouter
frame.pack(expand=YES)
# afficher
fenetre.mainloop()

