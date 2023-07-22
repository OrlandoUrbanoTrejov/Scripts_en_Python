"""Autor: Orlando Urbano Trejo (Lando)
   Fecha: 13-07-2023
   Correo: urbanoorlando79@gmail.com

 Ejercicio: Se requiere determinar el tiempo en que tarda una persona en llegar de una ciudad a otra en bicicleta. Considerando que lleva una velocidad constante 
"""

Distancia = float(input("Distancia (en kilómetros): "))
Velocidad = float(input("Velocidad (en kilómetros por hora): "))

tiempo_total = (Distancia * Velocidad) / 60

print(f"El tiempo total de viaje es de {tiempo_total} horas.")
