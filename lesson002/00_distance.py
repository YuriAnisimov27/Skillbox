#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pprint import pprint

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = dict()

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

moscow_london = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** 0.5
moscow_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** 0.5
london_paris = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** 0.5

# TODO здесь заполнение словаря

distances['Moscow'] = dict()
distances['Moscow']['London'] = int(moscow_london)
distances['Moscow']['Paris'] = int(moscow_paris)

distances['London'] = dict()
distances['London']['Moscow'] = int(moscow_london)
distances['London']['Paris'] = int(london_paris)

distances['Paris'] = dict()
distances['Paris']['London'] = int(london_paris)
distances['Paris']['Moscow'] = int(moscow_paris)

pprint(distances)
