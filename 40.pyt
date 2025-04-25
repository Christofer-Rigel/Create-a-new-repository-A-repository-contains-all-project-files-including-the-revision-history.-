def swap(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("After swapping: a =", a, "b =", b)

def swap1 (a, b):
    a = (a & b) + (a | b)
    b = a + (~b) +1
    a = a + (~b) + 1
    print("After swapping: a =", a, "b =", b)

swap(6572365289564789267826892365, 87962389653479895275689)
swap1(15678342536974862789658732658, 237532658326857235687265982081224)