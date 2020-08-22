from PIL import ImageChops


def calculate_fitness(original_image, generated_image):
    # ta funkcja nam zwraca obrazek przedstawiający różnicę między podanymi obrazkami jakoś to trzeba ewaluować
    return ImageChops.difference(original_image, generated_image).getbbox()
