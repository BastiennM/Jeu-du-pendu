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
