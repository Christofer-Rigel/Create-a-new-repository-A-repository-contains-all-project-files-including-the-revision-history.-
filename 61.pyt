def checksorted(a):
    lenght = len(a)
    if lenght == 1 or lenght == 0:
        return True
    return a[0] <= a[1] and checksorted(a[1:])
x = int(input("Enter array: "))
a = x

if checksorted(a):
    print("\nYes given array is sorted")
else:
    print("\nNo given array is not sorted")