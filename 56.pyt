def deadred(n , num):
    if n > num : 
        return
    deadred( n + 1 , num)
    print(n)
n = int(input("Enter the number that governs how much ammo is used to end the zombies: "))
deadred(1 , n)