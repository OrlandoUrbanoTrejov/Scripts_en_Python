"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  28-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Realiza un programa que lea una cadena por teclado y compruebe si es una letra mayuscula """

Letra = input("Ingresa una letra: " )
if 'A' <= Letra <= 'Z':
    print(f"La letra {Letra} es mayuscula")
else:
    print(f"La letra {Letra} es minuscula")
