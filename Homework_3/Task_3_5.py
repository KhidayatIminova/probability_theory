# Задача 5. Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25.
# Какова вероятность того, что в первый месяц выйдут из строя: а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?

import os         
os.system('cls')

# Обозначим вероятности выхода из строя деталей:

p1=0.1
p2=0.2
p3=0.25

# а) Какова вероятность того, что в первый месяц выйдут из строя все детали? (событие А3)

PA3=p1*p2*p3 # одновременное наступление всех трех событий - произведение их вероятностей
print(f'Вероятность того, что из строя выйдут все детали Р(A3) = {PA3:.5f}')

# б) Какова вероятность того, что в первый месяц выйдут из строя только две детали? (событие А2)

# Для события А2 возможны следующие комбинации:
# 1) Выйдет из строя первая и вторая детали (сочетание 110)
# 2) Выйдут из строя первая и третья детали (сочетание 101)
# 3) Выйдут из строя вторая и третья детали (сочетание 001)
# 
# PA2 = (p1 И p2 И (НЕ p3)) ИЛИ (p1 И (НЕ p2) И p3) ИЛИ ((НЕ p1) И p2 И p3)

PA2=p1*p2*(1-p3)+p1*(1-p2)*p3+(1-p1)*p2*p3
print(f'Вероятность того, что из строя выйдут только 2 детали Р(A2) = {PA2:.5f}')

# в) Какова вероятность того, что в первый месяц выйдет из строя хотя бы одна деталь? (событие А>=1)
# Cобытие "выйдет из строя хотя бы одна деталь" включает в себя все возможные комбинации вышедших из строя деталей,
# и по сути является общим событием "неисправность" (AF) - "failure", противоположным событию "исправно" (A0), когда все 3 детали исправны.

PA0=(1-p1)*(1-p2)*(1-p3)
PAF=1-PA0
print(f'Вероятность того, что выйдет из строя хотя бы одна деталь Р(A>=1) = P(AF) = {PAF:.5f}')

# г) Какова вероятность того, что в первый месяц выйдет из строя от одной до двух деталей? (событие А1,2)
# Для события A1,2 возможны следующие комбинации:
# 1) Выйдет из строя 1 деталь (событие A1)
# 2) Выйдет из строя 2 детали (событие A2)
# 
# Вероятность события A1,2 является суммой вероятностей событий А1 и А2 
# В то же время события A1 и A2 и A3 относятся к общему событию "неисправность" AF, 
# и их суммарная вероятность равна вероятности отказа хотя бы одной детали:
# 
# PA1 + PA2 + PA3 = PAF
# PA1,2 = PAF - PA3

print(f'Вероятность того, что выйдет из строя выйдут от 1 до 2 деталей Р(A1,2) = {PAF-PA3:.5f}')