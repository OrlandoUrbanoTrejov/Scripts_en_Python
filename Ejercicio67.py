"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  28-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Imprimir una piramide numeros """

Numero = int(input("Ingresa un numero: "))

Posicion_Central = Numero
Numero_Posiciones = Numero * 2 - 1
Posicion_Inicial = Numero
Posicion_Final = Numero

for i in range(Numero):
    Contador = 1
    for j in range(1, Numero_Posiciones + 1):
        if j < Posicion_Inicial or j > Posicion_Final:
            print(" ", end="")
        else:
            if j < Numero:
                print(Contador, end="")
                Contador += 1
            else:
                print(Contador, end="")
                Contador -= 1
    print()
    Posicion_Final += 1
    Posicion_Inicial -= 1


