# Задача 4. Даны 3 группы учеников плавания.
# В 1 группе время на дистанцию 50 м составляют: 56, 60, 62, 55, 71, 67, 59, 58, 64, 67
# Вторая группа : 57, 58, 69, 48, 72, 70, 68, 71, 50, 53
# Третья группа: 57, 67, 49, 48, 47, 55, 66, 51, 54
# Решение:
# H_0 : Время на дистанцию 50 м по группам не отличается
# Поскольку нарушены условия для параметрических критериев (нормальность и равенство дисперсий) и группы независимы применим критерий Крускала- Уоллиса 

import numpy as np
import scipy.stats as stats

x1=np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
x2=np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
x3=np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])
alpha=0.05
stats.kruskal(x1,x2,x3)

# KruskalResult(statistic=5.465564058257224, pvalue=0.0650380998590494)

# Т.к. p-value>α, (α=0,05) статистически значимых различий в выборках нет. Нулевую гипотезу H_0 не отвергаем. Время на дистанцию 50 м по группам не отличается.
