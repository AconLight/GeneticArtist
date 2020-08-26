from image_processing.helper_functions import save_image, read_image
from fitness.fitness_calculations import calculate_fitness
from image_processing.resizing import generate_scaled_images, resize_image

image = resize_image(0.1, 'duck.jpg')
save_image(image, 'smaller_duck')

i1 = read_image('hen_slight_change.jpg')
i2 = read_image('hen.jpg')

fitness = calculate_fitness(i1, i2)

generate_scaled_images(i1)
