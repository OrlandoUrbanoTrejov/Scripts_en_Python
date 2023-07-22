"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  17-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Solicita al usuario el numero de alumnos en un salon, posteriormente pida la edad de cada uno de ellas y calcula el promedio de edad"""

Suma = 0
Promedio = 0
Alumno = int(input("Cuantos alumnos hay en el salon: "))
for i in range(Alumno):
    Edad = int(input(f"Edad del alumno {i+1}: "))
    Suma += Edad

Promedio = Suma / Alumno
print("El promedio de las edades de los alumnos es: ",Promedio)
