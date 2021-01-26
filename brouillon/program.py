# coding=utf-8
import random

# fichier de mots dans liste
liste = []
fichier = open("liste.txt", "rt")
for x in fichier:
    liste.append(x.rstrip("\n"))

mot = liste[random.randint(0, len(liste) - 1)]
# liste contenant les caractères du mot
mot_l = list(mot)
# liste des caractères cachés soit _
mot_c = []
for i in range(len(mot_l)):
    mot_c.append("_")


essai = 100

print(" Trouvez le mot codé.")
print('Vous commencez avec 48 points, essayez de les conservers')
a = "_"
while a in mot_c:
    if essai > 0:
        print("\n Il vous reste %d essais" % essai)
        # lettre remplace _
        print(mot_c)
        choix = input(">>>")
        # majuscule
        b = choix.capitalize()
        if choix in mot_l or b in mot_l:
            for x in range(len(mot_l)):
                # remplacer les _ par rapport au nombre de caractère
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
