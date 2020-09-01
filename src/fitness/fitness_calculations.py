from PIL import ImageChops
from PIL import ImageStat
from PIL import ImageFilter
from PIL import ImageEnhance


def calculate_fitness_mean_difference(original_image, generated_image):
    if original_image.width != generated_image.width:
        print('FITNESS ERROR! Images are different.')

    # Calculate difference between two images
    difference = ImageChops.difference(original_image, generated_image)

    # Calculate average brightness of differential image, this tells us how similar those images are
    stats = ImageStat.Stat(difference)
    average_brightness = (stats.mean[0] + stats.mean[1] + stats.mean[2]) / 3

    # Return fitness value
    return (255 - average_brightness) / 255


def calculate_fitness_rms_difference(original_image, generated_image):
    if original_image.width != generated_image.width:
        print('FITNESS ERROR! Images are different.')

    # Calculate difference between two images
    difference = ImageChops.difference(original_image, generated_image)

    # Calculate average brightness of differential image, this tells us how similar those images are
    stats = ImageStat.Stat(difference)
    average_brightness = (stats.rms[0] + stats.rms[1] + stats.rms[2]) / 3

    # Return fitness value
    return (255 - average_brightness) / 255


def calculate_fitness_blur_mean_difference(original_image, generated_image):
    if original_image.width != generated_image.width:
        print('FITNESS ERROR! Images are different.')

    # Calculate difference between two images
    original_image = ImageEnhance.Contrast(original_image).enhance(1.5)
    generated_image = ImageEnhance.Contrast(generated_image).enhance(1.5)
    difference = ImageChops.difference(original_image, generated_image)

    # Blur image
    difference = difference.filter(ImageFilter.BLUR())

    # Calculate average brightness of differential image, this tells us how similar those images are
    stats = ImageStat.Stat(difference)
    average_brightness = (stats.rms[0] + stats.rms[1] + stats.rms[2]) / 3

    # Return fitness value
    return (255 - average_brightness) / 255


def calculate_fitness_contrast_mean_difference(original_image, generated_image):
    if original_image.width != generated_image.width:
        print('FITNESS ERROR! Images are different.')

    # Increase contrast of images
    original_image = ImageEnhance.Contrast(original_image).enhance(1.5)
    generated_image = ImageEnhance.Contrast(generated_image).enhance(1.5)

    # Calculate difference between two images
    difference = ImageChops.difference(original_image, generated_image)

    # Calculate average brightness of differential image, this tells us how similar those images are
    stats = ImageStat.Stat(difference)
    average_brightness = (stats.rms[0] + stats.rms[1] + stats.rms[2]) / 3

    # Return fitness value
    return (255 - average_brightness) / 255
