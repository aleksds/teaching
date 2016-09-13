# Aleks Diamond-Stanic
# 13-Sep-2016

import numpy as np

# consider mean and standard deviation of three position measurements
x = np.array([0.751, 0.745, 0.753])
print('x mean: ', np.mean(x))
print('x mean: {0:5.3f}'.format(np.mean(x)))
print('x std: ', np.std(x))
print('x std: {0:5.3f}'.format(np.std(x)))

# consider mean and standard deviation of three time measurements
t = np.array([0.653, 0.672, 0.684])
print('t mean: ', np.mean(t))
print('t mean: {0:4.2f}'.format(np.mean(t)))
print('t std: ', np.std(t))
print('t std: {0:4.2f}'.format(np.std(t)))


