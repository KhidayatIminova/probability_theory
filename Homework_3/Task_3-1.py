# Задача 1. Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. 
# Посчитать (желательно без использования статистических методов наподобие std, var, mean) среднее арифметическое, 
# среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки

import numpy as np

arr=np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])

# Метод для вычисления среднего арифметического выборки
def mean_value(array):
    return sum(array)/len(array)

print(f'Среднее арифметическое для данной выборки М(Х) = {mean_value(arr):.2f}')

# Метод для вычисления среднего квадратичного отклонения выборки
def mean_square_deviation(array):
    square_dev=(array-mean_value(array))**2
    return (sum(square_dev)/len(square_dev))**(1/2)

print(f'Среднее квадратичное отклонение для данной выборки SD = {mean_square_deviation(arr):.5f}')

# Метод для вычисления смещенной оценки дисперсии 
def dispers1(array):
    square_dev=(array-mean_value(array))**2
    return sum(square_dev)/len(square_dev)

# Метод для вычисления несмещенной оценки дисперсии 
def dispers2(array):
    square_dev=(array-mean_value(array))**2
    return sum(square_dev)/(len(square_dev)-1) 

print(f'Смещенная оценка дисперсии для данной выборки D = {dispers1(arr):.5f}\n'
      f'Несмещенная оценка дисперсии для данной выборки D = {dispers2(arr):.5f\n}'
     )