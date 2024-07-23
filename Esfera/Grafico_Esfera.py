import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Creamos una figura
figura = plt.figure()
# Creamos el eje
eje = figura.add_subplot(111, projection='3d')

# Variable Radio
radio = 9
# Variable Theta
theta = np.arange(0, 2 * np.pi, 0.01)
# Variable Phi
phi = np.arange(0, np.pi, 0.01)

# Creacion ???
theta, phi = np.meshgrid(theta, phi)
# El radio
ro = np.sqrt(radio)
# Ejes
eje_x = ro * np.sin(phi) * np.cos(theta)
eje_y = ro * np.sin(phi) * np.sin(theta)
eje_z = ro * np.cos(phi)

eje.plot_surface(eje_x, eje_y, eje_z, color = 'b')

# Mostramos las letras de las coordenadas
eje.set_xlabel('EJE X')
eje.set_ylabel('EJE Y')
eje.set_zlabel('EJE Z')

# Mostramos el resultado en una ventana
plt.show()