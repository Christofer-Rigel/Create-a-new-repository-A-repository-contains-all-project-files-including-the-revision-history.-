import cv2
import numpy as np
import matplotlib.pyplot as plt
#Loading the img
def display_image(title, image):
    plt.figure(figsize=(8, 6))
    if len(image.shape) == 1:  # Grayscale image
        plt.imshow(image, cmap='gray')
    elif len(image.shape) == 2:  # Color image 
        plt.imshow(image)
    else:
        raise ValueError(f"{image}Has no colors/has colors that cannot be transformed in the current program.")
    plt.title(title)
def interactive_edge_detection(image):
    image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if image is None:
        raise ValueError("The current image that you have attempted to edit has not been recognized or found, or it is invalid. If you want to continue using this program, please give us something to work with that can be used and is in constraints. Else, the program will not be able to function and will throw this error, which I personally don't want you to hear this error again, so I don't have to continue saying this error over and over to you who keep on uploading the same image.")
        return
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image("Original Image", image)
    print("Select an option:")
    print("1 : Sobel Edge Detection")
    print("2 : Canny Edge Detection")
    print("3 : Laplacian Edge Detection")
    print("4 : Gaussian Smoothing")
    print("5: Median Filtering")
    print("6 : Exit")
    print("a-z or A-z or any chracters: speak with our attendant, aka The Error.")
    print("Anything else , like nonsencial unicode: TO make this code run , go to the top right corner of the screen , click the x , and stop making our program cry")

    while True:
        choice = input("Enter you choice..and dont give me a headache")
        if choice == '1':
            sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)
            sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)
            sobel_edges = cv2.magnitude(sobelx, sobely)
            display_image("Sobel Edge Detection", sobel_edges)
        elif choice == '2':
            canny_edges = cv2.Canny(gray_image, 100, 200)
            display_image("Canny Edge Detection", canny_edges)
        elif choice == '3':
            laplacian_edges = cv2.Laplacian(gray_image, cv2.CV_64F)
            display_image("Laplacian Edge Detection", laplacian_edges)

        elif choice == '4':
            gaussian_blur = cv2.GaussianBlur(image, (15, 15), 0)
            kernel_size = 15
            display_image("Gaussian Smoothing", gaussian_blur)

        elif choice == '5':
            median_blur = cv2.medianBlur(image, 15)
            display_image("Median Filtering", median_blur)

        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        elif choice.isalpha():
            print("Just close the program brother")
            break
        else:
            print("How did you get this error...Idk , just stop pls")
def display_image(title, image):
    plt.figure(figsize=(8, 6))
    if len(image.shape) == 1:  # Grayscale image
        plt.imshow(image, cmap='gray')
    elif len(image.shape) == 2:  # Color image 
        plt.imshow(image)
    else:
        raise ValueError(f"{image}Has no colors/has colors that cannot be transformed in the current program.")
    plt.title(title)
    plt.show()
interactive_edge_detection(cv2.imread(r"C:\Users\Aditya\Desktop\HTML designs\Python_ig\117.jpg"))
