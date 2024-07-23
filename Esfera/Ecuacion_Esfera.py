from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def esfera(coordenada_x_ent, coordenada_y_ent, coordenada_z_ent, radio_ent, error):
    # Tomar los valores
    coordenada_x = coordenada_x_ent.get()
    coordenada_y = coordenada_y_ent.get()
    coordenada_z = coordenada_z_ent.get()
    radio = radio_ent.get()

    # Convertir los datos a enteros
    coordenada_x = float(coordenada_x)
    coordenada_y = float(coordenada_y)
    coordenada_z = float(coordenada_z)
    radio = float(radio)
    
    if radio <= 0:
        error.config(text="El radio no puede ser igual o menor a cero", fg="red")
    else:
        # Creamos una figura 3D
        figura = plt.figure()
        eje = figura.add_subplot(111, projection='3d')

        # Crear la superficie del cilindro
        theta = np.arange(0, 2 * np.pi, 0.01)
        phi = np.arange(0, np.pi, 0.01)
        ro = np.sqrt(radio)

        # Graficar la malla
        theta, phi = np.meshgrid(theta, phi)

        # Ejes
        eje_x = ro * np.sin(phi) * np.cos(theta) + coordenada_x
        eje_y = ro * np.sin(phi) * np.sin(theta) + coordenada_y
        eje_z = ro * np.cos(phi) + coordenada_z

        eje.plot_surface(eje_x, eje_y, eje_z, color = 'b', alpha=0.7)

        # Mostramos las letras de las coordenadas
        eje.set_xlabel('EJE X')
        eje.set_ylabel('EJE Y')
        eje.set_zlabel('EJE Z')

        # -------------------- Parte de la ecuacion -----------------------

        radio_cuadrado = 0  # radio al cuadrado
        x_por_dos = 0   # coordenada_x multiplicada por dos
        x_cuadrado = 0  # coordenada_x al cuadrado
        y_por_dos = 0   # coordenada_y multiplicada por dos
        y_cuadrado = 0  # coordenada_y al cudarado
        z_por_dos = 0   # coordenada_y multiplicada por dos
        z_cuadrado = 0  # coordenada_z al cudarado
        suma_cuadrados = 0 # Suma del resultado de la op_3 y la op_5

        # Operacion para el radio
        radio_cuadrado = radio * radio
        # Operaciones para la primera coordenada ingresada (en este caso x)
        x_por_dos = coordenada_x * 2
        x_cuadrado = coordenada_x * coordenada_x
        # Operaciones para la segunda coordenada ingresada (en este caso y)
        y_por_dos = coordenada_y * 2
        y_cuadrado = coordenada_y * coordenada_y
        # Operaciones para la segunda coordenada ingresada (en este caso z)
        z_por_dos = coordenada_z * 2
        z_cuadrado = coordenada_z * coordenada_z
        # Suma de los enteros
        suma_cuadrados = x_cuadrado + y_cuadrado + z_cuadrado

        # ---------------------------------------------- Mostrar la ecuacion de la esfera --------------------------------------------------

        #(+ + +)
        if x_por_dos > 0 and y_por_dos > 0 and z_por_dos > 0:
            eje.set_title(f'(Ecuación de la esfera)\n {radio_cuadrado} = x^2 -{x_por_dos}x + y^2 -{y_por_dos}y + z^2 -{z_por_dos}z + {suma_cuadrados}')

        #(- - -)
        elif x_por_dos < 0 and y_por_dos < 0 and z_por_dos < 0:
            x_por_dos = abs(x_por_dos)
            y_por_dos = abs(y_por_dos)
            z_por_dos = abs(z_por_dos)
            eje.set_title(f'(Ecuación de la esfera)\n {radio_cuadrado} = x^2 +{x_por_dos}x + y^2 +{y_por_dos}y + z^2 +{z_por_dos}z + {suma_cuadrados}')

        #(0 0 0)
        elif x_por_dos == 0 and y_por_dos == 0 and z_por_dos == 0:
            eje.set_title(f'(Ecuación de la esfera)\n {radio_cuadrado} = x^2 + y^2 + z^2')

        #(0 + +)
        elif x_por_dos == 0 and y_por_dos > 0 and z_por_dos > 0:
            eje.set_title(f'(Ecuación de la esfera)\n {radio_cuadrado} = x^2 + y^2 -{y_por_dos}y + z^2 -{z_por_dos}z + {suma_cuadrados}')

        #(+ 0 +)
        elif x_por_dos > 0 and y_por_dos == 0 and z_por_dos > 0:
            eje.set_title(f'(Ecuacion de la esfera)\n {radio_cuadrado} = x^2 -{x_por_dos}x + y^2 + z^2 -{z_por_dos}z + {suma_cuadrados}')

        #(+ + 0)
        elif x_por_dos > 0 and y_por_dos > 0 and z_por_dos == 0:
            eje.set_title(f'(Ecuación de la esfera)\n {radio_cuadrado} = x^2 -{x_por_dos}x + y^2 -{y_por_dos}y + z^2  + {suma_cuadrados}')

        #(0 - -)
        elif x_por_dos == 0 and y_por_dos < 0 and z_por_dos < 0:
            y_por_dos = abs(y_por_dos)
            z_por_dos = abs(z_por_dos)
            eje.set_title(f'(Ecuación de la esfera)\n {radio_cuadrado} = x^2 + y^2 +{y_por_dos}y + z^2 +{z_por_dos}z + {suma_cuadrados}')
        #(- 0 -)
        elif x_por_dos < 0 and y_por_dos == 0 and z_por_dos < 0:
            x_por_dos = abs(x_por_dos)
            z_por_dos = abs(z_por_dos)
            eje.set_title(f'(Ecuación de la esfera)\n {radio_cuadrado} = x^2 +{x_por_dos}x + y^2 + z^2 +{z_por_dos}z + {suma_cuadrados}')

        #(- - 0)
        elif x_por_dos < 0 and y_por_dos < 0 and z_por_dos == 0:
            x_por_dos = abs(x_por_dos)
            y_por_dos = abs(y_por_dos)
            eje.set_title(f'(Ecuación de la esfera)\n {radio_cuadrado} = x^2 +{x_por_dos}x + y^2 +{y_por_dos}y + z^2 + {suma_cuadrados}')

        #(0 + -)
        elif x_por_dos == 0 and y_por_dos > 0 and z_por_dos < 0:
            z_por_dos = abs(z_por_dos)
            eje.set_title(f'(Ecuación de la esfera)\n {radio_cuadrado} = x^2 + y^2 -{y_por_dos}y + z^2 +{z_por_dos}z + {suma_cuadrados}')

        #(0 - +)
        elif x_por_dos == 0 and y_por_dos < 0 and z_por_dos > 0:
            y_por_dos = abs(y_por_dos)
            eje.set_title(f'(Ecuación de la esfera)\n {radio_cuadrado} = x^2 + y^2 +{y_por_dos}y + z^2 -{z_por_dos}z + {suma_cuadrados}')

        #(+ 0 -)
        elif x_por_dos > 0 and y_por_dos == 0 and z_por_dos < 0:
            z_por_dos = abs(z_por_dos)
            eje.set_title(f'(Ecuación de la esfera)\n {radio_cuadrado} = x^2 -{x_por_dos}x + y^2 + z^2 +{z_por_dos}z + {suma_cuadrados}')

        #(- 0 +)
        elif x_por_dos < 0 and y_por_dos == 0 and z_por_dos > 0:
            x_por_dos = abs(x_por_dos)
            eje.set_title(f'(Ecuación de la esfera)\n {radio_cuadrado} = x^2 +{x_por_dos}x + y^2 + z^2 -{z_por_dos}z + {suma_cuadrados}')
    
        #(+ - 0)
        elif x_por_dos > 0 and y_por_dos < 0 and z_por_dos == 0:
            y_por_dos = abs(y_por_dos)
            eje.set_title(f'(Ecuación de la esfera)\n {radio_cuadrado} = x^2 -{x_por_dos}x + y^2 +{y_por_dos}y + z^2 + {suma_cuadrados}')

        #(- + 0)
        elif x_por_dos < 0 and y_por_dos > 0 and z_por_dos == 0:
            x_por_dos = abs(x_por_dos)
            eje.set_title(f'(Ecuación de la esfera)\n {radio_cuadrado} = x^2 +{x_por_dos}x + y^2 -{y_por_dos}y + z^2 + {suma_cuadrados}')

        #(- + +)
        elif x_por_dos < 0 and y_por_dos > 0 and z_por_dos > 0:
            x_por_dos = abs(x_por_dos)
            eje.set_title(f'(Ecuación de la esfera)\n {radio_cuadrado} = x^2 +{x_por_dos}x + y^2 -{y_por_dos}y + z^2 -{z_por_dos}z + {suma_cuadrados}')
        
        #(+ - +)
        elif x_por_dos > 0 and y_por_dos < 0 and z_por_dos > 0:
            y_por_dos = abs(y_por_dos)
            eje.set_title(f'(Ecuación de la esfera)\n {radio_cuadrado} = x^2 -{x_por_dos}x + y^2 +{y_por_dos}y + z^2 -{z_por_dos}z + {suma_cuadrados}')

        #(+ + -)
        elif x_por_dos > 0 and y_por_dos > 0 and z_por_dos < 0:
            z_por_dos = abs(z_por_dos)
            eje.set_title(f'(Ecuación de la esfera)\n {radio_cuadrado} = x^2 -{x_por_dos}x + y^2 -{y_por_dos}y + z^2 +{z_por_dos}z + {suma_cuadrados}')

        #(+ - -)
        elif x_por_dos > 0 and y_por_dos < 0 and z_por_dos < 0:
            y_por_dos = abs(y_por_dos)
            z_por_dos = abs(z_por_dos)
            eje.set_title(f'(Ecuación de la esfera)\n {radio_cuadrado} = x^2 -{x_por_dos}x + y^2 +{y_por_dos}y + z^2 +{z_por_dos}z + {suma_cuadrados}')

        #(- + -)
        elif x_por_dos < 0 and y_por_dos > 0 and z_por_dos < 0:
            x_por_dos = abs(x_por_dos)
            z_por_dos = abs(z_por_dos)
            eje.set_title(f'(Ecuación de la esfera)\n {radio_cuadrado} = x^2 +{x_por_dos}x + y^2 -{y_por_dos}y + z^2 +{z_por_dos}z + {suma_cuadrados}')
        
        #(- - +)
        elif x_por_dos < 0 and y_por_dos < 0 and z_por_dos > 0:
            x_por_dos = abs(x_por_dos)
            y_por_dos = abs(y_por_dos)
            eje.set_title(f'(Ecuación de la esfera)\n {radio_cuadrado} = x^2 +{x_por_dos}x + y^2 +{y_por_dos}y + z^2 -{z_por_dos}z + {suma_cuadrados}')

        # Mostramos el resultado en una ventana
        plt.show()

#Menu principal
def menu_principal():
    menu = Tk()
    menu.title("Coordenadas de la esfera")
    menu.configure(bg= "lightblue")
    menu.minsize(width= 400, height= 100)

    titulo_1 = Label(menu, text="Coordenadas de origen:", bg="blue", fg="white", width= 50,)
    titulo_1.grid(padx= 50, pady= 5, row= 0, column= 0, columnspan= 2)

    coordenada_x = Label(menu, text= "Ingrese el valor de la coordenada x: ", bg= "lightblue");
    coordenada_x.grid(pady= 5, row= 1, column= 0, columnspan= 1)
    coordenada_y = Label(menu, text= "Ingrese el valor de la coordenada y: ", bg= "lightblue");
    coordenada_y.grid(pady= 5, row= 2, column= 0, columnspan= 1)
    coordenada_z = Label(menu, text= "Ingrese el valor de la coordenada z: ", bg= "lightblue");
    coordenada_z.grid(pady= 5, row= 3, column= 0, columnspan= 1)
    radio = Label(menu, text="Ingrese el valor del radio: ", bg= "lightblue")
    radio.grid(pady= 5, row= 4, column= 0)

    entry_x = Entry(menu)
    entry_x.grid(padx= 5, row= 1, column= 1)
    entry_y = Entry(menu)
    entry_y.grid(padx= 5, row= 2, column= 1)
    entry_z = Entry(menu)
    entry_z.grid(padx= 5, row= 3, column= 1)
    entry_radio = Entry(menu)
    entry_radio.grid(padx= 5, row= 4, column= 1)

    error = Label(menu, text="", bg= "lightblue")
    error.grid(pady= 5, row= 6, columnspan= 2)

    btn_enviar = Button(menu, text= "Enviar", width=50, relief="raised", command=lambda: esfera(entry_x, entry_y, entry_z, entry_radio, error))
    btn_enviar.grid(pady= 10, padx= 10, row= 5, column=0, columnspan= 2)

    menu.mainloop()

#Se ejecuta el programa
menu_principal()



