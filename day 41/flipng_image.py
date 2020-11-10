#flipping the image

from PIL import Image

#importing the image

img = Image.open('47012233_2033599033605076_2922733714603507712_o.jpg')

#transposing
transpos_image = img.transpose(Image.FLIP_LEFT_RIGHT)

transpos_image.save('correct.jpg')

print("Done fliping")