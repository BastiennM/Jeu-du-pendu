import random
import xml.etree.ElementTree as ET

tree = ET.parse('mot.xml')
myroot = tree.getroot()


L = []
for x in myroot.findall('liste'):
    nom = x.find('mot').text
    L.append(nom)
    print(nom)
mot = random.choice(L)

print(mot)
