"""Autor:  Orlando Urbano Trejo (Lando) 
   Fecha:  27-07-2023
   Correo: urbanoorlando79@gmail.com

 Ejercicio: Realizar la serie Fibonacci """

Numero = int(input("Ingresa un numero: "))
x, y, z = 0,1,1
print("1,",end=" ")
for i in range(1, Numero + 1):
    z = x + y
    x = y
    y = z
    print(z, end= ", ")
print()

