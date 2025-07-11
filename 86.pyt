def leaders(a, a_size):
    currentmax = a[a_size-1]
    print(currentmax)

    for i in range(a_size-2 , -1 , -1):
        if currentmax < a[i]:
            currentmax = a[i]
            print(a[i])
            currentmax = a[i]

a = [16,17,4,3,5,245]
leaders(a, len(a))
