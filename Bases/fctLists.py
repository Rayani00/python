numeros = [2, 5, 7]
# Ajouter un element au debut
numeros.insert(0, 10)
# Ajouter un element a la fin
numeros.append(5)
print(numeros)
# Supprimer un element
numeros.remove(2)
print(numeros)
# Supprimer le dernier
numeros.pop()
print(numeros)
# Voir si un element existe ou pas dans la liste
print(50 in numeros)
# Occurence d'un element
print(numeros.count(5))
# Trier la liste croissant
numeros.sort()
print(numeros)
# Trier la liste decroissant
numeros.sort()
numeros.reverse()
print(numeros)
# Faire une copie d'une liste
numerosCpy = numeros.copy()
print(f"Numero {numeros} sa copie est numeroCpy {numerosCpy}")
# Eliminer les doublons
n = [2, 2, 6, 3, 6, 8, 9, 6]
unique = []
for elt in n:
    if elt not in unique:
        unique.append(elt)

print(f"La liste {n} sans doublons est {unique}")

# Triche
point = (2, -1, 5)
x, y, z = point
print(f"Les coordonnés du point sont ({x},{y},{z})")
