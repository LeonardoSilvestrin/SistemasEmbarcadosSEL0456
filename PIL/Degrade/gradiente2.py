from PIL import Image
import numpy

im = Image.open("Degrade\\bandeira.PNG")
im2 = Image.open("Degrade\\palmeiras.PNG")
im = im.resize((500,350))
im2 = im2.resize((500,350))
im_matriz1 = numpy.asarray(im)
im_matriz2 = numpy.asarray(im2)
a=0


def sigmoid(x):
    return 1/(1+numpy.exp(x))

im_nova_matriz = im_matriz1
for coluna in range(im_matriz1.shape[1]):
    for linha in range(im_matriz1.shape[0]):
        im_nova_matriz[linha][coluna] = a*im_matriz2[linha][coluna]+(1-a)*im_matriz1[linha][coluna]
    #a = coluna/im_matriz1.shape[1]
    a = sigmoid(coluna-im_matriz1.shape[1]/2)
    #a = .5
im_nova = Image.fromarray(im_nova_matriz,'RGBA')
im_nova.show()
