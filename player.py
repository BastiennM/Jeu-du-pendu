# self.nom
# difficulte
# a vide
#
# set name
# ...


class player:
    def __init__(self, nom, difficulte, score):
        self._nom = nom
        self._difficulte = difficulte
        self._score = score

    def getNom(self):
        return self._nom

    def setNom(self, value):
        self._nom = value

    def getDifficiculte(self):
        return self._difficulte

    def set_difficulte(self, value):
        self._difficulte = value

    def getScore(self):
        return self._score

    def setScore(self, value):
        self._score = value


bastien = player("Bastien", "Facile", "20")
print(bastien.getNom())
print(bastien.getDifficiculte())
