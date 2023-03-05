from PIL import Image
im1 = Image.open('Simples\\Bandeira.PNG').resize((500,350))
x,y = im1.size

caixas = [(0,0,int(x/2),int(y/2)),(int(x/2),0,x,int(y/2)), (0,int(y/2),int(x/2),y), (int(x/2),int(y/2),x,y)]

for caixa in caixas:
    croped = im1.crop(caixa).rotate(180)
    im1.paste(croped, caixa)

im1.show()  