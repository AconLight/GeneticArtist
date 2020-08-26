from PIL import Image, ImageDraw


def map_points(percentage_points, image_size):
    width = image_size[0]
    height = image_size[1]
    points = []
    for percentage_point in percentage_points:
        point = (int(round(percentage_point[0] * width)), int(round(percentage_point[1] * height)))
        points.append(point)
    return points


def average_color(colors):
    averaged_r = int(round((colors[0][0] + colors[1][0] + colors[2][0]) / 3))
    averaged_g = int(round((colors[0][1] + colors[1][1] + colors[2][1]) / 3))
    averaged_b = int(round((colors[0][2] + colors[1][2] + colors[2][2]) / 3))
    return averaged_r, averaged_g, averaged_b


def convert_triangles_to_image(triangles, image_size):
    image = Image.new('RGB', image_size)

    draw = ImageDraw.Draw(image)
    for triangle in triangles:
        points = map_points(triangle['points'], image_size)
        color = average_color(triangle['colors'])
        draw.polygon(points, fill=color)
    return image


t = [{'points': [(0, 0), (0.8, 0.8), (0.2, 0.8)], 'colors': [(255, 0, 0), (255, 255, 0), (0, 0, 0)]}]
convert_triangles_to_image(t, (600, 400))
