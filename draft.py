hole_x, hole_y = 8, 9
brick_x, brick_y, brick_z = 3, 6, 11

middle = brick_x + brick_y + brick_z - max(brick_x, brick_y, brick_z) - min(brick_x, brick_y, brick_z)
if max(hole_x, hole_y) >= middle and \
        min(hole_x, hole_y) >= min(brick_x, brick_y, brick_z):
    print('ДА')
else:
    print('НЕТ')
