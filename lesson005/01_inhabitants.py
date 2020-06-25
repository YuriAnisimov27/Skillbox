# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

# TODO здесь ваш код

from room1 import folks

citizens = ' ,'.join(folks)
print(f'В комнате room_1 живут: {citizens}')

from room2 import folks

citizens = ' ,'.join(folks)
print(f'В комнате room_1 живут: {citizens}')

