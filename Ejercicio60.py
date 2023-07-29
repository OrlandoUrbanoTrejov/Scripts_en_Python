"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  28-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Realiza un programa que clasifique un triangulo tras recibir el tamano de sus lados. Se debe clasificar como: triangulo rectangulo, isosceles, equilatero o escaleno. """


print("Ingresa el tamaño del lado 1: ")
Lado_1 = int(input())
print("Ingresa el tamaño del lado 2: ")
Lado_2 = int(input())
print("Ingresa el tamaño del lado 3: ")
Lado_3 = int(input())
if Lado_1 > Lado_2 and Lado_1 > Lado_3:
    if Lado_1 ** 2 == Lado_2 ** 2 + Lado_3 ** 2:
        print("ES UN TRIÁNGULO RECTÁNGULO")
elif Lado_2 > Lado_1 and Lado_2 > Lado_3:
    if Lado_2 ** 2 == Lado_1 ** 2 + Lado_3 ** 2:
        print("ES UN TRIÁNGULO RECTÁNGULO")
elif Lado_3 > Lado_1 and Lado_3 > Lado_2:
    if Lado_3 ** 2 == Lado_1 ** 2 + Lado_2 ** 2:
        print("ES UN TRIÁNGULO RECTÁNGULO")
elif Lado_1 == Lado_2 and Lado_1 != Lado_3 or Lado_1 == Lado_3 and Lado_1 != Lado_2 or Lado_2 == Lado_3 and Lado_2 != Lado_1:
    print("ES UN TRIÁNGULO ISÓSCELES")
elif Lado_1 == Lado_2 and Lado_3 == Lado_2:
    print("ES UN TRIÁNGULO EQUILÁTERO")
else:
    print("ES UN TRIÁNGULO ESCALENO")

