from PIL import Image

img= Image.open("StenographicImg\\outputs\\esteno.png")
pix2=list(img.getdata())
msg_bin_out = []

for posicao in range (0, ((len(pix2))-1)):
    for cor in range(0,4):
        cor_bin=bin(pix2[posicao][cor]) #cor da posição pix[posicao][cor] para binario
        lsb2=cor_bin[-2:].replace('b','0')
        msg_bin_out.append(lsb2)
    posicao+=1

msg_binf = ''.join(msg_bin_out)

def b2str(s):
    temp_h=hex(int(s,2))
    temp_hb = bytearray.fromhex(temp_h[2:])
    decod=temp_hb.decode("utf-8",'ignore')
    return decod   

with open("StenographicImg\\outputs\\decodificado.txt", "w", encoding="utf-8") as saída:
    mensagemfoto = b2str(msg_binf)
    saída.write(mensagemfoto)
    saída.close()