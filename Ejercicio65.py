"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  28-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Determina si un numero es primo (Un numero es primo si es divisible entre 1 y entres si mismo """

Numero = int(input("Ingresa un numero: "))
Contador = 0

for i in range(1, Numero + 1):
    if Numero % i == 0:
        Contador += 1

if Contador > 2:
    print("No es primo")
else:
    print("Es primo")

