from image_processing.helper_functions import save_image, read_image
from fitness.fitness_calculations import calculate_fitness
from points_model.image_model import ImageModel
from genetics.cross_prob import example_cross_prob_func
from genetics.mutation_prob import example_mutation_prob_func
from genetics.mutations import example_mutation_func
from image_processing.resizing import generate_scaled_images, resize_image
from image_processing.triangles_to_image import convert_triangles_to_image
import copy


def do_algorithm(image_name, scale_step, img_number, fitness_goal):
    img = read_image(image_name + '.jpg')
    scale = 600 / img.width

    first_image_to_compare = resize_image(img, scale)
    save_image(first_image_to_compare, 'temp1', file_extention='jpg')

    images_to_compare = generate_scaled_images(first_image_to_compare, scale_step)

    width = first_image_to_compare.width
    height = first_image_to_compare.height

    image_model = ImageModel(example_mutation_prob_func, example_cross_prob_func, example_mutation_func)

    for i in range(8):
        image_model.cross_model()

    fitness = 0
    last_i = 0
    best_images_to_compare_idx = 0
    images_to_compare_idx = 0
    i = 0
    while True:
        if i % 100 == 0:
            print()
            print('iterations: ' + str(i))
            print('image_numer: ' + str(images_to_compare_idx))
            print('fitness: ' + str(fitness))
            print('fitness goal: ' + str(fitness_goal))
        if fitness > 0.5 + fitness_goal * images_to_compare_idx / (
                img_number - 1) / 2 or i - last_i > 2000*(images_to_compare_idx+1) / img_number:
            last_i = i
            images_to_compare_idx = images_to_compare_idx + 1
            t = image_model.get_triangles()
            i2 = convert_triangles_to_image(t,
                                            (int(width / ((1 / scale_step) ** (
                                                        img_number - 1 - best_images_to_compare_idx))),
                                             int(height / ((1 / scale_step) ** (
                                                         img_number - 1 - best_images_to_compare_idx)))))
            save_image(i2, 'result')

            if images_to_compare_idx >= img_number:
                break
            images_to_compare_idx = min(images_to_compare_idx, img_number)

            image_model.cross_model()
            new_i2 = convert_triangles_to_image(image_model.get_triangles(),
                                                (int(width / ((1 / scale_step) ** (
                                                            img_number - 1 - images_to_compare_idx))), int(height / (
                                                            (1 / scale_step) ** (
                                                                img_number - 1 - images_to_compare_idx)))))
            print()
            fitness = calculate_fitness(images_to_compare[images_to_compare_idx], new_i2)
            continue


        new_image_model = copy.deepcopy(image_model)
        new_image_model.mutate_model()
        new_i2 = convert_triangles_to_image(new_image_model.get_triangles(),
                                            (
                                            int(width / ((1 / scale_step) ** (img_number - 1 - images_to_compare_idx))),
                                            int(height / (
                                                        (1 / scale_step) ** (img_number - 1 - images_to_compare_idx)))))
        new_fitness = calculate_fitness(images_to_compare[images_to_compare_idx], new_i2)
        if new_fitness > fitness:
            # last_i = int((i + last_i*5)/6)
            best_images_to_compare_idx = images_to_compare_idx
            fitness = new_fitness
            image_model = new_image_model

        i = i + 1


do_algorithm('circle', 0.7, 6, 0.98)
