"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  28-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Sumar numeros pares desde n hasta m """

Num_Inicio = int(input("Ingresa un numero para el inicio de la suma: "))
Num_Final = int(input("Ingresa un numero para el limite de la suma: "))
Suma = 0

for i in range(Num_Inicio, Num_Final + 1):
    if i % 2 == 0:
        Suma += i

print("Suma:", Suma)

