"""Autor: Orlando Urbano Trejo (Lando) 
   Fecha: 13-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Escriba un algoritmo que, dado el número de horas trabajadas por un empleado y el sueldo por hora, calcule el sueldo total de ese empleado"""

Horas = float(input("Horas Trabajadas: "))
Sueldo_Hora = float(input("Sueldo por hora:"))
Sueldo_Final = Horas * Sueldo_Hora
print("Sueldo total: ${:.2f}".format(Sueldo_Final))
