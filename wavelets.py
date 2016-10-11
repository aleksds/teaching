# Aleks Diamond-Stanic
# 20160929
#
# The main goal of this code is to produce a visualization of the
# reflection of a wave as the result of scattering (along the lines of
# Figure 4.15 from the Fifth Edition of Optics by Eugene Hecht)
#

import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

filename = 'wavelets.pdf'

xmin = -5.
xmax = 5.

x = np.arange(xmax - xmin + 1.) + xmin
y = np.zeros(len(x))

angle = [30., 40., 50., 60.]

with PdfPages(filename) as pdf:

    fig = plt.figure()

    for j in range(0, len(angle)):
    
        ax = fig.add_subplot(2,2,j+1)
        ax.set_xlim([xmin-1,xmax+1])
        ax.set_ylim([xmin-1,xmax+1])
        ax.plot(x, y, 'ro')
        plt.gca().set_aspect('equal', adjustable='box')
        title = str(r'$\theta_{i}=$')+str('{0:2.0f}'.format(angle[j]))
        plt.title(title)
        
        for i in range(0, len(x)):
            circle=plt.Circle((x[i],y[i]), radius=(len(x)-i)*np.cos(angle[j]*np.pi/180.), color='g', fill=False)
            ax.add_patch(circle)
    
    pdf.savefig()
    plt.close()

os.system("open %s &" % filename)
