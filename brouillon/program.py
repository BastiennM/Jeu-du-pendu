import random

liste = []
fichier = open("liste.txt", "rt")
for x in fichier:
    liste.append(x.rstrip("\n"))

mot = liste[random.randint(0, len(liste) - 1)]
mot_l = list(mot)
mot_c = []
for i in range(len(mot_l)):
    mot_c.append("_")


def c(mot):
    a = 0
    for b in range(len(mot)):
        if mot[b] == "_":
            a += 1
    return a


essai = len(mot_l) + 10

print(" Trouvez le mot codé.")
a = "_"
while a in mot_c:
    if essai > 0 and essai >= c(mot_c):
        print("\n Il vous reste %d essais" % essai)
        print(mot_c)
        choix = input(" »»» ")
        b = choix.capitalize()
        if choix in mot_l or b in mot_l:
            for x in range(len(mot_l)):
                if choix == mot_l[x] or b == mot_l[x]:
                    mot_c[x] = mot_l[x]
        essai -= 1
    else:
        print("\n Vous n'aviez plus assez d'essais pour continuer. "
              "\n Le mot était « %s »"
              "\n Vous avez perdu !!" % mot)
        break
if a not in mot_c:
    print("\n Bravo vous avez trouvé le mot « %s » !!!" % mot)
