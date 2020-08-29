def resize_image(image, scale_step):
    new_width = int(round(image.width * scale_step))
    new_height = int(round(image.height * scale_step))
    return image.resize((new_width, new_height))


def generate_scaled_images(image, scale_step=2, threshold=10):
    scaled_images = [image]
    while min(scaled_images[0].size) >= threshold:
        scaled_image = resize_image(scaled_images[0], scale_step)
        scaled_images.insert(0, scaled_image)
    return scaled_images
