# -*- coding: utf-8 -*-
# radioactive-decay.py
import sys, math, time
import matplotlib.pyplot as mpl

# λ = ln(2) / t (half)
# N = N0 * e ^ (-λt)

start_time = time.time()
mol = 6.022*(10**24)

half_life = 1.00
atoms = 10**4

atoms_remaining = atoms

decay_const = math.log(2) / half_life

atoms_plot = []
time_plot = []

while atoms_remaining > 0:
	elapsed_time = time.time() - start_time
	atoms_remaining = int(atoms * math.exp(-decay_const*elapsed_time))
	# print "\r", elapsed_time, int(atoms_remaining)

	atoms_plot.append(atoms_remaining)
	time_plot.append(elapsed_time)

mpl.plot(time_plot, atoms_plot)
mpl.title('Radioactive Decay - Half life %fs, %d atoms' % (half_life, atoms))
mpl.xlabel('Time (s)')
mpl.ylabel('Atoms')
mpl.show()
	
