# Задача 3. Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было.
# 1е измерение до приема препарата: 150, 160, 165, 145, 155
# 2е измерение через 10 минут: 140, 155, 150, 130, 135

# Решение:
# 	H_0 : препарат влияет на давление
# Поскольку есть 2 зависимые выборки и объем выборок <50 используем тест Уилкоксона

import numpy as np
import scipy.stats as stats

x1=np.array([150, 160, 165, 145, 155])
x2=np.array([140, 155, 150, 130, 135])

alpha=0.05
stats.wilcoxon(x1, x2)

# WilcoxonResult(statistic=0.0, pvalue=0.0625)
# Т.к. p-value>α, (α=0,05) статистически значимых различий в выборках нет. Нулевую гипотезу H_0 не отвергаем. Препарат не влияет на давление.
