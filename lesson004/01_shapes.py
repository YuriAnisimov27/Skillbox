# -*- coding: utf-8 -*-


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код

import simple_draw as sd
sd.resolution = (1200, 600)


def draw_3_angle(start_point, end_point, angle, line_length):
    point = sd.get_point(start_point, end_point)
    for i in range(3):
        point_draw = sd.get_vector(start_point=point, angle=i * angle, length=line_length)
        point_draw.draw()
        point = point_draw.end_point


def draw_4_angle(start_point, end_point, angle, line_length):
    point = sd.get_point(start_point, end_point)
    for i in range(4):
        point_draw = sd.get_vector(start_point=point, angle=i * angle, length=line_length)
        point_draw.draw()
        point = point_draw.end_point


def draw_5_angle(start_point, end_point, angle, line_length):
    point = sd.get_point(start_point, end_point)
    for i in range(5):
        point_draw = sd.get_vector(start_point=point, angle=i * angle, length=line_length)
        point_draw.draw()
        point = point_draw.end_point


def draw_6_angle(start_point, end_point, angle, line_length):
    point = sd.get_point(start_point, end_point)
    for i in range(6):
        point_draw = sd.get_vector(start_point=point, angle=i * angle, length=line_length)
        point_draw.draw()
        point = point_draw.end_point


draw_3_angle(100, 100, 120, 100)
draw_4_angle(300, 100, 90, 100)
draw_5_angle(600, 100, 72, 100)
draw_6_angle(900, 100, 60, 100)
sd.pause()

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


def draw_figure(start_point, end_point, angles_count, line_length):
    point = sd.get_point(start_point, end_point)
    angle = 360 // angles_count
    for i in range(angles_count):
        point_draw = sd.get_vector(start_point=point, angle=i * angle, length=line_length)
        point_draw.draw()
        point = point_draw.end_point


