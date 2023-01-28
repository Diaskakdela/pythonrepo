def firstTask(a, b):
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

thirdTask(18, 9)
