import xml.etree.ElementTree as ET

# tree = ET.parse('test.xml')
# myroot = tree.getroot()
'''
# PRINT NOM
for x in myroot.findall('user'):
    nom = x.find('nom').text
    print(nom)
'''

'''
#MODIFIER UN CHAMP
for x in myroot.iter('nom'):
    a = str(x.text) + '| Nom ajoute'
    x.text = str(a)
    x.set('updated', 'yes')
tree.write('new.xml')
'''

'''
# CREER UN TAG
ET.SubElement(myroot[0], 'score')
for x in myroot.iter('score'):
    b = 'score de 1'
    x.text = str(b)
tree.write('new.xml')
'''

'''
# ENLVER UN ATTRIBUT TAG (comme une classe en html)
myroot[0].attrib.pop('data-id')
tree.write('new.xml')
'''

'''
# SUPPRIMER UN TAG
myroot[0].remove(myroot[0][0])
tree.write('new.xml')
'''

'''
#SUPPRIMER UN GROUPE DE TAG
myroot[0].clear()
tree.write('new.xml')
'''



#creer un groupe
root = ET.Element("player")
groupe = ET.SubElement(root, "sub-player")

ET.SubElement(groupe, "nomplayer").text = "NOM"
ET.SubElement(groupe, "difficulte").text = "DIFFICULTE"

tree1 = ET.ElementTree(root)
tree1.write('new.xml')


