from PIL import ImageChops
from PIL import ImageStat


def calculate_fitness(original_image, generated_image):
    # Calculate difference between two images

    if original_image.width != generated_image.width:
        print('dupa')

    difference = ImageChops.difference(original_image, generated_image)

    # res = 0
    # for x in range(difference.width):
    #     for y in range(difference.height):
    #         val = 0
    #         val += difference.getpixel((x, y))[0]
    #         val += difference.getpixel((x, y))[1]
    #         val += difference.getpixel((x, y))[2]
    #         res += val
    #
    # max_val = (255*3)*difference.width*difference.height
    # res = (max_val - res) / max_val


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
