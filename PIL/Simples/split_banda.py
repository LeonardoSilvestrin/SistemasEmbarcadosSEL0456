from PIL import Image
im1 = Image.open('Simples\\Bandeira.PNG').resize((500,350))

fonte = im1.split() #divide a imagem em bandas
r, g, b, a = 0,1,2,3
im_nova = Image.merge('RGBA',(fonte[g],fonte[b],fonte[r],fonte[a])) #nova imagem trocando os valores das bandas RGBA -> GBRA
im_nova.show()

# Mudando regiões específicas da imagem

mascara = fonte[b].point(lambda azul: azul > 90 and 255) #seleciona as regiões onde o azul é maior que 90
out_red = fonte[r].point(lambda vermelho: vermelho*0+255) #leva o vermelho para 255
out_blue = fonte[b].point(lambda azul: azul*0) #leva o azul para zero

fonte[r].paste(out_red,None, mascara) #aplica as alterações de vermelho na regiao da máscara
fonte[b].paste(out_blue,None, mascara) # ''   ''   ''       ''  azul    ''   ''   ''  ''

im_nova_vermelho = Image.merge(im1.mode,(fonte[r],fonte[g],fonte[b],fonte[a])) #cria a nova imagem que troca azul por vermelho
im_nova_vermelho.show()