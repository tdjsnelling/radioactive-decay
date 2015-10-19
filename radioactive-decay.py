# -*- coding: utf-8 -*-
# radioactive-decay.py
import sys, math, time, array
import matplotlib.pyplot as mpl

# λ = ln(2) / t (half)
# N = N0 * e ^ (-λt)

start_time = time.time()

# half life and starting number of atoms
half_life = 19.29 # carbon-10
atoms = 100

# all initial atoms remain, until decay starts
atoms_remaining = atoms

# λ = ln(2) / t (half)
decay_const = math.log(2) / half_life

# set up arrays to hold valuest that will be plotted
atoms_plot = array.array('I', [])
time_plot = array.array('f', [])

index = 0

# while we still have atoms left
while atoms_remaining > 0:
	# keep track of time elapsed
	elapsed_time = time.time() - start_time

	# N = N0 * e ^ (-λt)
	atoms_remaining = int(atoms * math.exp(-decay_const * elapsed_time))

	# index once every 10**3 calculations to save memory
	if index % 10**3 == 0:
		atoms_plot.append(atoms_remaining)
		time_plot.append(elapsed_time)

	index += 1

# print time taken to simulate (real time)
print elapsed_time, 's'

# plot graph of time against atoms remaining
mpl.plot(time_plot, atoms_plot)
mpl.title('Radioactive Decay - Half life %fs, %d atoms' % (half_life, atoms))
mpl.xlabel('Time (s)')
mpl.ylabel('Atoms')
mpl.show()
