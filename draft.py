educational_grant, expenses = 10000, 12000
need_money = 0
for i in range(10):
    need_money += expenses - educational_grant
    expenses *= 1.03
print(f'Студенту надо попросить {round(need_money, 2)} рублей')