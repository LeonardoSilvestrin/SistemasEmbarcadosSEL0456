from PIL import Image
import numpy

def rodacirculo(imagem, x, y, raio, angulo):
    box = (x-raio, y-raio, x+raio+1, y+raio+1) #caixa que inscreve o círculo
    crop = imagem.crop(box=box)
    crop_arr = numpy.asarray(crop)
    # criando a máscara circular 
    mask = numpy.zeros((2*raio+1, 2*raio+1)) # máscara = quadrado de zeros
    for i in range(crop_arr.shape[0]):
        for j in range(crop_arr.shape[1]):
            if (i-raio)**2 + (j-raio)**2 <= raio**2:
                mask[i,j] = 1 #seta todos os pixeis fora do raio para 1
    # cria a imagem ciruclar
    sub_img_arr = numpy.empty(crop_arr.shape ,dtype='uint8') #subimage do formato da original
    sub_img_arr[:,:,:3] = crop_arr[:,:,:3] #iguala os pixeis da subimagem aos pixeis do quadrado 
    sub_img_arr[:,:,3] = mask*255 #aplica a imagem circular ao quadrado, restando somente o circulo
    sub_img = Image.fromarray(sub_img_arr, "RGBA").rotate(angulo) #reprinta o circulo na imagem, mas girado
    i2 = imagem.copy()
    i2.paste(sub_img, box[:2], sub_img.convert('RGBA'))
    return i2

if __name__ == '__main__':
    im = Image.open("Girabandeira\\Capturar.PNG")
    #im = im.resize((500,350))
    x = int(im.size[0]/2)
    y = int(im.size[1]/2)
    im2 = rodacirculo(im,x,y,400,90)
    im.show()
    im2.show()