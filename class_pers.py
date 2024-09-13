class Personne:
    # Attribut de classe pour stocker toutes les instances
    toutes_les_personnes = []

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        # Ajouter l'instance actuelle à la liste des personnes
        Personne.toutes_les_personnes.append(self)

    # Méthode pour afficher les détails de toutes les personnes
    @classmethod
    def afficher_toutes_les_personnes(cls):
        for personne in cls.toutes_les_personnes:
            print(f"Nom: {personne.nom}, Age: {personne.age}")


# Création de quelques objets Personne
p1 = Personne("Alice", 30)
p2 = Personne("Bob", 25)
p3 = Personne("Charlie", 35)

# Afficher tous les objets de la classe Personne
Personne.afficher_toutes_les_personnes()


class Personne2:
    # Attribut de classe pour stocker toutes les instances
    toutes_les_personnes = []

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        # Ajouter l'instance actuelle à la liste des personnes
        Personne2.toutes_les_personnes.append(self)

    # Méthode pour afficher les détails de toutes les personnes avec une boucle while
    @classmethod
    def afficher_toutes_les_personnes(cls):
        i = 0
        while i < len(cls.toutes_les_personnes):
            personne = cls.toutes_les_personnes[i]
            print(f"Nom: {personne.nom}, Age: {personne.age}")
            i += 1


# Création de quelques objets Personne
p1 = Personne2("Alice", 30)
p2 = Personne2("Bob", 25)
p3 = Personne2("Charlie", 35)

# Afficher tous les objets de la classe Personne
Personne2.afficher_toutes_les_personnes()
