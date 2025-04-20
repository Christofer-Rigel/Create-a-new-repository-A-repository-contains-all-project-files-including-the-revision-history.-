# Very simple grader
def Studentmarks():
    Grade_Marks = int(input("Enter your marks for any subject: "))
    
    if Grade_Marks > 110:
        print("You have O+ Grade")
    elif Grade_Marks > 100:
        print("You have O Grade")
    elif Grade_Marks > 95:
        print("You have got A+ Grade")
    elif Grade_Marks > 85:
        print("You have got A Grade")
    elif Grade_Marks > 75:
        print("You have got B+ Grade")
    elif Grade_Marks > 65:
        print("You have got B Grade")
    elif Grade_Marks > 55:
        print("You have got C+ Grade")
    elif Grade_Marks > 45:
        print("You have got C Grade")
    elif Grade_Marks > 35:
        print("You have got D+ Grade")
    elif Grade_Marks > 25:
        print("You have got D Grade")
    elif Grade_Marks > 15:
        print("You have got F+ Grade")
    else:
        print("You have got F Grade")

Studentmarks()

# Grade scale for reference

print("\nGrade Scale:")
print("O+ - Above 110%")
print("O - 100% to 110%")
print("A+ - Above 95%")
print("A - 85% to 95%")
print("B+ - 75% to 85%")
print("B - 65% to 75%")
print("C+ - 55% to 65%")
print("C - 45% to 55%")
print("D+ - 35% to 45%")
print("D - 25% to 35%")
print("F+ - 15% to 25%")
print("F - Below 15%")