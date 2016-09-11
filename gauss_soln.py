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

# define the gaussian function
g = gaussian(x, 3.0, 0., 0.3)

# plot the profiles
ax = plt.subplot(1,2,1)
ax.plot(x, f, color='blue')
ax.plot(x, g, color='red')

# integrate f and g over the full range of x
f_int = np.sum(f)
print("function area", f_int)
g_int = np.sum(g)
print("gaussian area", g_int)

# consider the fraction of the total area over a given width
nel = max / dx + 1
width = np.arange(nel) * dx
f_frac = np.zeros(nel)
g_frac = np.zeros(nel)

# loop over widths from 0 to 6
for i in np.arange(nel):
    rel = np.where(np.abs(x) < width[i])
    f_frac[i] = np.sum(f[rel]) / f_int
    g_frac[i] = np.sum(g[rel]) / g_int

# what width encloses 68% of the total area?
f_68 = f_frac > 0.68
print("function 68% width",width[f_68][0], f_frac[f_68][0])
g_68 = g_frac > 0.68
print("gaussian 68% width",width[g_68][0], g_frac[g_68][0])

# what width encloses 95% of the total area?
f_95 = f_frac > 0.95
print("function 95% width",width[f_95][0], f_frac[f_95][0])
g_95 = g_frac > 0.95
print("gaussian 95% width",width[g_95][0], g_frac[g_95][0])

# plot the percentage vs width
ax = plt.subplot(1,2,2)
ax.plot(width, f_frac, color='blue')
ax.plot(width, g_frac, color='red')

plt.show()


