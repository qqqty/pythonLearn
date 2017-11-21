from PIL import Image


img = Image.open('sourse/1.jpg')
img = img.resize((250, 156), Image.ANTIALIAS)


img.save('sourse/1_py.jpg')