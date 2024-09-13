# Classe mère
class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        print(f"Je suis un {self.nom} et j'ai {self.age} ans.")

# Classe fille
class Chien(Animal):
    def __init__(self, nom, age, race):
        # Appel du constructeur de la classe mère
        super().__init__(nom, age)
        self.race = race  # Attribut propre à la classe fille

    def aboyer(self):
        print(f"{self.nom} aboie !")

    # Redéfinition (polymorphisme) de la méthode de la classe mère
    def se_presenter(self):
        print(f"Je suis un {self.nom}, j'ai {self.age} ans, et je suis de race {self.race}.")

# Création d'un objet de la classe Chien
mon_chien = Chien("Rex", 5, "Labrador")
mon_chien.se_presenter()  # Appelle la méthode redéfinie dans la classe Chien
mon_chien.aboyer()        # Appelle la méthode spécifique à la classe Chien
