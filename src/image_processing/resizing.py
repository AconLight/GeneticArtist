import PIL.Image

from image_processing.helper_functions import read_image


def resize_image(resize_factor, image_name):
    image = read_image(image_name)
    new_width = int(round(image.width * resize_factor))
    new_height = int(round(image.height * resize_factor))
    return image.resize((new_width, new_height))


def generate_scaled_images(image, scale_step=2, threshold=20):
    scaled_images = [image]
    while min(scaled_images[0].size) >= threshold:
        previous_size = scaled_images[0].size
        new_width = int(round(previous_size[0] / scale_step))
        new_height = int(round(previous_size[1] / scale_step))
        new_scale = (new_width, new_height)
        scaled_image = scaled_images[0].resize(new_scale, PIL.Image.ANTIALIAS)
        scaled_images.insert(0, scaled_image)
    return scaled_images
