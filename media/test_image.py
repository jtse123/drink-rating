from PIL import Image
size = (200, 200)
image1 = Image.open('sprite.png')
image1.thumbnail(size, Image.ANTIALIAS)
image1.show()