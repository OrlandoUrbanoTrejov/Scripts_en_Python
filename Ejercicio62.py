"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  28-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por pantalla el numero en letras (dato cadena) de la cara opuesta al resultado obtenido.
Nota 1: En las caras opuestas de un dado de seis caras estan los numeros: 1-6, 2-5 y 3-4.
Nota 2: Si el numero del dado introducido es menor que 1 o mayor que 6, se mostrara el mensaje: ERROR: numero incorrecto """

Cara = int(input("Ingresa la cara del dado: "))

if Cara == 1:
    print("El valor contrario de la cara es: SEIS")
elif Cara == 2:
    print("El valor contrario de la cara es: CINCO")
elif Cara == 3:
    print("El valor contrario de la cara es: CUATRO")
elif Cara == 4:
    print("El valor contrario de la cara es: TRES")
elif Cara == 5:
    print("El valor contrario de la cara es: DOS")
elif Cara == 6:
    print("El valor contrario de la cara es: UNO")
else:
    print("ERROR: Número incorrecto")

