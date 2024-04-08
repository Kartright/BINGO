import random

def randNumArr(low,high):
    arr = []
    for i in range(0, 5):

        x = random.randint(low,high)
        while (x in arr):
            x = random.randint(low,high)

        arr.append(x)
    return arr

def displayBoard(b,i,n,g,o):
    print("="*31)
    print("|  B  |  I  |  N  |  G  |  O  |")
    print("="*31)
    for j in range(0, 5):
        print("-"*31)
        print("|  " + str(b[j]).ljust(3) + "|  " + str(i[j]) + " |  " + str(n[j]).ljust(2) + " |  " + str(g[j]) + " |  " + str(o[j]) + " | ")
    print("-"*31)



if __name__ == "__main__":
    choice = input("How many boards would you like to make? ")
    for i in range(0, int(choice)):
        b = randNumArr(1,15)
        i = randNumArr(16,30)
        n = randNumArr(31,45)
        n[2] = "X"
        g = randNumArr(46,60)
        o = randNumArr(61,75)
        displayBoard(b,i,n,g,o)
        print("\n")