class Point:
    def move(self):
        print('Move')

    def draw(self):
        print('Draw')

    # Constructeur
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Personne():
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def presentation(self):
        print(f"Bonjour, je m'appelle {self.prenom} {self.nom}")


# Instanciation
# point1 = Point()
# On peut creer des objets avec les valeurs qu'on veut
""" point1.x = 10
point1.y = 20
print(point1.x)
point1.move() """
# Creation avec le constructeur
point = Point(5, 3)
# Classe Personne
nom = input("Veuillez entrer votre nom ")
nom = str(nom)
prenom = input("Veuillez entrer votre prenom ")
prenom = str(prenom)
personne = Personne(nom=nom, prenom=prenom)
personne.presentation()
