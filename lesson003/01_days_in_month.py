# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
# user_input = input("Введите, пожалуйста, номер месяца: ")
# month = int(user_input)
# print('Вы ввели', month)

# TODO здесь ваш код
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)

month_with_31_days = [1, 3, 5, 7, 8, 10, 12]
month_with_30_days = [4, 6, 9, 11]
month_with_28_days = [2]
if month in month_with_31_days:
    days = 31
elif month in month_with_30_days:
    days = 30
elif month in month_with_28_days:
    days = 28
else:
    print('номер месяца некорректен')
    days = 'непонятно сколько'

print(f'вы ввели {month}, в этом месяце {days} дней')
