from PIL import ImageChops
from PIL import ImageStat


def calculate_fitness(original_image, generated_image):
    # Calculate difference between two images
    difference = ImageChops.difference(original_image, generated_image)

    # Calculate average brightness of differential image, this tells us how similar those images are
    stats = ImageStat.Stat(difference)
    average_brightness = stats.mean[0]

    # Calculate fitness value
    fitness = (255 - average_brightness) / 255

    # Use squaring to emphasise small changes when images are very similar
    # fitness = fitness ** 2

    return fitness
