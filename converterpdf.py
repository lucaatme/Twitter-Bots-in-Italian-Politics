# convert images to pdf
import os
from PIL import Image

# convert from png


def convert_png_to_pdf(path):
    im = Image.open(path)
    rgb_im = im.convert('RGB')
    rgb_im.save(path.replace('png', 'pdf'))

# convert from jpg
# def convert_jpg_to_pdf(path):
#    im = Image.open(path)
#    rgb_im = im.convert('RGB')
#    rgb_im.save(path.replace('jpg', 'pdf'))

# get path of image


path = '/home/lucaatme/Documents/University/Second Year/First Semester/Advanced Topics/publication/bot_det/finalLegend.png'

convert_png_to_pdf(path)
