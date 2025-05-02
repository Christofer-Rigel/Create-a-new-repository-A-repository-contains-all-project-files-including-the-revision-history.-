import math 
def printPowerSize(set,Setsize):
    PowerSetSize = (int) (math.pow(2, Setsize))
    outer = 0
    inner = 0
    for outer in range(0, PowerSetSize):
        for inner in range(0, Setsize):
            if (outer & (1 << inner)) > 0:
                print(set[inner], end = " ")
        print("")
size = int(input("Enter the size of the set: "))

set = []

for i in range(0,size):
    n = int(input("Enter the element of the set: "))
    set.append(n)

printPowerSize(set , len(set))