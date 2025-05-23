def railded(n, num):
    if n > num:
        return
    print(n)
    railded(n + 1, num)
n = int(input("Enter the number: "))
railded(1, n)