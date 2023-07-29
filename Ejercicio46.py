"""Autor:  Orlando Urbano Trejo (Lando) 
   Fecha:  27-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio:  Escribir un programa que lea los valores de los catetos de un triangulo rectangulo y calcule cual es la hipotenusa, area y el perimetro del triangulo mediante las siguientes expresiones """

Cateto1 = float(input("Valor del cateto 1: "))
Cateto2 = float(input("Valor del cateto 2: "))

Hipotenusa = (Cateto1**2 + Cateto2**2)**0.5
Area = (Cateto1 * Cateto2) / 2
Perimetro = Cateto1 + Cateto2 + Hipotenusa

print("Hipotenusa:", Hipotenusa)
print("Area:", Area)
print("Perimetro:", Perimetro)
