"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  28-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Escribe un programa que reciba una año y nos diga si es bisiesto o no """

Numero = int(input("Ingresa un año: "))
if Numero %4 == 0:
    print("Año bisiesto")
else:
    print("No es año bisiesto")
