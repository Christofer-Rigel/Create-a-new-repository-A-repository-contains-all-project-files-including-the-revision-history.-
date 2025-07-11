def roations(a, n, a_size):
    for i in range(n):
        rotate(a, a_size)

def rotate(a,a_size):
    temp = a[0]
    for i in range(a_size-1):
        a[i] = a[i + 1]
        a[a_size-1]  = temp

def printarray(a, a_size):
    for i in range(a_size):
        print("% d", a[i],end=" ")
    print("\n")

a = [8467647,7,645,475767,5,8,57,84,64,8,45,76367,547,54,8,47,8,6,8,6,8,7,68,2,4756547,8,5757,763,75,8,65,8,6,47575,898,65]
printarray(a,len(a))
roations(a, 2, len(a))
printarray(a,len(a))