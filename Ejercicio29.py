"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  17-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Haciendo uso de arreglos, almacena la calificación de una materia (Recuerda que son 5 unidades). Posteriormente, calcula el promedio final e imprime los resultados."""

calificacion = [0] * 5
materia = input("Materia: ")

for i in range(1, 6):
    calificacion[i - 1] = int(input(f"Calificacion en la Unidad {i}: "))
    suma += calificacion[i - 1]

print(f"Asignatura: {materia}")
print("Unidad 1\tUnidad 2\tUnidad 3\tUnidad 4\tUnidad 5\tPromedio")

for i in range(5):
    print(f"{calificacion[i]:8}\t", end="")

promedio = suma / 5
print(f"{promedio:.2f}")

