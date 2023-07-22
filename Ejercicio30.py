"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  18-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Haciendo uso de 2 arreglos, almacena 5 números en cada arreglo, posteriormente vas a multiplicar los arreglos """

Primero = []
Segundo = []
Multiplicacion = []

for i in range(5):
    Primero.append(int(input("Valor " + str(i+1) + ": ")))

print()

for i in range(4, -1, -1):
    Suma = i + 2
    Segundo.insert(0, int(input("Valor " + str(Suma-1) + ": ")))

for i in range(5):
    Multiplicacion.append(Primero[i] * Segundo[i])

print("Resultado:", *Multiplicacion)

