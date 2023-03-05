from PIL import Image
im1 = Image.open('Simples\\Bandeira.PNG').resize((500,350))
def roll(im, delta):
    xsize, ysize = im.size
    if delta == 0:
        return im
    part1 = im.crop((0, 0, delta, ysize)) #crop(left, up, right, lower)
    part2 = im.crop((delta, 0, xsize, ysize))
    im.paste(part1, (xsize - delta, 0, xsize, ysize))
    im.paste(part2, (0, 0, xsize - delta, ysize))
    return im

im = roll(im1,200)
im.show()