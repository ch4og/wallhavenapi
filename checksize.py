from PIL import Image
import os

images = os.listdir('walls')
for image in images:
    im = Image.open('walls/'+image)
    width, height = im.size
    if width > 3840 or height > 2160:
        img = im.resize((width//2, height//2), Image.Resampling.LANCZOS)
        img.save('wallsresized/'+image)