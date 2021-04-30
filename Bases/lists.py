noms = ['Rayan', 'Mourtada', 'Ghilas']
# Afficher la liste
print(noms)
# Index d'un element
a = noms.index('Rayan')
print(a)
# Debue et fin d'affichage
print(noms[0:2])
print(noms[:])
# Le mot le plus long dans la liste
pg = noms[0]
for item in noms:
    if len(item) > len(pg):
        pg = item
print(f"Le plus long prenom est : {pg}")
