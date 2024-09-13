class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.__titulaire = titulaire
        self.__solde = solde

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"{montant} EUR déposés.")
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        if montant > 0 and montant <= self.__solde:
            self.__solde -= montant
            print(f"{montant} EUR retirés.")
        else:
            print("Fonds insuffisants ou montant invalide.")

    def afficher_solde(self):
        print(f"{self.__titulaire} a pour solde: {self.__solde} EUR")


compte = CompteBancaire("Alice", 1000)
compte.deposer(200)
compte.retirer(150)
compte.afficher_solde()
