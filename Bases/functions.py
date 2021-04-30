def hello(nom, prenom):
    print(f"Bonjour {prenom} {nom}")


def sum(a, b):
    return (int(a)+int(b))


# Appel direct
hello("Haddadi", "Rayan")
# Appel avec key words
hello(prenom='Rayan', nom='Haddadi')

print(sum(5, 2))
