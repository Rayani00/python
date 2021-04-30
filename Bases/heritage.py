class Animal():
    def marcher(self):
        print("Je marche comme un animal")


# La classe Chien herite de Animal
class Chien(Animal):
    def aboyer(self):
        print('Waf')


class Chat(Animal):
    def miauler(self):
        print('Miaw')


chien = Chien()
chien.marcher()
chien.aboyer()
chat = Chat()
chat.miauler()
