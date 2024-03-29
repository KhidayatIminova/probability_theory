# Задача 3. На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. 
# Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. 
# Найти вероятность того, что выстрел произведен: a). первым спортсменом б). вторым спортсменом в). третьим спортсменом.

import os         
os.system('cls')

# Событие A - попадание в мишень
# Событие B1 - выстрелил первый спортсмен
# Событие B2 - выстрелил второй спортсмен
# Событие B3 - выстрелил третий спортсмен

# Обозначим вероятности попадания спортсменов:

p1=0.9 
p2=0.8
p3=0.6

# PB1=PB2=PB3=PB=1/3 - вероятность выстрела каждого спортсмена
PB=1/3

# Полная вероятность попадания в мишень
PA=PB*p1+PB*p2+PB*p3

print(f'Полная вероятность попадания в мишень Р(А) = {PA:.5f}\n')

# Воспользуемся формулой Байеса для определения вероятностей выстрела (B1..B3) каждым из спортсменов 
# при условии, что попадание в мишень (A) уже произошло
PB1A=PB*p1/PA
PB2A=PB*p2/PA
PB3A=PB*p3/PA

print(f'Вероятность того, что выстрел произвёл первый спортсмен: {PB1A:.5f}\n'
      f'Вероятность того, что выстрел произвёл второй спортсмен: {PB2A:.5f}\n'
      f'Вероятность того, что выстрел произвёл третий спортсмен: {PB3A:.5f}\n')

