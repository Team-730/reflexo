from PIL import Image
from transforms import RGBTransform # from source code mentioned above

lena = Image.open("sticker1.jpg")
lena = lena.convert('RGB') # ensure image has 3 channels
lena