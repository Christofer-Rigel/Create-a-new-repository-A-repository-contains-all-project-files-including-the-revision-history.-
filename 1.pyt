order_amount = int(input("Please tell how many times you would like to order:   "))

while order_amount > 0:
    order_number = int(input("Please enter a number between 1 and 10 based on your craving:  "))
    
    if order_number == 1:
        print("Ok, ordering KFC for you.")
    elif order_number == 2:
        print("Ok, ordering PIZZA for you.")
    elif order_number == 3:
        print("Ok, ordering PASTA for you.")
    elif order_number == 4:
        print("Ok, ordering DOSA for you.")
    elif order_number == 5:
        print("Ok, ordering SOMETHING SWEET for you.")
    elif order_number == 6:
        print("Ok, ordering BRISKET for you.")
    elif order_number == 7:
        print("Ok, ordering A ALIEN INVASION for you.")
    elif order_number == 8:
        print("Ok, ordering COLD BEVERAGE for you.")
    elif order_number == 9:
        print("Ok, ordering HOT BEVERAGE for you.")
    elif order_number == 10:
        print("Ok, ordering A ICBM for you.")
    else:
        print("Sorry, can't find anything to match your craving : ")
    
    order_amount -= 1  # Decrement order_amount by 1

print("All orders have been placed.")
