from PIL import Image
im1 = Image.open('Simples\\Bandeira.PNG')
im1.show()


#apresentar: rotate() resize() convert() 

# filter(): from PIL import ImageFilter
#ImageFilter.DETAIL, ImageFilter.BLUR, ...

#from PIL import ImageFilter 
#im1 = Image.open('Simples\\Bandeira.PNG').filter(ImageFilter.BLUR)
#im1.show()

#enhance(): from PIL import ImageEnhance

#from PIL import ImageEnhance
#im_en = ImageEnhance.Contrast(im1)
#im_en.enhance(1.3).show()