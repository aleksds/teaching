# Aleks Diamond-Stanic
# 20160929

import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

filename = 'wavelets.pdf'

xmin = -5.
xmax = 5.

x = np.arange(xmax - xmin + 1.) + xmin
y = np.zeros(len(x))

with PdfPages(filename) as pdf:

    fig = plt.figure()
    
    ax = fig.add_subplot(1,1,1)
    ax.set_xlim([xmin-1,xmax+1])
    ax.set_ylim([xmin-1,xmax+1])
    ax.plot(x, y, 'ro')

    pdf.savefig()
    plt.close()

os.system("open %s &" % filename)
