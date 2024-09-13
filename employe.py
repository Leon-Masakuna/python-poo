class Employe:
    def __init__(self, nom, poste, salaire):
        self.nom = nom
        self.poste = poste
        self.__salaire = salaire

    def augmenter_salaire(self, montant):
        if montant > 0:
            self.__salaire += montant
            print(f"Salaire augmenté de {montant} EUR.")
        else:
            print("Montant invalide.")

    def afficher_salaire(self):
        print(f"Salaire de {self.nom}: {self.__salaire} EUR")


e1 = Employe("Bob", "Développeur", 35000)
e1.augmenter_salaire(5000)
e1.afficher_salaire()
