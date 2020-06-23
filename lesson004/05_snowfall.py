# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код
while True:
    sd.clear_screen()
    pass
    pass
    pass
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


import simple_draw as sd

sd.resolution = (1300, 600)

N = 20

for x in range(N):
    y = 650
    snow_len1 = sd.random_number(10, 40)
    snow_len2 = sd.random_number(10, 40)
    snow_len3 = sd.random_number(10, 40)
    snow_len4 = sd.random_number(10, 40)
    snow_len5 = sd.random_number(10, 40)
    snow_len6 = sd.random_number(10, 40)
    snow_len7 = sd.random_number(10, 40)
    snow_len8 = sd.random_number(10, 40)
    snow_len9 = sd.random_number(10, 40)
    snow_len10 = sd.random_number(10, 40)
    color1 = sd.random_color()
    color2 = sd.random_color()
    color3 = sd.random_color()
    color4 = sd.random_color()
    color5 = sd.random_color()
    color6 = sd.random_color()
    color7 = sd.random_color()
    color8 = sd.random_color()
    color9 = sd.random_color()
    color10 = sd.random_color()
    x1 = sd.random_number(1, 1300)
    x2 = sd.random_number(1, 1300)
    x3 = sd.random_number(1, 1300)
    x4 = sd.random_number(1, 1300)
    x5 = sd.random_number(1, 1300)
    x6 = sd.random_number(1, 1300)
    x7 = sd.random_number(1, 1300)
    x8 = sd.random_number(1, 1300)
    x9 = sd.random_number(1, 1300)
    x10 = sd.random_number(1, 1300)
    y1 = sd.random_number(650, 1300)
    y2 = sd.random_number(650, 1300)
    y3 = sd.random_number(650, 1300)
    y4 = sd.random_number(650, 1300)
    y5 = sd.random_number(650, 1300)
    y6 = sd.random_number(650, 1300)
    y7 = sd.random_number(650, 1300)
    y8 = sd.random_number(650, 1300)
    y9 = sd.random_number(650, 1300)
    y10 = sd.random_number(650, 1300)
    speed1 = sd.random_number(3, 15)
    speed2 = sd.random_number(3, 15)
    speed3 = sd.random_number(3, 15)
    speed4 = sd.random_number(3, 15)
    speed5 = sd.random_number(3, 15)
    speed6 = sd.random_number(3, 15)
    speed7 = sd.random_number(3, 15)
    speed8 = sd.random_number(3, 15)
    speed9 = sd.random_number(3, 15)
    speed10 = sd.random_number(3, 15)
    while True:
        sd.sleep(0.1)
        sd.clear_screen()
        root_point1 = sd.get_point(x1, y1)
        root_point2 = sd.get_point(x2, y2)
        root_point3 = sd.get_point(x3, y3)
        root_point4 = sd.get_point(x4, y4)
        root_point5 = sd.get_point(x5, y5)
        root_point6 = sd.get_point(x6, y6)
        root_point7 = sd.get_point(x7, y7)
        root_point8 = sd.get_point(x8, y8)
        root_point9 = sd.get_point(x9, y9)
        root_point10 = sd.get_point(x10, y10)
        if sd.user_want_exit():
            break
        sd.snowflake(root_point1, length=snow_len1, color=color1)
        sd.snowflake(root_point2, length=snow_len2, color=color2)
        sd.snowflake(root_point3, length=snow_len3, color=color3)
        sd.snowflake(root_point4, length=snow_len4, color=color4)
        sd.snowflake(root_point5, length=snow_len5, color=color5)
        sd.snowflake(root_point6, length=snow_len6, color=color6)
        sd.snowflake(root_point7, length=snow_len7, color=color7)
        sd.snowflake(root_point8, length=snow_len8, color=color8)
        sd.snowflake(root_point9, length=snow_len9, color=color9)
        sd.snowflake(root_point10, length=snow_len10, color=color10)
        y1 -= speed1
        y2 -= speed2
        y3 -= speed3
        y4 -= speed4
        y5 -= speed5
        y6 -= speed6
        y7 -= speed7
        y8 -= speed8
        y9 -= speed9
        y10 -= speed10
        x1 -= sd.random_number(-10, 10)
        x2 -= sd.random_number(-10, 10)
        x3 -= sd.random_number(-10, 10)
        x4 -= sd.random_number(-10, 10)
        x5 -= sd.random_number(-10, 10)
        x6 -= sd.random_number(-10, 10)
        x7 -= sd.random_number(-10, 10)
        x8 -= sd.random_number(-10, 10)
        x9 -= sd.random_number(-10, 10)
        x10 -= sd.random_number(-10, 10)
        if y1 < - 100:
            y1 = 700
            x1 = sd.random_number(1, 1300)
            color1 = sd.random_color()
            snow_len1 = sd.random_number(30, 100)
        if y2 < - 100:
            y2 = 700
            x2 = sd.random_number(1, 1300)
            color2 = sd.random_color()
            snow_len2 = sd.random_number(30, 100)
        if y3 < - 100:
            y3 = 700
            x3 = sd.random_number(1, 1300)
            color3 = sd.random_color()
            snow_len3 = sd.random_number(30, 100)
        if y4 < - 100:
            y4 = 700
            x4 = sd.random_number(1, 1300)
            color4 = sd.random_color()
            snow_len4 = sd.random_number(30, 100)
        if y5 < - 100:
            y5 = 700
            x5 = sd.random_number(1, 1300)
            color5 = sd.random_color()
            snow_len5 = sd.random_number(30, 100)
        if y6 < - 100:
            y6 = 700
            x6 = sd.random_number(1, 1300)
            color6 = sd.random_color()
            snow_len6 = sd.random_number(30, 100)
        if y7 < - 100:
            y7 = 700
            x7 = sd.random_number(1, 1300)
            color7 = sd.random_color()
            snow_len7 = sd.random_number(30, 100)
        if y8 < - 100:
            y8 = 700
            x8 = sd.random_number(1, 1300)
            color8 = sd.random_color()
            snow_len8 = sd.random_number(30, 100)
        if y9 < - 100:
            y9 = 700
            x9 = sd.random_number(1, 1300)
            color9 = sd.random_color()
            snow_len9 = sd.random_number(30, 100)
        if y10 < - 100:
            y10 = 700
            x10 = sd.random_number(1, 1300)
            color10 = sd.random_color()
            snow_len10 = sd.random_number(30, 100)

sd.pause()
