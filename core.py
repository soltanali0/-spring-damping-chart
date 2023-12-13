import numpy as np
import matplotlib.pyplot as plt

def wave_function1(x):
    return np.sin(3 * x)

def damped_oscillation(x, amplitude, frequency, damping_factor):
    return amplitude * np.exp(-damping_factor * x) * np.sin(2 * np.pi * frequency * x)

x_values = np.linspace(0, 4 * np.pi, 1000)

plt.plot(x_values, wave_function1(x_values), label='Wave 1')

damping_factor = 200
plt.plot(x_values, damped_oscillation(x_values, 0.5, 2, damping_factor), label='Spring damping')

plt.title('Waves')
plt.xlabel('Time')
plt.ylabel('Place')
plt.legend()
plt.show()