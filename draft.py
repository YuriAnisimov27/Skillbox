import simple_draw as sd

sd.resolution = (1200, 600)


def draw_figure(start_point, end_point, angles_count, line_length):
    point = sd.get_point(start_point, end_point)
    angle = 360 // angles_count

    for i in range(angles_count):
        point_draw = sd.get_vector(start_point=point, angle=i * angle, length=line_length)
        point_draw.draw()
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


N = int(input('''Возможные фигуры:
0. Треугольник
1. Квадрат
2. Пятиугольник
3. Шестиугольник
Введите желаемую фигуру > 
'''))
while N < 0 or N > 3:
    print('Вы ввели некорректный номер!')
    N = int(input('Введите желаемую фигуру > '))

draw_figure(200, 200, N + 3, 200)
sd.pause()
