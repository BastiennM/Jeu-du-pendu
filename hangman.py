class HangMan:
        def __init__(self,difficulte):
         self.motadecouvrir="SAPIN"
         self.nombressaimax=difficulte*5
         self.nombresessai=0
         self.lettresdisponibles = [chr(n) for n in range(65,91)]
         self.lettredecouverte=[]

        def trouvelettre(self,lettresoumise):
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
                self.nombresessai +=1
                return False
        def verifiemotcomplet(self):
            if sorted(self.motadecouvrir)==sorted(self.lettredecouverte):
                return True
            else:
                return False   
        def verifieetatessai(self):
            if self.nombresessai==self.nombressaimax:
                return False
            else:
                return True   



