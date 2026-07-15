import cv2
import numpy as np
import colorama
def apply_color_r_g_b_filter(image ,filter_choice):
    filtered_image = image.copy()
    if filter_choice == 'red' or filter_choice == 'r' or filter_choice == 'R' or filter_choice == 'Red':
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0
    elif filter_choice == 'green' or filter_choice == 'g' or filter_choice == 'G' or filter_choice == 'Green':
        filtered_image[:, :, 2] = 0
        filtered_image[:, :, 0] = 0
    elif filter_choice == 'blue' or filter_choice == 'b' or filter_choice == 'B' or filter_choice == 'Blue':
        filtered_image[:, :, 2] = 0
        filtered_image[:, :, 1] = 0
    elif filter_choice == 'Intense Red' or filter_choice == 'Intense red' or filter_choice == 'intense red' or filter_choice == 'Intense Red' or filter_choice == 'IR' or filter_choice == 'ir' or filter_choice == 'Ir':
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 100)
    elif filter_choice == 'Intense Green' or filter_choice == 'Intense green' or filter_choice == 'intense green' or filter_choice == 'Intense Green' or filter_choice == 'IG' or filter_choice == 'ig' or filter_choice == 'Ig':
        filtered_image[:, :, 2] = 0
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 1] = cv2.add(filtered_image[:, :, 1], 100)
    elif filter_choice == 'Intense Blue' or filter_choice == 'Intense blue' or filter_choice == 'intense blue' or filter_choice == 'Intense Blue' or filter_choice == 'IB' or filter_choice == 'ib' or filter_choice == 'Ib':
        filtered_image[:, :, 2] = 0
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = cv2.add(filtered_image[:, :, 0], 100)
    elif filter_choice == 'Yellow' or filter_choice == 'yellow' or filter_choice == 'YELLOW' or filter_choice == 'Y' or filter_choice == 'y':
        filtered_image[:, :, 2] = 0
        filtered_image[:, :, 1] = cv2.add(filtered_image[:, :, 1], 100)
        filtered_image[:, :, 0] = cv2.add(filtered_image[:, :, 0], 100)
    else:
        raise ValueError("Invalid filter choice. Please choose 'red', 'green', or 'blue'.")
image = "C:\\Users\\Aditya\\Desktop\\HTML designs\\Python_ig\\example.jpg"
image = cv2.imread(image)
if image is None:
    print("Please enter an actual image path.")
else:
    print("IMFOUND:1108")
    print("Welcome to the Color R-G-B Filter protochoice")
    print("Select fromt he folowing options:")
    print(colorama.Fore.RED + "1. Red")
    print(colorama.Fore.GREEN + "2. Green")
    print(colorama.Fore.BLUE + "3. Blue")
    print(colorama.Fore.LIGHTRED_EX + "4. Intense Red")
    print(colorama.Fore.LIGHTGREEN_EX + "5. Intense Green")
    print(colorama.Fore.LIGHTBLUE_EX + "6. Intense Blue")
    print(colorama.Fore.YELLOW + "7. Yellow")
    while True:
        filtered_image = apply_color_r_g_b_filter(image, 'red')

        key = cv2.waitKey(1) & 0xFF
        
        filter_type = input("Enter the number corresponding to the desired filter: ")
        if filter_type == '1':
            filtered_image = apply_color_r_g_b_filter(image, 'red')
            break
        elif filter_type == '2':
            filtered_image = apply_color_r_g_b_filter(image, 'green')
            break
        elif filter_type == '3':
            filtered_image = apply_color_r_g_b_filter(image, 'blue')
            break
        elif filter_type == '4':
            filtered_image = apply_color_r_g_b_filter(image, 'Intense Red')
            break
        elif filter_type == '5':
            filtered_image = apply_color_r_g_b_filter(image, 'Intense Green')
            break
        elif filter_type == '6':
            filtered_image = apply_color_r_g_b_filter(image, 'Intense Blue')
            break
        elif filter_type == '7':
            filtered_image = apply_color_r_g_b_filter(image, 'Yellow')
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
    cv2.imshow("Filtered Image", filtered_image)
cv2.DestroyAllWindows()
