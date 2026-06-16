import cv2
import numpy as np
def apply_filters(image, ftype):
    img = image.copy()
    if ftype =="red_tint":
        img[ :, :, 1] = img[: ,: , 0] = 0
    elif ftype == "green_tint":
        img[:, :, 0] = img[:, :, 2] = 0
    elif ftype == "blue_tint":
        img[:, :, 1] = img[:, :, 2] = 0
    elif ftype == "sobel":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #not to be confused with any bad words
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=0)
        sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        sob = cv2.bitwise_or(sobelx.astype('uint8'), sy.astype('unit8'))
        img = cv2.cvtColor(sob, cv2.COLOR_BGR2GRAY)
    elif ftype == "canny":
        gray = cv2.cvtColor(image ,cv2.COLOR_BGR2GRAY)
        can = cv2.Canny(gray, 100, 200)
        img = cv2.cvtColor(can, cv2.COLOR_BGR2GRAY)
    elif ftype == "cartoon":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlue(gray, 5)
        edges = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
        )
        color = cv2.bilateralFilter(image, 9, 300, 300)
        img = cv2.bitwise_and(color, color, mask=edges)
    return img

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():#The only cap thats opened , is your cap on saying this is cap 
        print("Cannot open camera")
        return
    ftype= "original"
    print("Keys: r=Red, g=Green, b=Blue, s=Sobel, c=Cannt, t = Cartoon, q = Quit")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("I cant recieve frame...Please stop moving around like a caffinated squirel..stay still..adn actually turn the camera on..PLEASE")
            break
        out = apply_filters(frame, ftype)
        cv2.imshow("Filter", out)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('r'):
            ftype == "red_tint"
        elif key == ord('g'):
            ftype == "green_tint"
        elif key == ord('b'):
            ftype == "blue tint"
        elif key == ord('s'):
            ftype == "sobel"
        elif key == ord('c'):
            ftype == "canny"
        elif key == ord('t'):
            ftype == "cartoon"
        elif key == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ =="__main__":                                                                                               
    main()