import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_cylinder(origin):
    # Crear una figura 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Definir el radio y la altura del cilindro
    radius = 1.0
    height = 3.0

    # Crear la superficie del cilindro
    theta = np.linspace(0, 2*np.pi, 100)
    z = np.linspace(0, height, 100)
    r = np.linspace(radius, radius, 100)
    theta, z = np.meshgrid(theta, z)
    x = r * np.cos(theta) + origin[0]
    y = r * np.sin(theta) + origin[1]

    ax.plot_surface(x, y, z, color='b', alpha=0.7)

    # Configurar etiquetas y título
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Cilindro con origen en {}'.format(origin))

    # Mostrar el gráfico
    plt.show()

# Solicitar al usuario el punto de origen
origin_x = float(input("Ingrese la coordenada x del punto de origen: "))
origin_y = float(input("Ingrese la coordenada y del punto de origen: "))
origin_z = float(input("Ingrese la coordenada z del punto de origen: "))

origin = (origin_x, origin_y, origin_z)

# Llamar a la función para graficar el cilindro con el origen especificado
plot_cylinder(origin)
