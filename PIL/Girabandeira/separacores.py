#importar o "separacores.py" traz as funções: maxval() tops() corespresentes() isolacor(), cujas descrições estão abaixo
from PIL import Image
def maxval(d): #função que retorna a key de maior valor de um dicionario
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]
def tops(dicio,max): #retorna as top(max) keys de maiores valores de um dicionario (usado pra encontrar a cor mais recorrente)
    dicio_aux = dicio
    tops = list()
    i=0
    while i<max:
        tops.append(maxval(dicio_aux))
        dicio_aux.pop(maxval(dicio_aux))
        i+=1
    return tops
def corespresentes(image): #retorna as top 4 cores presentes na imagem 
    imgpix = image.getdata()
    cores = dict()
    for pixel in list(imgpix):
        if pixel not in cores:
            cores[pixel]=0
        else:
            cores[pixel]+=1
    cores = tops(cores,4)
    return cores
def isolacor(image,cor): #isola uma cor específica da imagem, retorna uma nova imagem somente com os píxeis da cor selecionada
    imgpix = image.getdata()
    pixelcor = [i for i, pixel in enumerate(imgpix) if pixel == cor] #índices dos píxels da cor
    imgnovapix = []
    for i,pixel in enumerate(imgpix):
        if i not in pixelcor:
            imgnovapix.append((0,0,0,0))
        else:
            imgnovapix.append(pixel)
    img2 = Image.new('RGBA',image.size)
    img2.putdata(imgnovapix)
    return img2

if __name__ == '__main__':
    im = Image.open("Girabandeira\\Capturar.PNG")
    #im = Image.open("StenographicImg\\praia.png")
    im = im.resize((int(250*1.2),int(175*1.2)))
    cores = corespresentes(im)
    #print("As cinco cores presentes na imagem em maior quantidade são:\n" + str(cores))
    #cor = input("Entre a cor que deseja isolar da forma R G B A separados por espaços: ")
    #cor = tuple([int(cor) for cor in cor.split(' ')])
    #cores = [(0, 156, 59, 255), (255, 223, 0, 255), (0, 39, 118, 255), (255, 255, 255, 255)]
    for cor in cores:
        imgnova = isolacor(im,cor)
        imgnova.show()
    im.show()