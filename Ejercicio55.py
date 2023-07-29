"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  28-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Calcular el mayor de dos numeros leidos del teclado y visualzarlos en pantalla """

Numero1 = int(input("Ingresa el numero 1: "))
Numero2 = int(input("Ingresa el numero 2: "))

if Numero1 > Numero2:
    print("El numero mayor es:", Numero1)
elif Numero1 == Numero2:
    print("Los numeros son iguales")
else:
     print("El numero mayor es:", Numero2)

