# Aleks Diamond-Stanic
# 13-Sep-2016

import numpy as np

# consider mean and standard deviation of three position measurements
x = np.array([0.751, 0.745, 0.753])
print('x mean: ', np.mean(x))
# print the mean with three decimal places
print('x mean: {0:5.3f}'.format(np.mean(x)))
print('x std: ', np.std(x))
# print the standard deviation with three decimal places
print('x std: {0:5.3f}'.format(np.std(x)))
print('x unc: ', ((np.max(x)-np.min(x))/2))
# print the (max-min)/2 estimate of uncertainty to three decimal places
print('x unc: {0:5.3f}'.format((np.max(x)-np.min(x))/2))

# consider mean and standard deviation of three time measurements
t = np.array([0.653, 0.672, 0.684])
print('t mean: ', np.mean(t))
# print the mean with two decimal places
print('t mean: {0:4.2f}'.format(np.mean(t)))
print('t std: ', np.std(t))
# print the standard deviation with two decimal places
print('t std: {0:4.2f}'.format(np.std(t)))
print('t unc: ', (np.max(t)-np.min(t))/2)
# print the (max-min)/2 estimate of uncertainty to three decimal places
print('t unc: {0:4.2f}'.format((np.max(t)-np.min(t))/2))


