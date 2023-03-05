from PIL import Image

im = Image.linear_gradient('L')
im2 = Image.radial_gradient('L')

im.show()
im2.show()