"""Autor:  Orlando Urbano Trejo (Lando) 
   Fecha:  27-07-2023
   Correo: urbanoorlando79@gmail.com

 Ejercicio: Realiza un codigo que calcule la siguiente suma (1-2+3-4+5-6 hasta n) donde n sea ingresada por el usuario """

Numero = int(input("Ingresa un numero: "))
Pares, Impares, Negativos = 0,0,0
for i in range(1 , Numero + 1):
    if i % 2 == 0:
        Negativos = i * (-1)
        Pares += Negativos
    else:
        Impares += i
print("Suma: ", Pares + Impares)
