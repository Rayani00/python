import math


def main():
    x = 2.9
    isAlive = True
    # declaration de variable
    username = input('Veuillez indiquer votre nom ')
    sexe = input('Veuillez indiquer votre sexe ')
    age = input('Veuillez introduire votre age ')
    # convertir une variable
    int(age)
    # affiche le premier char
    username[0]
    # affiche le dernier char
    username[-1]
    # longuer d'un mot
    print('Nom '+username[-1]+''+username[1:-1]+''+username[0]+'\nSexe '+sexe)
    # index d'une lettre dans un string
    username.find('R')
    # Remplacer une chaine de caractere
    username.replace('Rayan', 'Rayane')
    # Voir si un mot appartient a une chaine
    print('Ra' in username)
    # division entiere
    print(10//3)
    # Puissance
    print(10**3)
    # Modulo
    print(10 % 3)
    # Arrondir
    print(round(x))
    # Valeur absolue
    print(abs(-2.9))
    # Seuil
    print(math.ceil(2.9))


if __name__ == "__main__":
    main()
