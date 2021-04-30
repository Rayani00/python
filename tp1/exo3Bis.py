import json
import random
from random import randint


with open('points.csv', 'w') as fp:
    for i in range(200):
        L = ['R', 'D']
        label = random.choice(L)
        point = ({
            'label': label,
            'x': randint(0, 1000),
            'y': randint(0, 1000),
        })
        ligne = json.dumps(point)
        fp.writelines(ligne+"\n")
