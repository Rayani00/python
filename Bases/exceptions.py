try:
    age = int(input('Age : '))
    income = 20000
    risk = income//age
    print(age)
except ValueError:
    print("Valeur invalide")
except ZeroDivisionError:
    print("Age ne doit pas être égal a zéro")
