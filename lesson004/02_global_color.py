# -*- coding: utf-8 -*-

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# TODO здесь ваш код

import simple_draw as sd

sd.resolution = (1200, 600)


def draw_figure(start_point, end_point, angles_count, line_length, color):
    point = sd.get_point(start_point, end_point)
    angle = 360 // angles_count

    for i in range(angles_count):
        point_draw = sd.get_vector(start_point=point, angle=i * angle, length=line_length)
        point_draw.draw(color=color, width=3)
        point = point_draw.end_point


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
