from PIL import ImageChops
from PIL import ImageStat


def calculate_fitness(original_image, generated_image):
    # Calculate difference between two images
    difference = ImageChops.difference(original_image, generated_image)

    # res = 0
    # for x in range(difference.width):
    #     for y in range(difference.height):
    #         val = 0
    #         val += difference.getpixel((x, y))[0]
    #         val += difference.getpixel((x, y))[1]
    #         val += difference.getpixel((x, y))[2]
    #         res += val**2
    #
    # # max_val = (255*3)**2*difference.width*difference.height
    # res = 1.0 / (res + 1)


    # Calculate average brightness of differential image, this tells us how similar those images are
    stats = ImageStat.Stat(difference)
    average_brightness = (stats.mean[0] + stats.mean[1] + stats.mean[2])/3

    # Calculate fitness value
    fitness = (255 - average_brightness) / 255

    # Use squaring to emphasise small changes when images are very similar
    # fitness = fitness ** 2
    # print(res)
    # return res
    return fitness
