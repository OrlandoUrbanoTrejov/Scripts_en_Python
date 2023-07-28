"""Autor:  Orlando Urbano Trejo (Lando) 
   Fecha:  27-07-2023
   Correo: urbanoorlando79@gmail.com

 Ejercicio: Realiza las tablas de multiplicar """

Filas = int(input("Numero de filas: "))
Columnas = int(input("Numero de columnas: "))

for i in range(1, Filas + 1):
    print("\t")
    for j in range(1, Columnas + 1):
        print(i*j,"\t", end="")
print()
