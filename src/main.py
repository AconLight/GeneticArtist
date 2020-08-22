from image_processing.helper_functions import resize_image, save_image, read_image
from fitness.fitness_calculations import calculate_fitness

image = resize_image(0.1, 'duck.jpg')
save_image(image, 'smaller_duck')

i1 = read_image('duck.jpg')
i2 = read_image('hen.jpg')
fitness = calculate_fitness(i1, i2)
print(fitness)
