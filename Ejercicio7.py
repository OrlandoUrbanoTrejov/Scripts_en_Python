"""Autor: Orlando Urbano Trejo (Lando) 
   Fecha: 13-07-2023
   Correo: urbanoorlando79@gmail.com

 Ejercicio: Realice un algoritmo para leer calificaciones de N alumnos y determine el numero de alumnos aprobados y reprobados """

Alumnos = int(input("Cantidad de alumnos: "))
aprobados = 0
reprobados = 0

for i in range(Alumnos):
    Calificacion = float(input(f"Calificación del alumno {i+1} (1-100): "))
    
    if Calificacion > 70:
        print("APROBADO")
        aprobados += 1
    else:
        print("REPROBADO")
        reprobados += 1

print(f"Número de alumnos aprobados: {aprobados}")
print(f"Número de alumnos reprobados: {reprobados}")

