
# image enhancement CLAME
import cv2

# Read the image
img = cv2.imread('47012233_2033599033605076_2922733714603507712_o.jpg')

# preparation for CLAHE
clahe = cv2.createCLAHE()

# Convert to gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply enhancement
enh_img = clahe.apply(gray_img)

# save it to a file
cv2.imwrite('Annshiv.jpg', enh_img)

print('Enhancing completed)