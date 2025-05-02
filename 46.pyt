def findposition(xp, xd, yp, yd, zp, zd, t):
    xp = int(input("Enter current x positon: "))
    xd = int(input("Enter destination x position: "))
    t = int(input("Enter time to reach destination: "))
    yp = int(input("Enter current y positon: "))
    yd = int(input("Enter destination y position: "))
    zp = int(input("Enter current z positon: "))
    zd = int(input("Enter destination z position: "))

    for i in range(zp,zd,t):
        print("Probabal time to get there: z :", i)

    for b in range(yp,yd,t):
        print("Probabal time to get there: y :", i)

    for m in range(xp,xd,t):
        print("Probabal time to get there: x :", i)

ask = input("Do you want to find the position of the object or yourself? (yes/no): ")
if ask == "yes":
    findposition(0,0,0,0,0,0,0)
elif ask == "no":
    print("Goodbye!")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")