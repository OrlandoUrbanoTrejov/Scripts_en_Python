"""Autor: Orlando Urbano Trejo (Lando) 
   Fecha: 13-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Calcula el precio de un boleto de viaje, tomando en cuenta el numero de kilometros que se van a recorrer. El precio por kilometro es de $20.50"""

Precio_Boleto = 20.50

Num_Kilometros = float(input("Número de kilómetros a recorrer: "))
Precio = Precio_Boleto * Num_Kilometros

print("El precio de tu boleto es de: ${:.2f}".format(Precio))

