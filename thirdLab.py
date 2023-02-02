import random


def firstTask(a, b):
    print("a = " + str(a))
    print("b = " + str(b))
    for x in range(a, b+1):
        print(x)


def secondTask(a, b):
    if(a>b):
        for x in range(a, b-1, -1):
            print(x)
    else:
        for x in range(a, b + 1):
            print(x)
def thirdTask(a, b):
    if(a % 2 == 0):
        a -= 1
    for x in range(a, b-1, -2):
        print(x)

firstTask(random.randint(0, 10), random.randint(10, 20));
