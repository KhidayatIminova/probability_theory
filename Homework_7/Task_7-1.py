# Задача 1. Даны две независимые выборки. Не соблюдается условие нормальности
# x1 380,420, 290
# y1 140,360,200,900
# Сделайте вывод по результатам, полученным с помощью функции
# Решение:
# 	Поскольку нарушено условие применимости t-критерия произведем тест Манна-Уитни с помощью функции mannwhitheyu().

import numpy as np
import scipy.stats as stats

x1=np.array([380,420,290])
y1=np.array([140,360,200,900])
alpha=0.05
stats.mannwhitneyu(x1, y1)

# MannwhitneyuResult(statistic=8.0, pvalue=0.6285714285714286)
# Т.к. p-value>α, (α=0,05) статистически значимых различий в выборках нет. Нулевую гипотезу H_0 не отвергаем
