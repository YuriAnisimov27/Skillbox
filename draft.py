import simple_draw as sd
import random

sd.resolution = (1200, 600)

for i in range(100):
    point = sd.random_point()
    sd.random_color()
    radius = random.randint(2, 33)
    sd.circle(point, radius, width=3, color=sd.random_color())

sd.pause()
