# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код

for y in range(10):
    for x in range(10):
        if y % 2 == 0:
            point_a = simple_draw.get_point(100 * x, 50 * y)
            point_b = simple_draw.get_point(100 * x + 100, 50 * y + 50)
            simple_draw.rectangle(point_a, point_b, width=3)
        if y % 2 != 0:
            point_a = simple_draw.get_point(100 * x + 50, 50 * y)
            point_b = simple_draw.get_point(100 * x + 150, 50 * y + 50)
            simple_draw.rectangle(point_a, point_b, width=3)

simple_draw.pause()
