from image_processing.helper_functions import save_image, read_image
from fitness.fitness_calculations import calculate_fitness_mean_difference
from points_model.image_model import ImageModel
from genetics.cross_prob import example_cross_prob_func
from genetics.mutation_prob import all_mutate
from genetics.mutations import example_mutation_func
from image_processing.resizing import generate_scaled_images, resize_image
from image_processing.triangles_to_image import convert_triangles_to_image
import copy


def do_algorithm(image_name, scale_step, img_number, fitness_goal):
    img = read_image(image_name + '.jpg')
    width = img.width
    height = img.height

    image_model = ImageModel(all_mutate, example_cross_prob_func, example_mutation_func)

    for i in range(8):
        image_model.cross_model()

    fitness = 0
    last_i = 0
    i = 0
    while True:
        if i % 100 == 0:
            print()
            print('iterations: ' + str(i))
            print('fitness: ' + str(fitness))
            print('fitness goal: ' + str(fitness_goal))
        if i % 500 == 0:
            t = image_model.get_triangles()
            i2 = convert_triangles_to_image(t, (width, height))
            save_image(i2, 'result')
            print()
            print("saved result")
        if fitness > fitness_goal or i > 20000:
            t = image_model.get_triangles()
            i2 = convert_triangles_to_image(t, (width, height))
            save_image(i2, 'result')


        new_image_model = copy.deepcopy(image_model)
        new_image_model.mutate_model()
        new_i2 = convert_triangles_to_image(new_image_model.get_triangles(), (width, height))
        new_fitness = calculate_fitness_mean_difference(img, new_i2)
        if new_fitness > fitness:
            fitness = new_fitness
            image_model = new_image_model

        i = i + 1


do_algorithm('mona_color', 0.7, 6, 0.98)
