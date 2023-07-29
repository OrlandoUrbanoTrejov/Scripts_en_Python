"""Autor:  Orlando Urbano Trejo (Lando) 
   Fecha:  27-07-2023
   Correo: urbanoorlando79@gmail.com

 Ejercicio: Realiza un codigo que imprima los numeros de 5 en 5 hasta donde el usuario digite """

Numero = int(input("Ingresa un numero: "))
for i in range(1, Numero + 1):
    if i % 5 == 0:
       print(i, end = ", ")
print()
