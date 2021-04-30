# Files object
# When we use the with it closes the file automatically at the end
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')
with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents, end="*")
    # Retourne la position du pointeur
    print(f.tell())


with open('test2.txt', 'w') as f:
    f.write("Fork")
    f.seek(1)
    f.write('u')
    f.seek(2)
    f.write('c')

with open('test2.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)
