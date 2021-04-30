import random
from math import *


def nearest_points(filename, user_point):
    # definir le pattern qui va generer les labels des points
    pattern = ["R", "D"]
    points = []
    # on gener 200 points de maniere aleatoire
    for i in range(200):
        label = random.randint(0, 1)
        x = random.randint(1, 1000)
        y = random.randint(1, 1000)
        points.append({pattern[label]: (x, y)})
    # pour chaque point on ecrit le pattern et la coordinate dans le fichier csv
    fi = open(filename, "a")
    for point in points:
        for a in point:
            x, y = point[a]
            fi.write(a + ":" + str(x) + "," + str(y) + "\n")
    fi.close()

    # On crée une liste de points depuis le fichier csv
    # chaque point est un dictionnaire qui contient le label et les coordonnés de chaque point
    points_f = []
    fi = open(filename, "r")
    for x in fi.readlines():
        lb = x[0]
        x = x.lstrip(lb + ":")
        x = x.rstrip("\n")
        a, b = x.split(",")
        points_f.append({"label": lb, "x": int(a), "y": int(b)})

    # on prend l'input de l'utilisateur et on crée un point
    # Pour chaque point on calcule la distance
    # On stock le resultat dans une liste qui contient le point et la distance
    x, y = user_point
    x = int(x)
    y = int(y)
    distances = [[sqrt((point["x"] - x) ** 2 + (point["y"] - y) ** 2), point["label"], point["x"], point["y"]] for point
                 in points_f]

    # On prend les 5 poits les plus proches et on les stock dans une liste
    min_dist = []
    for i in range(5):
        min_dist.append(min(distances))
        distances.remove(min(distances))
    print(min_dist)
    r = [1 for point in min_dist if point[1] == "R"]
    r = sum(r)
    d = 5-r
    if r < d:
        return "D"
    else:
        return "R"


print(nearest_points("po.csv", [500, 260]))
