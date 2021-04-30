is_hot = True
age = input("Indiquez votre age ")
age = int(age)
if age < 18:
    print(f"Mineur, votre age {age}")
elif age <= 80 and age >= 18:
    print(f"Adulte, votre age {age}")
else:
    print(f"Vieux, votre age {age}")
