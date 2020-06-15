import simple_draw

simple_draw.resolution = (1300, 700)


def smily_face(x, y, colore):
    point_center = simple_draw.get_point(x, y)
    left_eye = simple_draw.get_point(x - 40, y + 27)
    right_eye = simple_draw.get_point(x + 40, y + 27)

    simple_draw.circle(point_center, 88, color=colore, width=4)
    simple_draw.circle(left_eye, 23, color=colore, width=4)
    simple_draw.circle(right_eye, 23, color=colore, width=4)

    for i in range(10):
        new_center = simple_draw.get_point(x, y - i * 3)
        simple_draw.circle(new_center, 20 - i, width=0)


for _ in range(10):
    x = simple_draw.random_number(0, 1300)
    y = simple_draw.random_number(0, 700)
    smily_face(x, y, simple_draw.random_color())

simple_draw.pause()
