# On importe la fonction radint a partir de radom
from random import randint
# On crée une liste de notes ou chaque item est un dictionnaire, chacun contiendra 5 element(5 notes)
student_marks = []
# donner des notes aleatoires a chque etudiant
for i in range(50):
    student_marks.append({"Test1": randint(0, 20),
                          "Test2": randint(0, 20),
                          "Test3": randint(0, 20),
                          "Test4": randint(0, 20),
                          "Test5": randint(0, 20)})
# Inserer les notes dans le fichier
scv = open("note.csv", "a")
for student in student_marks:
    s = f"{student['Test1']}:{student['Test2']}:{student['Test3']}:{student['Test4']}:{student['Test5']}\n"
    scv.write(s)
scv.close()

# Lire le notes de chaque etudiant et les stocker dans une liste
scv = open("note.csv", "r")
notes = []
scv.readline()
for x in scv:
    note = x.rstrip()
    notii = note.split(":")
    notii = [int(i) for i in notii]
    notes.append(notii)
# calculer la moyenne pour chaque etudiant
# on recupere les deux plus petites notes et leur donne un coef de 5
# le reste avec un coef de 30
# On divise la somme sur 100 pour avoir la moyenne
moyens_etud = []
for note in notes:
    a = min(note)
    b = min(set(note).difference([a]))
    c = set(note).difference([a, b])
    sum2 = (a*5+b*5)
    sum1 = {x * 30 for x in c}
    sum1 = sum(sum1)
    moyens_etud.append((sum1 + sum2)/100)
# Pour chaque test on calucle la moyenne
# Pour chaque etudiant on recupere les notes et les ajoute a la liste
# On divise sur 50 pour chaque somme de notes
moyens_tests = [0 for i in range(5)]
for note in student_marks:
    moyens_tests[0] += note["Test1"]
    moyens_tests[1] += note["Test2"]
    moyens_tests[2] += note["Test3"]
    moyens_tests[3] += note["Test4"]
    moyens_tests[4] += note["Test5"]
moyens_tests = [x/50 for x in moyens_tests]

# On insere les moyennes dans le fichier
fmo = open("average.csv", "a")
for s in moyens_etud:
    fmo.write(str(s)+"\n")
st = f"{moyens_tests[0]}:{moyens_tests[1]}:{moyens_tests[2]}:{moyens_tests[3]}:{moyens_tests[4]}\n"
fmo.write(st)
fmo.close()
