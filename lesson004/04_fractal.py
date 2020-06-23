# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,
sd.resolution = (1200, 600)
root_point = sd.get_point(300, 0)


def draw_branches(start_point, angle, length):
    v1 = sd.get_vector(start_point=start_point, angle=angle - 30, length=length)
    v1.draw()
    v2 = sd.get_vector(start_point=start_point, angle=angle + 30, length=length)
    v2.draw()

draw_branches(root_point, 90, 100)
# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

sd.resolution = (1300, 600)
root_point = sd.get_point(600, 0)


def draw_bunches(start_point, angle, length):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle - 15, length=length)
    v1.draw()
    v2 = sd.get_vector(start_point=start_point, angle=angle + 15, length=length)
    v2.draw()
    length = length * 0.75
    angle1 = angle + 30
    angle2 = angle - 30
    draw_bunches(v1.end_point, angle1, length)
    draw_bunches(v2.end_point, angle2, length)

draw_bunches(root_point, 90, 160)
sd.pause()


# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.resolution = (1300, 600)


def draw_bunches(start_point, angle, length):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=start_point, angle=angle - 15, length=length)
    v1.draw()
    v2 = sd.get_vector(start_point=start_point, angle=angle + 15, length=length)
    v2.draw()
    length = length * (0.75 * sd.random_number(-20, 20) / 100 + 0.75)
    angle1 = angle + (30 * sd.random_number(-40, 40) / 100 + 30)
    angle2 = angle - (30 * sd.random_number(-40, 40) / 100 + 30)
    draw_bunches(v1.end_point, angle1, length)
    draw_bunches(v2.end_point, angle2, length)


root_point = sd.get_point(600, 30)
draw_bunches(start_point=root_point, angle=90, length=160)
sd.pause()

