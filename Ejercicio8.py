"""Autor: Orlando Urbano Trejo (Lando) 
   Fecha: 13-07-2023
   Correo: urbanoorlando79@gmail.com

 Ejercicio: La CONAGUA requiere determinar el pago que debe de realizar a una persona por el total de metros cúbicos que consume de agua"""

PrecioMetros = int(input("Ingresa el precio por metro: "))
Metros = int(input("Metros consumidos: "))

Resultado = PrecioMetros * Metros
print("Pago: {:.2f}".format(Resultado))

