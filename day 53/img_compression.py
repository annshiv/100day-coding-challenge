from PIL import Image
import numpy

im = Image.open("lena_gray.jpg")

pixelMap = im.load()

img = Image.new(im.mode, im.size)
pixel = img.load()

for i in range(img.size[0]):
    for l in range(img.size[1]):
        if(pixelMap[i,j]>=0 and pixelMap[i.j]<=31):
            pixel[i,j] = 0
        elif(pixelMap[i,j]>=32 and pixelMap[i.j]<=63):
            pixel[i,j] = 1
        elif(pixelMap[i,j]>=64 and pixelMap[i.j]<=95):
            pixel[i,j] = 2
        elif(pixelMap[i,j]>=96 and pixelMap[i.j]<=127):
            pixel[i,j] = 3
        elif(pixelMap[i,j]>=128 and pixelMap[i.j]<=159):
            pixel[i,j] = 4
        elif(pixelMap[i,j]>=160 and pixelMap[i.j]<=191):
            pixel[i,j] = 5
        elif(pixelMap[i,j]>=192 and pixelMap[i.j]<=223):
            pixel[i,j] = 6
        elif(pixelMap[i,j]>=224 and pixelMap[i.j]<=255):
            pixel[i,j] = 7

img.save("compressed.png")