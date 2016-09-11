# Aleks Diamond-Stanic
# 11-Sep-2016
#

import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, peak, center, sigma):
    return peak * np.exp(((x-center)/sigma)**2*(-0.5))

# make an array that goes from -6 to +6 with elements every 0.01
min = -6
max = 6
dx = 0.01
nel = (max - min) / dx + 1
x = np.arange(nel) * dx + min

# define the profile from the book
f = 3 / (10 * x**2 + 1)

plt.plot(x, f)

# define the gaussian function
gau = gaussian(x, 3.0, 0., 0.3)
plt.plot(x,gau)

plt.show()


