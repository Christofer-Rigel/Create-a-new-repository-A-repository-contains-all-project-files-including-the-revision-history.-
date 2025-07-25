def pushZeroesToEnd(a,a_size):
    zero = 0
    nonzero = 0
    while(nonzero!=a_size):
        if a[nonzero] != 0 :
            a[nonzero],a[zero] = a [zero],a[nonzero]
            zero+=1
        nonzero+=1

a = [1,9,2,7,3,53,5,634,53,6,34,7,355,6,4765467,689070,76,32,40,70,0,670,10306076,650760580,6706,80,860780088368,508,66580,464783260]
a_size = len(a)
print(a)
pushZeroesToEnd(a, a_size)
print("Array after pushing all zeroes to end of array")
print(a)