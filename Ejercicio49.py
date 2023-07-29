"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  28-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Define un array de 10 numeros enteros con nombre Num y asigna 5 valores.Muestra el contenido de todos los elementos de el array """

Num = [0] * 12
Num[1] = 2
Num[3] = 4
Num[6] = -2
Num[7] = 6
 #Usamos un ciclo for para mostrar las posciones
for i in range(1, 11):
    print(f"Posición {i}: {Num[i]}")


