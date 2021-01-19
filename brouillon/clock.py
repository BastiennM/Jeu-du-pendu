import tkinter as tk

def decompte(count=5):
    lab.config(text=str(count))
    if count > 0:
        fen1.after(1000, decompte, count - 1,)
    if count <=0:
         lab.config(text="Temps écoulé !")


fen1 = tk.Tk()

lab = tk.Label(fen1, text="")
lab.pack()

btn = tk.Button(fen1, text="Commencer", command=decompte)
btn.pack()

fen1.mainloop()
