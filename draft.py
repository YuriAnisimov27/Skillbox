import simple_draw as sd

sd.resolution = (1200, 600)


def draw_figure(start_point, end_point, angles_count, line_length, color):
    point = sd.get_point(start_point, end_point)
    angle = 360 // angles_count

    for i in range(angles_count):
        point_draw = sd.get_vector(start_point=point, angle=i * angle, length=line_length)
        point_draw.draw(color=color, width=3)
        point = point_draw.end_point


# point1 = sd.get_vector(start_point=point, angle=0, length=line_length)
# point1.draw()
# point2 = sd.get_vector(start_point=point1.end_point, angle=60, length=line_length)
# point2.draw()
# point3 = sd.get_vector(start_point=point2.end_point, angle=120, length=line_length)
# point3.draw()
# point4 = sd.get_vector(start_point=point3.end_point, angle=180, length=line_length)
# point4.draw()
# point5 = sd.get_vector(start_point=point4.end_point, angle=240, length=line_length)
# point5.draw()
# point6 = sd.get_vector(start_point=point5.end_point, angle=300, length=line_length)
# point6.draw()




colors = {
    'COLOR_RED': (255, 0, 0),
    'COLOR_ORANGE': (255, 127, 0),
    'COLOR_YELLOW': (255, 255, 0),
    'COLOR_GREEN': (0, 255, 0),
    'COLOR_CYAN': (0, 255, 255),
    'COLOR_BLUE': (0, 0, 255),
    'COLOR_PURPLE': (255, 0, 255),
    'COLOR_DARK_YELLOW': (127, 127, 0),
    'COLOR_DARK_ORANGE': (127, 63, 0),
    'COLOR_DARK_RED': (127, 0, 0),
    'COLOR_DARK_GREEN': (0, 127, 0),
    'COLOR_DARK_CYAN': (0, 127, 127),
    'COLOR_DARK_BLUE': (0, 0, 127),
    'COLOR_DARK_PURPLE': (127, 0, 127),
}

for i, item in enumerate(colors, start=1):
    print(i, item)
my_color = int(input('Введите желаемый цвет > '))
while my_color < 1 or my_color > 14:
    print('Вы ввели некорректный номер!')
    my_color = int(input('Введите желаемый цвет > '))

colors_list = [
    'COLOR_RED',
    'COLOR_ORANGE',
    'COLOR_YELLOW',
    'COLOR_GREEN',
    'COLOR_CYAN',
    'COLOR_BLUE',
    'COLOR_PURPLE',
    'COLOR_DARK_YELLOW',
    'COLOR_DARK_ORANGE',
    'COLOR_DARK_RED',
    'COLOR_DARK_GREEN',
    'COLOR_DARK_CYAN',
    'COLOR_DARK_BLUE',
    'COLOR_DARK_PURPLE',
]



draw_figure(200, 200, 4, 200, colors[colors_list[my_color - 1]])
sd.pause()
