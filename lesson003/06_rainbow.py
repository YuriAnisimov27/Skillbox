# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код

for i in range(7):
    point = sd.get_point(0, 0)
    radius = (100 + 100 * i)
    sd.circle(point, radius, width=100, color=rainbow_colors[i])


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

for i in range(7):
    point = sd.get_point(400, -200)
    radius = (500 + 30 * i)
    sd.circle(point, radius, width=30, color=rainbow_colors[i])

sd.pause()
