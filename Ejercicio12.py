"""Autor: Orlando Urbano Trejo (Lando) 
   Fecha: 13-07-2023
   Correo: urbanoorlando79@gmail.com

 Ejercicio: Una persona recibe un prestamo de 10,000 de un banco y desea saber cuanto pagara de interes, 
 si el banco le cobrara una tasa de 27% anual */"""

Prestamo = 10000
Interes = 0.27

Tiempo = int(input("Año en que se solicitó el préstamo: "))
Tiempo_Transcurrido = int(input("Año actual: "))

for i in range(Tiempo, Tiempo_Transcurrido + 1):
    Prestamo = Prestamo + (Prestamo * Interes)
    print("El interés en el año {} es de: ${:.2f}".format(i, Prestamo))   

