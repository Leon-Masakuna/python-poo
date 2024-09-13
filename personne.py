class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def afficher_info(self):
        print(f"Nom: {self.nom}, Âge: {self.age}")


p1 = Personne("Alice", 30)
p1.afficher_info()
