import simple_draw as sd

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
