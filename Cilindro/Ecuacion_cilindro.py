from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# (Y, Z)
def cilindro_caso_1(coordenada_y_ent, coordenada_z_ent, radio_ent, error):
    # Tomar los valores
    coordenada_y = coordenada_y_ent.get()
    coordenada_z = coordenada_z_ent.get()
    radio = radio_ent.get()

    # Convertir los datos a enteros
    coordenada_y = float(coordenada_y)
    coordenada_z = float(coordenada_z)
    radio = float(radio)

    if radio <= 0:
        error.config(text="El radio no puede ser igual o menor a cero", fg="red")
    else:
        # Creamos una figura 3D
        figura = plt.figure()
        eje = figura.add_subplot(111, projection='3d')

        # Definir el radio y la altura del cilindro
        radius = radio
        altura = 3

        # Crear la superficie del cilindro
        theta = np.linspace(0, 2*np.pi, 100)
        valor_x = np.linspace(0, altura, 100)

        # Graficar la malla
        theta, valor_x = np.meshgrid(theta, valor_x)

        # Ejes
        eje_x = valor_x
        eje_y = radius * np.cos(theta) + coordenada_y
        eje_z = radius * np.sin(theta) + coordenada_z

        eje.plot_surface(eje_x, eje_y, eje_z, color = 'b', alpha=0.7)

        # Mostramos las letras de las coordenadas
        eje.set_xlabel('EJE X')
        eje.set_ylabel('EJE Y')
        eje.set_zlabel('EJE Z')

        # -------------------- Parte de la ecuacion -----------------------

        # Operaciones
        operacion_1 = 0  # radio al cuadrado
        operacion_2 = 0  # coordenada_1 multiplicada por dos
        operacion_3 = 0  # coordenada_1 al cuadrado
        operacion_4 = 0  # coordenada_2 multiplicada por dos
        operacion_5 = 0  # coordenada_2 al cudarado
        operacion_6 = 0  # Suma del resultado de la op_3 y la op_5

        # Operacion para el radio
        operacion_1 = radio * radio
        # Operaciones para la segunda coordenada ingresada (en este caso y)
        operacion_4 = coordenada_y * 2
        operacion_5 = coordenada_y * coordenada_y
        # Operaciones para la primera coordenada ingresada (en este caso z)
        operacion_2 = coordenada_z * 2
        operacion_3 = coordenada_z * coordenada_z
        # Suma de los enteros
        operacion_6 = operacion_3 + operacion_5

        # ------------------------------------------------- Mostrar la ecuacion del cilindro --------------------------------------------------
        # (+ +)
        if operacion_2 > 0 and operacion_4 > 0:
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = y^2 -{operacion_2}y + z^2 -{operacion_4}z + {operacion_6}')
        # (- -)
        elif operacion_2 < 0 and operacion_4 < 0:
            operacion_2 = abs(operacion_2)
            operacion_4 = abs(operacion_4)
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = y^2 +{operacion_2}y + z^2 +{operacion_4}z + {operacion_6}')
        
        # (0 0) 
        elif operacion_2 == 0 and operacion_4 == 0 :
            eje.set_title(f'(Ecuación de la esfera)\n {operacion_1} = y^2 + z^2')

        # (+ -)
        elif operacion_2 > 0 and operacion_4 < 0:
            operacion_4 = abs(operacion_4)
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = y^2 -{operacion_2}y + z^2 +{operacion_4}z + {operacion_6}')

        # (- +)
        elif operacion_2 < 0 and operacion_4 > 0:
            operacion_2 = abs(operacion_2)
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = y^2 +{operacion_2}y + z^2 -{operacion_4}z + {operacion_6}')

        # (+ 0)
        elif operacion_2 > 0 and operacion_4 == 0:
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = y^2 -{operacion_2}y + z^2 + {operacion_6}')

        # (0 +)
        elif operacion_2 == 0 and operacion_4 > 0:
            operacion_2 = abs(operacion_2)
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = y^2 + z^2 -{operacion_4}z + {operacion_6}')

        # (- 0)
        elif operacion_2 < 0 and operacion_4 == 0:
            operacion_2 = abs(operacion_2)
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = y^2 +{operacion_2}y + z^2 + {operacion_6}')

        # (0 -)
        elif operacion_2 == 0 and operacion_4 < 0:
            operacion_4 = abs(operacion_4)
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = y^2 + z^2 +{operacion_4}z + {operacion_6}')

        # Mostramos el resultado en una ventana
        plt.show()

# (X, Z)
def cilindro_caso_2(coordenada_x_ent, coordenada_z_ent, radio_ent, error):
    # Tomar los valores
    coordenada_x = coordenada_x_ent.get()
    coordenada_z = coordenada_z_ent.get()
    radio = radio_ent.get()

    # Convertir los datos a enteros
    coordenada_x = float(coordenada_x)
    coordenada_z = float(coordenada_z)
    radio = float(radio)

    if radio <= 0:
        error.config(text="El radio no puede ser igual o menor a cero", fg="red")
    else:

        # Creamos una figura 3D
        figura = plt.figure()
        eje = figura.add_subplot(111, projection='3d')

        # Definir el radio y la altura del cilindro
        radius = radio
        altura = 3

        # Crear la superficie del cilindro
        theta = np.linspace(0, 2*np.pi, 100)
        valor_y = np.linspace(0, altura, 100)

        # Graficar la malla
        theta, valor_y = np.meshgrid(theta, valor_y)

        # Ejes
        eje_x = radius * np.cos(theta) + coordenada_x
        eje_y = valor_y
        eje_z = radius * np.sin(theta) + coordenada_z

        eje.plot_surface(eje_x, eje_y, eje_z, color = 'b', alpha=0.7)

        # Mostramos las letras de las coordenadas
        eje.set_xlabel('EJE X')
        eje.set_ylabel('EJE Y')
        eje.set_zlabel('EJE Z')

        # -------------------- Parte de la ecuacion -----------------------

        # Operaciones
        operacion_1 = 0  # radio al cuadrado
        operacion_2 = 0  # coordenada_1 multiplicada por dos
        operacion_3 = 0  # coordenada_1 al cuadrado
        operacion_4 = 0  # coordenada_2 multiplicada por dos
        operacion_5 = 0  # coordenada_2 al cudarado
        operacion_6 = 0  # Suma del resultado de la op_3 y la op_5

        # Operacion para el radio
        operacion_1 = radio * radio
        # Operaciones para la primera coordenada ingresada (en este caso x)
        operacion_2 = coordenada_x * 2
        operacion_3 = coordenada_x * coordenada_x
        # Operaciones para la segunda coordenada ingresada (en este caso z)
        operacion_4 = coordenada_z * 2
        operacion_5 = coordenada_z * coordenada_z
        # Suma de los enteros
        operacion_6 = operacion_3 + operacion_5

        # ------------------------------------------------- Mostrar la ecuacion del cilindro --------------------------------------------------
        # (+ +)
        if operacion_2 > 0 and operacion_4 > 0:
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = x^2 -{operacion_2}x + z^2 -{operacion_4}z + {operacion_6}')
        # (- -)
        elif operacion_2 < 0 and operacion_4 < 0:
            operacion_2 = abs(operacion_2)
            operacion_4 = abs(operacion_4)
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = x^2 +{operacion_2}x + z^2 +{operacion_4}z + {operacion_6}')
        
        # (0 0) 
        elif operacion_2 == 0 and operacion_4 == 0 :
            eje.set_title(f'(Ecuación de la esfera)\n {operacion_1} = x^2 + z^2')

        # (+ -)
        elif operacion_2 > 0 and operacion_4 < 0:
            operacion_4 = abs(operacion_4)
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = x^2 -{operacion_2}x + z^2 +{operacion_4}z + {operacion_6}')

        # (- +)
        elif operacion_2 < 0 and operacion_4 > 0:
            operacion_2 = abs(operacion_2)
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = x^2 +{operacion_2}x + z^2 -{operacion_4}z + {operacion_6}')

        # (+ 0)
        elif operacion_2 > 0 and operacion_4 == 0:
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = x^2 -{operacion_2}x + z^2 + {operacion_6}')

        # (0 +)
        elif operacion_2 == 0 and operacion_4 > 0:
            operacion_2 = abs(operacion_2)
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = x^2 + z^2 -{operacion_4}z + {operacion_6}')

        # (- 0)
        elif operacion_2 < 0 and operacion_4 == 0:
            operacion_2 = abs(operacion_2)
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = x^2 +{operacion_2}x + z^2 + {operacion_6}')

        # (0 -)
        elif operacion_2 == 0 and operacion_4 < 0:
            operacion_4 = abs(operacion_4)
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = x^2 + z^2 +{operacion_4}z + {operacion_6}')

        # Mostramos el resultado en una ventana
        plt.show()

# (X, Y)      
def cilindro_caso_3(coordenada_x_ent, coordenada_y_ent, radio_ent, error):
    # Tomar los valores
    coordenada_x = coordenada_x_ent.get()
    coordenada_y = coordenada_y_ent.get()
    radio = radio_ent.get()

    # Convertir los datos a enteros
    coordenada_x = float(coordenada_x)
    coordenada_y = float(coordenada_y)
    radio = float(radio)

    if radio <= 0:
        error.config(text="El radio no puede ser igual o menor a cero", fg="red")
    else:
        # Creamos una figura 3D
        figura = plt.figure()
        eje = figura.add_subplot(111, projection='3d')

        # Definir el radio y la altura del cilindro
        radius = radio
        altura = 3

        # Crear la superficie del cilindro
        theta = np.linspace(0, 2*np.pi, 100)
        valor_z = np.linspace(0, altura, 100)

        # Graficar la malla
        theta, valor_z = np.meshgrid(theta, valor_z)

        # Ejes
        eje_x = radius * np.cos(theta) + coordenada_x
        eje_y = radius * np.sin(theta) + coordenada_y
        eje_z = valor_z

        eje.plot_surface(eje_x, eje_y, eje_z, color = 'b', alpha=0.7)

        # Mostramos las letras de las coordenadas
        eje.set_xlabel('EJE X')
        eje.set_ylabel('EJE Y')
        eje.set_zlabel('EJE Z')

        # -------------------- Parte de la ecuacion -----------------------

        # Operaciones
        operacion_1 = 0  # radio al cuadrado
        operacion_2 = 0  # coordenada_1 multiplicada por dos
        operacion_3 = 0  # coordenada_1 al cuadrado
        operacion_4 = 0  # coordenada_2 multiplicada por dos
        operacion_5 = 0  # coordenada_2 al cudarado
        operacion_6 = 0  # Suma del resultado de la op_3 y la op_5

        # Operacion para el radio
        operacion_1 = radio * radio
        # Operaciones para la primera coordenada ingresada (en este caso x)
        operacion_2 = coordenada_x * 2
        operacion_3 = coordenada_x * coordenada_x
        # Operaciones para la segunda coordenada ingresada (en este caso y)
        operacion_4 = coordenada_y * 2
        operacion_5 = coordenada_y * coordenada_y
        # Suma de los enteros
        operacion_6 = operacion_3 + operacion_5

        # ------------------------------------------------- Mostrar la ecuacion del cilindro --------------------------------------------------
        
        # (+ +)
        if operacion_2 > 0 and operacion_4 > 0:
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = x^2 -{operacion_2}x + y^2 -{operacion_4}y + {operacion_6}')
        # (- -)
        elif operacion_2 < 0 and operacion_4 < 0:
            operacion_2 = abs(operacion_2)
            operacion_4 = abs(operacion_4)
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = x^2 +{operacion_2}x + y^2 +{operacion_4}y + {operacion_6}')
        
        # (0 0) 
        elif operacion_2 == 0 and operacion_4 == 0 :
            eje.set_title(f'(Ecuación de la esfera)\n {operacion_1} = x^2 + y^2')

        # (+ -)
        elif operacion_2 > 0 and operacion_4 < 0:
            operacion_4 = abs(operacion_4)
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = x^2 -{operacion_2}x + y^2 +{operacion_4}y + {operacion_6}')

        # (- +)
        elif operacion_2 < 0 and operacion_4 > 0:
            operacion_2 = abs(operacion_2)
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = x^2 +{operacion_2}x + y^2 -{operacion_4}y + {operacion_6}')

        # (+ 0)
        elif operacion_2 > 0 and operacion_4 == 0:
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = x^2 -{operacion_2}x + y^2 + {operacion_6}')

        # (0 +)
        elif operacion_2 == 0 and operacion_4 > 0:
            operacion_2 = abs(operacion_2)
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = x^2 + y^2 -{operacion_4}y + {operacion_6}')

        # (- 0)
        elif operacion_2 < 0 and operacion_4 == 0:
            operacion_2 = abs(operacion_2)
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = x^2 +{operacion_2}x + y^2 + {operacion_6}')

        # (0 -)
        elif operacion_2 == 0 and operacion_4 < 0:
            operacion_4 = abs(operacion_4)
            eje.set_title(f'(Ecuacion del cilindro)\n  {operacion_1} = x^2 + y^2 +{operacion_4}y + {operacion_6}')
        
        # Mostramos el resultado en una ventana
        plt.show()

def caso_1():
    caso_1 = Toplevel()
    caso_1.configure(bg= "lightblue")
    caso_1.minsize(width= 400, height= 100)

    titulo_1 = Label(caso_1, text="Coordenadas en caso de que X sea el eje paralelo", bg="blue", fg="white", width= 50,)
    titulo_1.grid(padx= 50, pady= 5, row= 0, column= 0, columnspan= 2)

    coordenada_y = Label(caso_1, text= "Ingrese el valor de la coordenada y: ", bg= "lightblue");
    coordenada_y.grid(pady= 5, row= 1, column= 0, columnspan= 1)
    coordenada_z = Label(caso_1, text= "Ingrese el valor de la coordenada z: ", bg= "lightblue");
    coordenada_z.grid(pady= 5, row= 2, column= 0, columnspan= 1)
    radio = Label(caso_1, text="Ingrese el valor del radio: ", bg= "lightblue")
    radio.grid(pady= 5, row= 3, column= 0)

    entry_y = Entry(caso_1)
    entry_y.grid(padx= 5, row= 1, column= 1)
    entry_z = Entry(caso_1)
    entry_z.grid(padx= 5, row= 2, column= 1)
    entry_radio = Entry(caso_1)
    entry_radio.grid(padx= 5, row= 3, column= 1)

    error = Label(caso_1, text="", bg= "lightblue")
    error.grid(pady= 5, row= 5, columnspan= 2)

    btn_enviar = Button(caso_1, text= "Enviar", width=50, relief="raised", command=lambda: cilindro_caso_1(entry_y, entry_z, entry_radio, error))
    btn_enviar.grid(pady= 10, padx= 10, row= 4, column=0, columnspan= 2)

def caso_2():
    caso_2 = Toplevel()
    caso_2.configure(bg= "lightblue")
    caso_2.minsize(width= 400, height= 100)
    
    titulo_1 = Label(caso_2, text="Coordenadas en caso de que Y sea el eje paralelo", bg="blue", fg="white", width= 50,)
    titulo_1.grid(padx= 50, pady= 5, row= 0, column= 0, columnspan= 2)

    coordenada_x = Label(caso_2, text= "Ingrese el valor de la coordenada x: ", bg= "lightblue");
    coordenada_x.grid(pady= 5, row= 1, column= 0, columnspan= 1)
    coordenada_z = Label(caso_2, text= "Ingrese el valor de la coordenada z: ", bg= "lightblue");
    coordenada_z.grid(pady= 5, row= 2, column= 0, columnspan= 1)
    radio = Label(caso_2, text="Ingrese el valor del radio: ", bg= "lightblue")
    radio.grid(pady= 5, row= 3, column= 0)

    entry_x = Entry(caso_2)
    entry_x.grid(padx=5, row=1, column=1)
    entry_z = Entry(caso_2)
    entry_z.grid(padx=5, row=2, column=1)
    entry_radio = Entry(caso_2)
    entry_radio.grid(padx=5, row=3, column=1)

    error = Label(caso_2, text="", bg= "lightblue")
    error.grid(pady= 5, row= 5, columnspan= 2)

    btn_enviar = Button(caso_2, text= "Enviar", width=50, relief="raised", command=lambda: cilindro_caso_2(entry_x, entry_z, entry_radio, error))
    btn_enviar.grid(pady= 10, padx= 10, row= 4, column=0, columnspan= 2)

def caso_3():
    caso_3 = Toplevel()
    caso_3.configure(bg= "lightblue")
    caso_3.minsize(width= 400, height= 100)
    
    titulo_1 = Label(caso_3, text="Coordenadas en caso de que Z sea el eje paralelo", bg="blue", fg="white", width= 50,)
    titulo_1.grid(padx= 50, pady= 5, row= 0, column= 0, columnspan= 2)

    coordenada_x = Label(caso_3, text= "Ingrese el valor de la coordenada x: ", bg= "lightblue");
    coordenada_x.grid(pady= 5, row= 1, column= 0, columnspan= 1)
    coordenada_y = Label(caso_3, text= "Ingrese el valor de la coordenada y: ", bg= "lightblue");
    coordenada_y.grid(pady= 5, row= 2, column= 0, columnspan= 1)
    radio = Label(caso_3, text="Ingrese el valor del radio: ", bg= "lightblue")
    radio.grid(pady= 5, row= 3, column= 0)

    entry_x = Entry(caso_3)
    entry_x.grid(padx=5, row=1, column=1)
    entry_y = Entry(caso_3)
    entry_y.grid(padx=5, row=2, column=1)
    entry_radio = Entry(caso_3)
    entry_radio.grid(padx=5, row=3, column=1)

    error = Label(caso_3, text="", bg= "lightblue")
    error.grid(pady= 5, row= 5, columnspan= 2)

    btn_enviar = Button(caso_3, text= "Enviar", width=50, relief="raised", command=lambda: cilindro_caso_3(entry_x, entry_y, entry_radio, error))
    btn_enviar.grid(pady= 10, padx= 10, row= 4, column=0, columnspan= 2)

#Menu principal
def menu_principal():
    main = Tk()
    main.title("Coordenadas de origen")
    main.configure(bg= "lightblue")
    # variable para el radiobutton
    seleccion = IntVar()

    titulo_1 = Label(main, text="BIENVENIDO", bg="blue", fg="white", width= 50,)
    titulo_1.grid(padx= 50, pady= 5, row= 0, column= 0, columnspan= 2)
    titulo_2 = Label(main, text="Seleccione el eje que sera paralelo a la figura", bg= "lightblue", width= 50)
    titulo_2.grid(padx= 50, pady= 5, row= 1, column= 0, columnspan= 2)

    opcion_x = Radiobutton(main, text= "Eje x", bg= "lightblue", value= 1, variable= seleccion, command= caso_1)
    opcion_x.grid(padx= 50, pady= 5, row= 2, column=0, columnspan= 2)

    opcion_y = Radiobutton(main, text= "Eje y", bg= "lightblue", value= 2, variable= seleccion, command= caso_2)
    opcion_y.grid(padx= 50, pady= 5, row= 3, column=0, columnspan= 2)

    opcion_z = Radiobutton(main, text= "Eje z", bg= "lightblue", value= 3, variable= seleccion, command= caso_3)
    opcion_z.grid(padx= 50, pady= 5, row= 4, column=0, columnspan= 2)
    
    main.mainloop()

#Se ejecuta el programa
menu_principal()