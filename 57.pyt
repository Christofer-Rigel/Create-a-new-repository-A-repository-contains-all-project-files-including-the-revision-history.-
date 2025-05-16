def railded(n, num):
    if n > num:
        return
    print(n)
    railded(n + 1, num)
n = int(input("Enter the number that governs how much ammo is used to end the zombies: "))
railded(1, n)