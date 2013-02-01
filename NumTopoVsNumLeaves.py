#!/usr/bin/env python

# This script makes a figure that plots the staggering increase 
# in number of possible tree topologies with increasing number of taxa

import math
import numpy as np
import matplotlib
matplotlib.use('PS') #makes postscript the default file type
import matplotlib.pyplot as plt


leavesList = []  # number of leaves, indexed to two variables below
rootedTreesList = []  # number of rooted trees
unrootedTreesList = []  # number of unrooted trees
atoms = 10 ** 80  # estimated number of atoms in the universe
cells = 10 ** 13 # estimated number of cells in the human body

# generates the three lists; this example displays output from 4-100 taxa
for numLeaves in range(4,100):
    leavesList.append(numLeaves)
    rootedTreesList.append(math.factorial((2 * numLeaves) - 3) / ((2 ** (numLeaves - 2)) * math.factorial(numLeaves - 2)))
    unrootedTreesList.append(math.factorial((2 * numLeaves) - 5) / ((2 ** (numLeaves - 3)) * math.factorial(numLeaves - 3)))


# Plot on semilog y axis
plt.axes()
plt.semilogy(leavesList, rootedTreesList, 'b.')
plt.semilogy(leavesList, unrootedTreesList, 'r.')
plt.axhline(y = atoms, color = 'g', label = 'atoms / universe')  #adds horizontal line for # atoms in the universe
plt.axhline(y = cells, color = 'c', label = 'cells / human')   #adds horizontal line for # cells in human body
plt.title('Factorial increase in tree topologies with number of taxa')
plt.grid(True)
plt.ylabel('number of possible tree topologies')
plt.xlabel('number of taxa')
#plt.legend()
#plt.show()
plt.savefig('myfig')
