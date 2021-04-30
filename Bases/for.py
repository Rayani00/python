for item in 'Rayan':
    print(item)

print('------------------')

for item in [1, 2, 3, 4, 5]:
    print(f"{item}")

print('------------------')

somme = 0
for item in range(0, 10+1, 2):
    somme += item
    print(item)

print(f"La somme est {somme}")

# Nested looos
for x in range(5+1):
    for y in range(5+1):
        print(f"({x},{y})")
