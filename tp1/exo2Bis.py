from os import F_TEST, write
from random import randint
import json

with open('notes.csv', 'w') as fn:
    for i in range(50):
        student = ({
            'id': i,
            'test1': int(randint(0, 19)),
            'test2': int(randint(0, 19)),
            'test3': int(randint(0, 19)),
            'test4': int(randint(0, 19)),
            'test5': int(randint(0, 19)),
        })
        notes = []
        notes.append(student['test1'])
        notes.append(student['test2'])
        notes.append(student['test3'])
        notes.append(student['test4'])
        notes.append(student['test5'])
        notes.sort()
        k = ((notes[1]+notes[0])*5/100) + ((notes[2]+notes[3]+notes[4])*30/100)
        student["moyenne"] = k
        ligne = json.dumps(student)
        fn.writelines(ligne+"\n")


with open('average.csv', 'w') as fa:
    with open('notes.csv', 'r') as fn:
        avtest1 = 0
        avtest2 = 0
        avtest3 = 0
        avtest4 = 0
        avtest5 = 0
        for line in fn:
            student = json.loads(line)
            avtest1 += student['test1']/50
            avtest2 += student['test2']/50
            avtest3 += student['test3']/50
            avtest4 += student['test4']/50
            avtest5 += student['test5']/50
    avgTest = {
        'avgTest1': avtest1,
        'avgTest2': avtest2,
        'avgTest3': avtest3,
        'avgTest4': avtest4,
        'avgTest5': avtest5,
    }
    ligne = json.dumps(avgTest)
    fa.writelines(ligne)
