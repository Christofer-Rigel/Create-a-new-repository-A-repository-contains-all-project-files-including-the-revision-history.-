import cv2
image = cv2.imread("Simple.png")
cv2.namedWindow('abc',cv2.WINDOW_NORMAL)
cv2.resizeWindow('abc', 800, 500)
cv2.imshow('abc', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(f"Image dimensions: {image.shape}")