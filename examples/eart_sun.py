from solarsystem import SolarSystem, Body
import numpy as np

import matplotlib.pyplot as plt
from tqdm import tqdm


sun = Body(mass=2e30, position=[0, 0, 0], velocity=[0, 0, 0])
earth = Body(mass=6e24, position=[152.1e9, 0, 0], velocity=[0, 29.29e3, 0])

system = SolarSystem([sun, earth])


n_years = 3
n_steps = 100000
delta_t = n_years * np.pi * 1e7 / n_steps

positions = np.empty((n_steps, 3))
energies = []
for i in tqdm(range(n_steps)):
    energies.append(system.total_energy)
    positions[i] = earth.position
    system.do_velocity_verlet_step(delta_t)

t = delta_t * np.arange(n_steps) / (3600 * 24)

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.set_aspect(1)
plot = ax1.scatter(
    positions[:, 0],
    positions[:, 1],
    c=t,
    cmap='viridis'
)
fig.colorbar(plot, ax=ax1)

ax1.plot(
    sun.position[0],
    sun.position[1],
    'yo'
)


ax2.plot(t, energies / energies[0])

plt.show()
