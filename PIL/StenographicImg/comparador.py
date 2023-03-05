from PIL import Image

img1 = Image.open("StenographicImg\\fonte.png")
img2 = Image.open("StenographicImg\\outputs\\esteno.png")

pix1 = list(img1.getdata())
pix2 = list(img2.getdata())

pix3 = []
for i,n in enumerate(pix1):
    listatemp = []
    for k in range(0,4):
        listatemp.append(50*abs(pix1[i][k]-pix2[i][k]))
    tuplatemp = tuple(listatemp)
    pix3.append(tuplatemp)

novafoto=Image.new('RGBA', img1.size)
novafoto.putdata(pix3)
novafoto.save("StenographicImg\\outputs\\compara.png")