import cv2

image = cv2.imread("C:/purdue/datamine/elanco/resource/ex_3.jpg")
# image_blur = cv2.GaussianBlur(image, (45, 45), 0)
# image_grey = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# image_canny = cv2.Canny(image_grey, 20, 50)
# image_canny_2 = cv2.Canny(image, 20, 50)

# Resize image variables (width,height,dimension)
width = 450
height = 400

# Tuple structure (int,int) specific to python
dim = (width, height)

# Resize images
# resize takes parameters (source,dimensions,estimation method)
resized = cv2.resize(image, dim, cv2.INTER_AREA)
# resized_blur = cv2.resize(image_blur, dim, cv2.INTER_AREA)
# resized_grey = cv2.resize(image_grey, dim, cv2.INTER_AREA)
# resized_canny = cv2.resize(image_canny, dim, cv2.INTER_AREA)
# resized_canny_2 = cv2.resize(image_canny_2, dim, cv2.INTER_AREA)

# cv2.imshow("Blur image", resized_blur)
cv2.imshow("Original image", resized)
# cv2.imshow("grey image", resized_grey)
# cv2.imshow("canny image", resized_canny)
# cv2.imshow("canny image with grey", resized_canny_2)
cv2.waitKey(0)