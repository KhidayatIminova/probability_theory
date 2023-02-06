# Задача 3. Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175 
# Используя эти данные построить 95% доверительный интервал для разности среднего
# роста родителей и детей

import os         
os.system('cls')

import numpy as np
import scipy.stats as stats

daughters = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
mothers = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])

n_mothers = len(mothers)     # объем выборки матерей
n_daughters = len(daughters)     # объем выборки дочерей

x_daughters = np.mean(daughters) # среднее арифметическое по выборке дочерей 
x_mothers = np.mean(mothers) # среднее арифметическое по выборке матерей 

delta_x = x_mothers - x_daughters    # разность средних

D_mothers = np.var(mothers, ddof=1)		# несмещенная дисперсия по выборке матерей
D_daughters = np.var(daughters, ddof=1)		# несмещенная дисперсия по выборке дочерей

D = (D_mothers + D_daughters)/2     # объединенная оценка дисперсии

SE = np.sqrt(D/n_mothers + D/n_daughters)   # стандартная ошибка разности средних

alpha = 1-0.95
n = 2 * (n_mothers - 1) # степени свободы n = 18
t = stats.t.ppf(1-alpha/2, n-1)	# критерий Стьюдента t=2.10092204024096

L = delta_x - t*SE # нижняя граница интервала

U = delta_x + t*SE # верхняя граница интервала

print(f'Доверительный интервал (95%) для разности среднего роста родителей и детей: [{L:.5f};{U:.5f}]')

# Доверительный интервал (95%) для разности среднего роста родителей и детей: [-6.30300;10.10300]