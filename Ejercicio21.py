"""Autor: Orlando Urbano Trejo (Lando) 
   Fecha: 13-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Obtener la edad de una persona en meses, si se ingresa su edaden años y meses. 
 * Ejemplo: Ingresado 3 años 4 meses debe mostrar 40 meses"""

Edad = int(input("Edad en años: "))
Meses = int(input("Cuantos meses: "))

Resultado = (Edad * 12) + Meses
print("Edad:", Resultado, "meses")

