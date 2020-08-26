from image_processing.helper_functions import resize_image, save_image, read_image
from fitness.fitness_calculations import calculate_fitness
from points_model.image_model import ImageModel
from genetics.cross_prob import example_cross_prob_func
from genetics.mutation_prob import example_mutation_prob_func
from genetics.mutations import example_mutation_func

image = resize_image(0.1, 'duck.jpg')
save_image(image, 'smaller_duck')

i1 = read_image('hen_slight_change.jpg')
i2 = read_image('hen.jpg')

fitness = calculate_fitness(i1, i2)
print(fitness)

image_model = ImageModel(example_mutation_prob_func, example_cross_prob_func, example_mutation_func)

for i in range(100):
    image_model.mutate_model()
    image_model.cross_model()

