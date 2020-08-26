from os import path

from PIL import Image

dir_path = path.join(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))), 'images')


def read_image(image_name):
    file_path = path.join(dir_path, image_name)
    return Image.open(file_path)


def save_image(image, name, file_extention='png'):
    image.save('{}/{}.{}'.format(dir_path, name, file_extention))
