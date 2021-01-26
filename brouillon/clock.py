import tkinter as tk

def decompte(count=120):
    lab.config(text=str(count))
    if count > 0:
        fen1.after(1000, decompte, count - 1,)
    if count <=0:
         lab.config(text="Temps écoulé, vous avez perdu !!")
    pts=50

    if count == 90:
        pts=pts-10
        print("Il vous reste",pts,"points")
    pts=pts-10
    if count == 60:
        pts=pts-10
        print("Il vous reste", pts, "points")
    pts = pts-20
    if count == 30:
        pts = pts-10
        print("Il vous reste", pts, "points")

fen1 = tk.Tk()

lab = tk.Label(fen1, text="")
lab.pack()

btn = tk.Button(fen1, text="Commencer", command=decompte)
btn.pack()

fen1.mainloop()
