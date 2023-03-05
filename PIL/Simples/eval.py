from PIL import Image

im = Image.open('Simples\\Bandeira.PNG')
im = im.convert('RGB')

im2 = Image.eval(im,(lambda pix: 255-pix))

im.show()
im2.show()