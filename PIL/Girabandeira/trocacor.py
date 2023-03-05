from PIL import Image 
import separacores as sp

def trocacor(imagem, cor_sai,cor_entra):
    img_data = list(imagem.getdata())
    img_nova_data = list()
    for pixel in img_data:
        if pixel == cor_sai:
            img_nova_data.append(cor_entra)
        else:
            img_nova_data.append(pixel)
    img_nova = Image.new('RGBA',imagem.size)
    img_nova.putdata(img_nova_data)
    return img_nova

if __name__ == '__main__':
    im = Image.open("Girabandeira\\Capturar.PNG")
    print("As 10 cores mais presentes na imagem são: \n" + str(sp.corespresentes(im)))
    im2 = trocacor(im,sp.corespresentes(im)[0],(255,0,0,255))
    im.show()
    im2.show()