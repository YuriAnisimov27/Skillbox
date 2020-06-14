goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for i in goods:
    total_count, total_cost = 0, 0
    if goods[i] in store:
        for item in store[goods[i]]:
            total_count += item['quantity']
            total_cost += item['quantity'] * item['price']
        print(f'на складе: {i} - {total_count} шт, стоимость {total_cost} руб')
