from image_processing.helper_functions import save_image, read_image
from fitness.fitness_calculations import calculate_fitness_mean_difference
from points_model.image_model import ImageModel
from genetics.cross_prob import example_cross_prob_func, example_cross_prob_func2
from genetics.mutation_prob import all_mutate
from genetics.mutations import example_mutation_func, mirror_mutation_func
from image_processing.resizing import generate_scaled_images, resize_image
from image_processing.triangles_to_image import convert_triangles_to_image
import copy
import sys

sys.setrecursionlimit(10000)


def do_algorithm(image_name, scale_step, img_number, fitness_goal):
    img = read_image(image_name + '.jpg')
    width = img.width
    height = img.height

    image_model = ImageModel(all_mutate, example_cross_prob_func2, mirror_mutation_func)

    image_model.cross_model()
    tp = image_model.get_triangles()
    ip = convert_triangles_to_image(tp, (width, height))
    save_image(ip, 'beginning')

    fitness = 0
    last_fitness = 0
    last_i = 0
    crosses_count = 2
    max_crosses = 7
    mutation_type = 1
    i = 0
    while True:
        if i % 100 == 0 and i != 0:
            print()
            print('iterations: ' + str(i))
            print('fitness: ' + str(fitness))
            print('fitness goal: ' + str(fitness_goal))
            print('fitness diff:', fitness - last_fitness)
            print('mutation type:', mutation_type)
            print('crosses:', crosses_count)
            if fitness != 0 and last_fitness != 0:
                if fitness - last_fitness < 0.00001:
                    t = image_model.get_triangles()
                    i2 = convert_triangles_to_image(t, (width, height))
                    save_image(i2, 'res' + str(crosses_count))
                    print('ii')
                    print(fitness, last_fitness)
                    if mutation_type == 3:
                        if crosses_count < max_crosses:
                            image_model.cross_model()
                        fitness = 0
                        crosses_count += 1
                        mutation_type = 1
                    else:
                        mutation_type += 1
            last_fitness = fitness

        if i % 500 == 0:
            t = image_model.get_triangles()
            i2 = convert_triangles_to_image(t, (width, height))
            save_image(i2, 'result')
            # print()
            # print("saved result")
        if fitness > fitness_goal or crosses_count > max_crosses:
            t = image_model.get_triangles()
            i2 = convert_triangles_to_image(t, (width, height))
            save_image(i2, 'result')
            break

        new_image_model = copy.deepcopy(image_model)
        new_image_model.mutate_model(mutation_type=mutation_type)
        new_i2 = convert_triangles_to_image(new_image_model.get_triangles(), (width, height))
        new_fitness = calculate_fitness_mean_difference(img, new_i2)
        if new_fitness > fitness:
            fitness = new_fitness
            image_model = new_image_model

        i = i + 1


do_algorithm('mona_color', 0.7, 6, 0.98)
