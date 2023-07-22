"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  18-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio:Recuerda que cada materia tiene 5 unidades, una vez obtenida cada calificación por unidad, calcula el promedio de cada materia. Finalmente, calcula el promedio general. """

# En python los arreglos se conocen como: listas.
Materias = [
    "Cálculo Diferencial",
    "Fundamentos de Programación",
    "Química",
    "Fundamentos de investigación",
    "Matemáticas Discretas",
    "Desarrollo Sustentable"
]

Calificaciones = []
Promedios_Materias = [0] * 6
Promedio_General = 0

# Aqui guardamos todas las calificaciones de las materias
for i in range(6):
    print("Calificación", Materias[i])
    califs = []
    for j in range(5):
        calificacion = float(input("Unidad {}: ".format(j + 1)))
        # Guardamos las caliifcaciones en otra lista
        califs.append(calificacion)
        Promedios_Materias[i] += calificacion
    Calificaciones.append(califs)
    Promedios_Materias[i] /= 5
    Promedio_General += Promedios_Materias[i]
    print("")

Promedio_General /= 6

# Impresión de resultados
print("Unidad 1\tUnidad 2\tUnidad 3\tUnidad 4\tUnidad 5\tPromedio")
for i in range(6):
    for j in range(5):
        # el "end" sirve para imprimir los resultados en una sola linea 
        print("{:.1f}\t\t".format(Calificaciones[i][j]), end="")
    print(" {:.2f}".format(Promedios_Materias[i]))

print("\nPromedio general: {:.2f}".format(Promedio_General))

