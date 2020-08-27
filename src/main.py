from image_processing.helper_functions import save_image, read_image
from fitness.fitness_calculations import calculate_fitness
from points_model.image_model import ImageModel
from genetics.cross_prob import example_cross_prob_func
from genetics.mutation_prob import example_mutation_prob_func
from genetics.mutations import example_mutation_func
from image_processing.resizing import generate_scaled_images, resize_image
from image_processing.triangles_to_image import convert_triangles_to_image

import copy

image = resize_image(0.1, 'duck.jpg')
save_image(image, 'smaller_duck', file_extention='jpg')

i1 = read_image('hen_slight_change.jpg')

image_model = ImageModel(example_mutation_prob_func, example_cross_prob_func, example_mutation_func)

for i in range(6):
    image_model.cross_model()

t = image_model.get_triangles()
i2 = convert_triangles_to_image(t, (1024, 684))
fitness = calculate_fitness(i1, i2)

last_i = 0
for i in range(2000):
    if i % 100 == 0:
        print(str(i))
    if i - last_i > 200:
        last_i = i
        image_model.cross_model()
        continue

    new_image_model = copy.deepcopy(image_model)
    new_image_model.mutate_model()
    new_i2 = convert_triangles_to_image(new_image_model.get_triangles(), (1024, 684))
    new_fitness = calculate_fitness(i1, new_i2)
    if new_fitness > fitness:
        last_i = i
        fitness = new_fitness
        image_model = new_image_model
        print(fitness)




t = image_model.get_triangles()
print(str(t))

i2 = convert_triangles_to_image(t, (1024, 684))

fitness = calculate_fitness(i1, i2)
print(fitness)

save_image(i2, 'siema')
