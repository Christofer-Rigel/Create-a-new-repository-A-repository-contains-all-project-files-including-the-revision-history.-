import cv2
import matplotlib.pyplot as plt
import colorama

colorama.init(autoreset=True)

# Load image
image = cv2.imread("example.jpg")

# Check if image loaded correctly
if image is None:
    print(colorama.Fore.RED +
          "ERROR: Could not find 'example.jpg'.")
    exit()


def ask_user_choice():
    print(colorama.Fore.GREEN +
          "\nWhat function do you want to perform?\n")

    print(colorama.Fore.YELLOW + "1. Convert to Grayscale")
    print(colorama.Fore.YELLOW + "2. Crop the Image")
    print(colorama.Fore.YELLOW + "3. Rotate the Image")
    print(colorama.Fore.YELLOW + "4. Resize the Image")
    print(colorama.Fore.YELLOW + "5. Apply Blur Filter")

    choice = input(
        colorama.Fore.CYAN + "Enter your choice (1-5): "
    )

    return choice


def show_image(img, title="Image", gray=False):
    plt.figure(figsize=(8, 6))

    if gray:
        plt.imshow(img, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    plt.title(title)
    plt.axis("off")
    plt.show()


def perform_function(choice, image):

    try:

        # 1. Grayscale
        if choice == "1":
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            show_image(gray_image, "Grayscale Image", gray=True)

        # 2. Crop
        elif choice == "2":

            h, w = image.shape[:2]

            print(colorama.Fore.GREEN +
                  f"Image dimensions: Width={w}, Height={h}")

            x1 = int(input("Top-left X: "))
            y1 = int(input("Top-left Y: "))
            x2 = int(input("Bottom-right X: "))
            y2 = int(input("Bottom-right Y: "))

            # Validation
            if x1 < 0 or y1 < 0 or x2 > w or y2 > h:
                print(colorama.Fore.RED +
                      "Coordinates are outside image bounds.")
                return

            if x1 >= x2 or y1 >= y2:
                print(colorama.Fore.RED +
                      "Invalid crop coordinates.")
                return

            cropped = image[y1:y2, x1:x2]
            show_image(cropped, "Cropped Image")

        # 3. Rotate
        elif choice == "3":

            angle = float(
                input("Enter rotation angle (degrees): ")
            )

            h, w = image.shape[:2]
            center = (w // 2, h // 2)

            matrix = cv2.getRotationMatrix2D(
                center,
                angle,
                1.0
            )

            rotated = cv2.warpAffine(image, matrix, (w, h))

            show_image(rotated, "Rotated Image")

        # 4. Resize
        elif choice == "4":

            width = int(input("Enter new width: "))
            height = int(input("Enter new height: "))

            if width <= 0 or height <= 0:
                print(colorama.Fore.RED +
                      "Width and height must be positive.")
                return

            resized = cv2.resize(image, (width, height))

            show_image(resized, "Resized Image")

        # 5. Blur
        elif choice == "5":

            kernel = int(
                input("Enter odd kernel size (e.g. 5): ")
            )

            # GaussianBlur requires odd numbers
            if kernel % 2 == 0 or kernel <= 0:
                print(colorama.Fore.RED +
                      "Kernel size must be a positive odd number.")
                return

            blurred = cv2.GaussianBlur(
                image,
                (kernel, kernel),
                0
            )

            show_image(blurred, "Blurred Image")

        else:
            print(colorama.Fore.RED +
                  "Invalid choice. Enter 1-5.")

    except ValueError:
        print(colorama.Fore.RED +
              "Invalid input. Numbers only please.")

    except Exception as e:
        print(colorama.Fore.RED +
              f"Unexpected error: {e}")


def main():

    print(colorama.Fore.GREEN +
          "Welcome to IPT Prototype v2")

    print(colorama.Fore.YELLOW +
          "Basic image processing because apparently Photoshop costs money.\n")

    choice = ask_user_choice()

    perform_function(choice, image)

    print(colorama.Fore.CYAN +
          "\nProgram finished.")


if __name__ == "__main__":
    main()