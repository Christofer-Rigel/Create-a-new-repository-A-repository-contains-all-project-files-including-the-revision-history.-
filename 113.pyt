#an interactive application that enables users to upload an image, apply different edge detection techniques, experiment with various filters, and visualize the results. The application will allow real-time adjustments to parameters like threshold values and kernel sizes, giving users hands-on experience with OpenCV.
import cv2
import numpy as np
from matplotlib import pyplot as plt
def apply_canny(image, low_threshold, high_threshold):
    edges = cv2.Canny(image, low_threshold, high_threshold)
    return edges
def apply_sobel(image, kernel_size):
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=kernel_size)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=kernel_size)
    sobel_combined = cv2.magnitude(sobelx, sobely)
    return sobel_combined
def apply_laplacian(image, kernel_size):
    laplacian = cv2.Laplacian(image, cv2.CV_64F, ksize=kernel_size)
    return laplacian
def main():
    image_path = input("Enter the path to the image: ")
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Error: Image not found.")
        return
    while True:
        print("\nChoose an edge detection technique:")
        print("1. Canny")
        print("2. Sobel")
        print("3. Laplacian")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            low_threshold = int(input("Enter low threshold: "))
            high_threshold = int(input("Enter high threshold: "))
            edges = apply_canny(image, low_threshold, high_threshold)
            plt.imshow(edges, cmap='gray')
            plt.title('Canny Edges')
            plt.show()
        elif choice == '2':
            kernel_size = int(input("Enter kernel size (odd number): "))
            sobel_edges = apply_sobel(image, kernel_size)
            plt.imshow(sobel_edges, cmap='gray')
            plt.title('Sobel Edges')
            plt.show()
        elif choice == '3':
            kernel_size = int(input("Enter kernel size (odd number): "))
            laplacian_edges = apply_laplacian(image, kernel_size)
            plt.imshow(laplacian_edges, cmap='gray')
            plt.title('Laplacian Edges')
            plt.show()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":    main()               