from image_processing.helper_functions import  resize_image, save_image

image = resize_image(0.1, 'duck.jpg')
save_image(image, 'smaller_duck')