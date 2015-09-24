# -*- coding: utf-8 -*-
# radioactive-decay.py
import sys, math, time, array
import matplotlib.pyplot as mpl

# λ = ln(2) / t (half)
# N = N0 * e ^ (-λt)

start_time = time.time()

half_life = 19.29 # carbon-10
atoms = 100

atoms_remaining = atoms

decay_const = math.log(2) / half_life

atoms_plot = array.array('I', [])
time_plot = array.array('f', [])

index = 0

while atoms_remaining > 0:
	elapsed_time = time.time() - start_time
	atoms_remaining = int(atoms * math.exp(-decay_const * elapsed_time))

	# index once every 10**3 to save memory
	if index % 10**3 == 0:
		atoms_plot.append(atoms_remaining)
		time_plot.append(elapsed_time)

	index += 1

print elapsed_time, 's'

mpl.plot(time_plot, atoms_plot)
mpl.title('Radioactive Decay - Half life %fs, %d atoms' % (half_life, atoms))
mpl.xlabel('Time (s)')
mpl.ylabel('Atoms')
mpl.show()
