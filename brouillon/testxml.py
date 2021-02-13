# # import xml.etree.ElementTree as ET
# #
# # tree = ET.parse('new.xml')
# # myroot = tree.getroot()
# # # PRINT NOM
# import unicodedata
# '''
# for x in myroot.findall('sub-player'):
#     nom = x.find('nomplayer').text
#     print(nom)
# '''
#
# '''
# #MODIFIER UN CHAMP
# for x in myroot.iter('nom'):
#     a = str(x.text) + '| Nom ajoute'
#     x.text = str(a)
#     x.set('updated', 'yes')
# tree.write('new.xml')
# '''
#
# '''
# # CREER UN TAG
# ET.SubElement(myroot[0], 'score')
# for x in myroot.iter('score'):
#     b = 'score de 1'
#     x.text = str(b)
# tree.write('new.xml')
# '''
#
# '''
# # ENLVER UN ATTRIBUT TAG (comme une classe en html)
# myroot[0].attrib.pop('data-id')
# tree.write('new.xml')
# '''
#
# '''
# # SUPPRIMER UN TAG
# myroot.remove(myroot)
# tree.write('new.xml')
# '''
# '''
# #SUPPRIMER UN GROUPE DE TAG
# myroot[0].clear()
# tree.write('new.xml')
# '''
# #
# # # creer un groupe
# # L = [
# #     ['Bastien', 'a', 10],
# #     ['LOL', 'b', 50],
# #     ['MOI', 'c', 15]
# # ]
#
#
# # score = []
# # # cpt = 0
# # # cptscore = 1
# # # for item in L:
# # #     score.append(L[cpt][2])
# # #     cpt = cpt +1
# # # print(score)
# # # for i in range(0,len(score)-1):
# # #     maxscore = max(score)
# # #     indexmaxscore = score.index(max(score))
# # #     print("TOP ",cptscore,L[indexmaxscore-1][0],"avec ",maxscore,"points")
# # #     cptscore = cptscore + 1
# # #     L.pop(indexmaxscore)
# # #     score.pop(indexmaxscore)
# # #     if len(score) == 1:
# # #         print("TOP ",cptscore,L[indexmaxscore-1][0],"avec ",maxscore,"points")
# #
# # def Sort(sub_li):
# #     sub_li.sort(key=lambda x: x[2])
# #     return sub_li
# #
# #
# # print(Sort(L))
#
#
# # print(score)
# # print(max(score))
# # print(score.index(max(score)))
# # L.pop(1)
# # print(L)
#
# # L2 = []
# # L2.append([])
# # L2[len(L2)-1].append('a')
# # L2[len(L2)-1].append('b')
# # print(L2)
# # print(len(L2))
# # L2.append([])
# # L2[len(L2)-1].append('c')
# # L2[len(L2)-1].append('d')
# # print(L2)
# # print(len(L2))
#
# # cpt = 0
# #
# # new_field = ET.Element("word")
# # for item in L:
# #     for i in range (0,1):
# #         groupe = ET.SubElement(new_field, "PLAYER")
# #         ET.SubElement(groupe, "joueur").text = L[cpt][0]
# #         ET.SubElement(groupe, "score").text = L[cpt][1]
# #     cpt = cpt +1
# # tree1 = ET.ElementTree(new_field)
# # tree1.write('new.xml')
#
# mot = "été!"
# mot_no_accents = ''.join((c for c in unicodedata.normalize('NFD', mot) if unicodedata.category(c) != 'Mn'))
# string = mot_no_accents
# mot_no_special = ''.join(e for e in string if e.isalnum())
# print(mot_no_special)

array = [
    {
        'time': {"hour":"1", "minute":"30","seconds": "40"}
    },
    {
        'place': {"street":"40 something", "zip": "00000"}
    }
]
