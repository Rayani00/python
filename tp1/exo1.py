from decimal import Decimal

# Python 3.8.2 (default, Feb 26 2020, 02:56:10)
#  100/4
# 25.0
#  10/3
# 3.3333333333333335
#  10.0/3
# 3.3333333333333335
#  10/3.0
# 3.3333333333333335
#  from decimal import Decimal
#  a = 10
#  b = 3.0
#  a/b
# 3.3333333333333335
#  a= Decimal(10)
#  b=Decimal(3)
#  a/b
# Decimal('3.333333333333333333333333333')
#  v= 15
#  type(v)
# type v retourne le nom de la calsse d'apartenance de v
# <class 'int'>
#  v = "Olivier"
#  type(v)
# <class 'str'>
#  v = "Olivier"
#  type(v)
# <class 'str'>
#  v=3.2
#  type (v)
# <class 'float'>
#  thislist = ["apple", "banana", "cherry"]
#  print(thislist)
# ['apple', 'banana', 'cherry']
# vu que le premier element de la liste commence a l'index 0
# le fait d'afficher l'elt 1 affiche le deuxieme elt
#  thislist[1]
# 'banana'
# append permet d'ajouter un element a la fin de la liste
#  thislist.append("orange")
#  thislist
# ['apple', 'banana', 'cherry', 'orange']
# del supprime l'elt de le liste a l'index donné
#  del thislist[1]
# thislist[-1] affiche le dernier element de la liste
#  print(thislist[-1])
# orange
#  thislist
# ['apple', 'cherry', 'orange']
#  thislist[0:2]
# ['apple', 'cherry']
# si le debut et la fin ne sont pas spécifiés alors la boule prend
# comme valeurs par defaut l'index 0 et longueur de la liste
# ce qui affiche la liste du debut a la fin
#  thislist[:]
# ['apple', 'cherry', 'orange']
#  thislist[0], thislist[2]
# ('apple', 'orange')
# y = x fait que y pointe sur la tableau [1,2,3]
# ce qui fait que toute modification faite sur y ou x ou z (vu qu'ils pointent sur le même tab)
# fait que le tableau change
#  x = [1,2,3]
#  y = x
#  y[0] = 4
#  x
# [4, 2, 3]
#  y
# [4, 2, 3]
#  z=x
#  z
# [4, 2, 3]
#  z[0] = 1
#  z
# [1, 2, 3]
#  x
# [1, 2, 3]
#  y
# [1, 2, 3]
""" x = [1, 2, 3]
y = x
y[0] = 4
print(x)
print(y)
 """
# Là on copie les valeurs contenues dans x dans le tableau y
# Ce qui crée au debut un tableau y contenant les mêmes valeurs que x
# Mais qui est totalement independant de x
""" x = [1, 2, 3]
y = x[:]
y[0] = 9
print(x)
print(y) """

# La fonction split decoupe la chaine de caracteres en mots
# chaque fois quelle troue un espace (par defaut)
# ici on specifie le char de decoupe qui est :
""" ma_chaine = "Olivier:ENGEL:Strasbourg"
print(ma_chaine.split(":")) """
# Crée une chaine de caracteres avec des : comme separateurs
""" liste = ["Olivier", "ENGEL", "Strasbourg"]
liste = " ".join(liste)
print(f"liste = {liste}") """

# On ne peut pas modifier un tuple ce qui rend
# l'instruction thistuple[1]='blackcurant' fausse
""" thistuple = ('apple', 'banana', 'cherry')
print(thistuple)
print(thistuple[1])
thistuple[1] = 'blackcurant'
print(thistuple)
 """

""" thisdict = {"brand": "Ford",
            "model": "Mustang",
            "year": 1964
            }
print(thisdict)
# x va prendre la valeur Mustang qui est est contenue dans le label model
x = thisdict["model"]
print(x)

# On ajoute la color red a notre dictionnaire
thisdict["color"] = "red"
print(thisdict)

# On supprime le label "model" de notre dictionnaire
del thisdict["model"]
print(thisdict)
 """
 
"-----------------------"
 
 # On lit l'age de l'utilisateur et cast la valeur en entier
age = int(input("Quel est votre age? : "))
print("Vous avez ", age, " ans")
mois = 10

# Formattage du text 
print("Vous avez %d ans et %d mois" % (age, mois))
texte = """Bonjour je m'appelle "Olivier"."""
# fonctionne qu'en python2, les parentheses sont obligatiores sur python3 
# print texte

# Ouvrir un fichier et ajouter du text a la fin (append)
# ecrire les deux lignes et le fermer
f = open("demofile.txt", "a")
f.write("01 Now the file has one more line! \n")
f.write("02 Now the file has one more line!\n")
f.close()
# Ouvrir un fichier en mode lecture 
# afficher le contenu du fichier
f = open("demofile.txt", "r")
print(f.read())

# lire les 5 premiers caracteres contenu dans le fichier
print(f.read(5))
# Lis une ligne a partir de la position courante du curseur
print(f.readline())
# Lis le reste des caracteres a partir de l'index indiqué 
for x in f:
    print(x)

# Ouvre un fichier et ecrit le texte au debut du fichier
f = open("demofile.txt", "w")
f.write('203')
# lis la premiere ligne et la converti en num
f = open("demofile.txt", "r")
num = f.readline()
type(num)
# Convertie en type numerique
n = int(num)
type(num)
type(n)

# Les differentes façons de faire une boucle for
for x in range(6):
    print(x)
# pour x de 2 a 30 pas + 3
for x in range(2, 30, 3):
    print(x)
# quand x = 6 on arrete la boucle et affiche le message "Finally finished"
for x in range(6):
    print(x)
else:
    print("Finally finished!")
# On avance dans les elements du dictionnaire et affiche les key de chaque element
for x in thisdict:
    print(x)
# we Iterate through the element of the dictionary and print each value
for x in thisdict:
    print(thisdict[x])

# While standard
i = 0
while i < 10:
    print("Iteration :", i)
    i = i + 1

# Block de condition
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


#################
# functions
# la fonction prend une variable en parametres et l'affiche avec un texte
# on appelle la fonctions avec des parametres
# les parametres sont requis
def my_function(country):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
#my_function()

# definir une fontions avec parametres par defaut 
# Si aucune variable n'est passée en parametres "France" est passé en parametres 
def my_function(country = "France"):
    print("I am from " + country)
    return len(country)
my_function("Sweden")
my_function("India")
my_function()

# Detecte les erreurs pour pouvoir continuer l'execution du programme meme si une erreur se produit
# s'execute meme s'il y a une erreur 
# Le programme prend en charge le nameError
try:
    print(toto)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# On essaie d'executer le programme
# sinon on fait autre chose, on passe dans le else en l'occurence
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# Le finally s'execute quoi qu'il arrive
try:
    print(toto)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")


##############################################
# modules and scripts
# On importe le module
# Pour les utiliser il faut les specifier avant
import mymodule
mymodule.greeting("myname")

# On importe tout a partie du module math
# On a importé toutes les fonction de math donc pas besoin de les definir
from math import *
sqrt(121)
