# -*- coding: utf-8 -*-


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# TODO здесь ваш код

import simple_draw as sd


sd.resolution = (1200, 600)

def draw_figure(start_point, end_point, angles_count, line_length):
    point = sd.get_point(start_point, end_point)
    angle = 360 // angles_count

    for i in range(angles_count):
        point_draw = sd.get_vector(start_point=point, angle=i * angle, length=line_length)
        point_draw.draw()
        point = point_draw.end_point


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
