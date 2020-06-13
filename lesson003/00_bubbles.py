# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код

point = sd.get_point(100, 100)
radius = 50
for i in range(4):
    sd.circle(point, radius + 5 * i)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код

def paint_bubbles(x, y, radius, bubbles_count):
    point = sd.get_point(x, y)
    for i in range(bubbles_count):
        sd.circle(point, radius + 5 * i)

paint_bubbles(700, 300, 50, 20)

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

for i in range(10):
    point = sd.get_point(50 + i * 84, 50 + 50 * i)
    sd.circle(point, 50)

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

for i in range(10):
    for j in range(3):
        point = sd.get_point(50 + i * 100, 50 + 100 * j)
        sd.circle(point, 50)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

for i in range(100):
    point = sd.random_point()
    sd.random_color()
    radius = random.randint(2, 33)
    sd.circle(point, radius, width=3, color=sd.random_color())

sd.pause()


