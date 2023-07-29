"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  28-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Ingresa un numero, calcula e imprime su raiz cuadrada, si el numero es negativo imprimir un mensaje que diga "Tiene raiz imaginaria" """

Numero = int(input("Ingresa un numero: "))
if Numero > 1:
    Resultado = Numero ** 0.5
    print("Raiz cuadrada:", Resultado)
else:
    print("Tiene raiz imaginaria")

