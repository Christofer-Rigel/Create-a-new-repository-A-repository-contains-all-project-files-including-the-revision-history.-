def ONsquareTime(n) :
    iteration = 0
    for i in range(0,n) :
        for j in range(0,n) :
           print("+", end ="  ")
           iteration += 1
    print("")
    print("when n is", n, "Total iteration : ", iteration)
ONsquareTime(10)
ONsquareTime(20)
ONsquareTime(30)
print("/n with any 'n' the time taken will be equal to n^2")
print("O(n^2)")