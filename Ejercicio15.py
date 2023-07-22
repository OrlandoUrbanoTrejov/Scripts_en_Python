"""Autor: Orlando Urbano Trejo (Lando) 
   Fecha: 13-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Calcular el descuento de un medicamento"""

Nombre = input("Nombre: ")
Precio = float(input("Precio del medicamento: "))

Total = Precio - (Precio * 0.35)
print("Cliente:", Nombre, "el total a pagar: $", "{:.2f}".format(Total))


