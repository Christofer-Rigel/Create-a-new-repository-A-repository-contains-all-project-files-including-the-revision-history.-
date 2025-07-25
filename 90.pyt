def Maxlenghtbecuasewearetoodistratedtodoit(a,a_size):
    counter = 0 # why we need this I can count  1,2,3,...37827387
    maxOnes = 0

    for i in range(0,a_size):#I hope this works
        if (a[i] == 0):
            counter = 0
        else:
            counter += 1
            MaxOnes = max(maxOnes, counter)
    return maxOnes
a = [1,1,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,1,1,0,1,0,1,1,0,1,0,1,0,1]
a_size = len(a)
print("max 1's:",Maxlenghtbecuasewearetoodistratedtodoit(a,a_size))