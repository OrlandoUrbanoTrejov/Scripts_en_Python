"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  17-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Realiza un codigo que imprima un arbol de navidad, de la siguiente manera. Recuerda hacer uso de ciclos"""

Altura = int(input("Altura del árbol: "))

# Imprimir la parte superior del árbol
for i in range(1, Altura + 1):
    Espacios = Altura - i

    # Imprimir espacios en blanco
    for j in range(Espacios):
        print(" ", end="")

    # Imprimir asteriscos
    for j in range(2 * i - 1):
        print("*", end="")

    print()

Tronco = Altura - 1
# Imprimir el tronco del árbol
for i in range(2):
    for j in range(Tronco):
        print(" ", end="")

    print("**")

