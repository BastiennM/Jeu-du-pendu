import xml.etree.ElementTree as ET

tree = ET.parse('new.xml')
myroot = tree.getroot()
# PRINT NOM
'''
for x in myroot.findall('sub-player'):
    nom = x.find('nomplayer').text
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
myroot.remove(myroot)
tree.write('new.xml')
'''
'''
#SUPPRIMER UN GROUPE DE TAG
myroot[0].clear()
tree.write('new.xml')
'''

# creer un groupe
L = ['1', '2']

new_field = ET.Element("word")
groupe = ET.SubElement(new_field, "liste")
for item in L:
    ET.SubElement(groupe, "mot").text = item
tree1 = ET.ElementTree(new_field)
tree1.write(open('new.xml', 'wb'))
