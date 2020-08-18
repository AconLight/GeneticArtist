from os import path

from PIL import Image

dir_path = path.join(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))), 'images')

def read_image(image_name):
    file_path = path.join(dir_path, image_name)
    return Image.open(file_path) 

def resize_image(resize_factor, image_name):
    image = read_image(image_name)
    new_width = int(round(image.width * resize_factor))
    new_height = int(round(image.height * resize_factor))
    return image.resize((new_width, new_height))

def save_image(image, name, file_extention = 'png'):
    image.save('{}/{}.{}'.format(dir_path, name, file_extention))

