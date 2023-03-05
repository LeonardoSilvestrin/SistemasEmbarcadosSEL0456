from PIL import Image

im1 = Image.open('Simples\\Bandeira.PNG').resize((500,350))
im2 = Image.open('Simples\\eesc.PNG').resize((500,350))
mask = im2

im3 = Image.composite(im1,im2,mask)

im1.show()
mask.show()
im3.show()


#result = mask * image1 + (1 - mask) * image2