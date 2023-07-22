"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  17-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Solicita un numero al usuario y calcula su factorial"""
Resultado = 1
Numero = int(input("Ingresa un numero: "))
for i in range(1, Numero + 1):
    Resultado *= i
    print(Resultado)
   

