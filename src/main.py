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


i1 = resize_image(4, 'mona.jpg')
save_image(i1, 'circle2', file_extention='jpg')

i2 = resize_image(0.5, 'circle2.jpg')
save_image(i2, 'hen_slight_change2', file_extention='jpg')

i3 = resize_image(0.5, 'hen_slight_change2.jpg')
save_image(i3, 'hen_slight_change3', file_extention='jpg')

i4 = resize_image(0.5, 'hen_slight_change3.jpg')
save_image(i4, 'hen_slight_change4', file_extention='jpg')

i5 = resize_image(0.5, 'hen_slight_change4.jpg')
save_image(i5, 'hen_slight_change5', file_extention='jpg')


i11 = [
    i5, i4, i3, i2, i1
]

# width = 1600
# height = 1597

# width = 1024
# height = 684

width = 143*4
height = 188*4

image_model = ImageModel(example_mutation_prob_func, example_cross_prob_func, example_mutation_func)

print(str(2**0))

for i in range(6):
    image_model.cross_model()

# t = image_model.get_triangles()
# first = convert_triangles_to_image(t, (width, height))
# fitness = calculate_fitness(i1, first)

fitness = 0

print(fitness)

last_i = 0
best_i11idx = 0
i11idx = 0
i = 0
while True:
    if i % 100 == 0:
        print(str(i))
        print(str(i11idx))
        print(fitness)
        print((57 + i11idx*8)/100)
    if fitness > (57 + i11idx*8)/100 or i - last_i > 500:
        print('dupa')
        last_i = i
        i11idx = i11idx + 1

        t = image_model.get_triangles()
        print(str(t))
        print(best_i11idx)
        i2 = convert_triangles_to_image(t,
                                        (int(width / (2 ** (4 - best_i11idx))), int(height / (2 ** (4 - best_i11idx)))))

        fitness = calculate_fitness(i11[best_i11idx], i2)
        print(fitness)

        save_image(i2, 'siema')

        if i11idx > 4:
            break
        i11idx = min(i11idx, 4)
        i1 = i11[i11idx]
        image_model.cross_model()
        new_i2 = convert_triangles_to_image(image_model.get_triangles(),
                                            (int(width / (2 ** (4 - i11idx))), int(height / (2 ** (4 - i11idx)))))

        fitness = calculate_fitness(i11[i11idx], new_i2)
        continue

    new_image_model = copy.deepcopy(image_model)
    new_image_model.mutate_model()
    new_i2 = convert_triangles_to_image(new_image_model.get_triangles(), (int(width / (2**(4-i11idx))), int(height / (2**(4-i11idx)))))
    new_fitness = calculate_fitness(i11[i11idx], new_i2)
    if new_fitness > fitness:
        #last_i = int((i + last_i*5)/6)
        best_i11idx = i11idx
        fitness = new_fitness
        image_model = new_image_model
        print(fitness)

    i = i+1





