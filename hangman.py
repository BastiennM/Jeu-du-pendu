import xml.etree.ElementTree as ET
import random

xml_mot = ET.parse('xml/mot.xml')
root_mot = xml_mot.getroot()


class HangMan:
    def __init__(self, difficulte):
        self.motadecouvrir = self.genmot()
        self.longueurmot = len(self.motadecouvrir)
        self.difficultelevel = difficulte
        self.nombressaimax = self.__calcnombreessai()
        self.pointbonus = (self.difficultelevel + 1) * 5
        self.nombresessai = 0
        self.lettresdisponibles = [chr(n) for n in range(65, 91)]
        self.lettredecouverte = []

    def getdifficultetext(self):
        optionsdifficulte = ["Facile", "Normal", "Difficile"]
        return optionsdifficulte[self.difficultelevel]

    def __calcnombreessai(self):
        listessai = [11, 9, 7]
        return listessai[self.difficultelevel]

    def calc_score(self):
        return (self.nombressaimax - self.nombresessai) + self.longueurmot + self.pointbonus

    def genmot(self):
        return root_mot[random.randrange(0, len(root_mot))].text

    def verifiemotcomplet(self):
        if sorted(self.motadecouvrir) == sorted(self.lettredecouverte):
            return True
        else:
            return False

    def verifieetatessai(self):
        if self.nombresessai == self.nombressaimax:
            return False
        else:
            return True

    def trouvelettre(self, lettresoumise):
        if not self.verifietatessai:
            return False
        if self.verifiemotcomplet:
            return True
        if lettresoumise in self.motadecouvrir:
            self.lettredecouverte.append(lettresoumise)
            self.lettresdisponibles.remove(lettresoumise)
            return True
        else:
            self.lettresdisponibles.remove(lettresoumise)
            self.nombresessai += 1
            return False
