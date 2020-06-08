#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []

my_family.append("father")
my_family.append("mother")
my_family.append("brother")
my_family.append("sister")

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [],
]

my_family_height = my_family_height * len(my_family)
my_family_height[0] = [my_family[0], 180]
my_family_height[1] = [my_family[1], 160]
my_family_height[2] = [my_family[2], 80]
my_family_height[3] = [my_family[3], 130]
print(my_family_height)

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца -', my_family_height[0][1], 'см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
print('Общий рост моей семьи -', my_family_height[0][1] + my_family_height[1][1] +
      my_family_height[2][1] + my_family_height[3][1], 'см')
