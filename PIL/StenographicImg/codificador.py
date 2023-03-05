from PIL import Image

img= Image.open("StenographicImg\\fonte.png")
pix=list(img.getdata())
img2 = img
pixmsg=pix

with open("StenographicImg\\mensagem.txt", encoding='utf-8') as texto:
    msg = texto.read()
msg_bin = ''.join(format(ord(i), '08b') for i in msg) #transforma todos os chars da msg em binarios de 8bits

pos_mes=0 #posição da mensagem que estou passando para a foto

for pos_foto in range(0, len(pix)):
    listatemp=list(pix[pos_foto]) #lista temporararia pq tupla não altera
    for cor in range(0,4):
        cor_bin=bin(pix[pos_foto][cor]) #cor da posição pix[pos_foto][cor] para binario
        if pos_mes+2 <= len(msg_bin):
            cor_novo_b=cor_bin[0:len(cor_bin)-2]+msg_bin[pos_mes:pos_mes+2] #altera 2 LSB
            cor_novo = int(cor_novo_b,2) #cor novo para b2d
            listatemp[cor] = cor_novo #c'ésimo item da lista vira a nova cor
            pos_mes +=2
    pixmsg[pos_foto] = tuple(listatemp)
    pos_foto+=1

novafoto=Image.new('RGBA', img.size)
novafoto.putdata(pixmsg)
novafoto.save("StenographicImg\\outputs\\esteno.png")