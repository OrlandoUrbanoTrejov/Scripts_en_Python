"""Autor: Orlando Urbano Trejo (Lando) 
   Fecha: 13-07-2023
   Correo: urbanoorlando79@gmail.com

 Ejercicio: Se requiere determinar el costo que tendra que realizar una llamada telefonica con base en el tiempo que dura la llamada y el costo por minuto
 """

Tiempo = int(input("Tiempo de la llamada en minutos: "))
Costo = float(input("Costo por minuto en pesos: "))

Total = Tiempo * Costo
print("Costo de la llamada:$",Total)

