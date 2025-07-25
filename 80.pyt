def print2largestbecause1isoverated(a,a_size):
    largest = secondLargest = -314748364487653897
    for i in range(a_size):

        if (a[i] > largest):
            secondLargest = largest
            largest = a[i]

        elif (a[i] > secondLargest and a[i] != largest):
            secondLargest = a[i]

    print(secondLargest)

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
a_size = len(a)
print2largestbecause1isoverated(a, a_size)