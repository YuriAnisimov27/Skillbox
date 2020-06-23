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

def draw_figure(start_point, end_point, angles_count, line_length):
    point = sd.get_point(start_point, end_point)
    angle = 360 // angles_count
    for i in range(angles_count):
        point_draw = sd.get_vector(start_point=point, angle=i * angle, length=line_length)
        point_draw.draw()
        point = point_draw.end_point



# point1 = sd.get_vector(start_point=point, angle=0, length=line_length)
# point1.draw()
# point2 = sd.get_vector(start_point=point1.end_point, angle=60, length=line_length)
# point2.draw()
# point3 = sd.get_vector(start_point=point2.end_point, angle=120, length=line_length)
# point3.draw()
# point4 = sd.get_vector(start_point=point3.end_point, angle=180, length=line_length)
# point4.draw()
# point5 = sd.get_vector(start_point=point4.end_point, angle=240, length=line_length)
# point5.draw()
# point6 = sd.get_vector(start_point=point5.end_point, angle=300, length=line_length)
# point6.draw()


# draw_3_angle(100, 100, 120, 100)
# draw_4_angle(300, 100, 90, 100)
# draw_5_angle(600, 100, 72, 100)
# draw_6_angle(900, 100, 60, 100)
draw_figure(200, 200, 4, 200)
draw_figure(400, 100, 3, 200)
draw_figure(600, 200, 5, 200)
draw_figure(900, 100, 6, 200)
sd.pause()
