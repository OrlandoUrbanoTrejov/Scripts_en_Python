"""Autor:  Orlando Urbano Trejo (Lando) 
   Fecha:  27-07-2023
   Correo: urbanoorlando79@gmail.com

 Ejercicio: Escribir un programa que lea un caracter en minuscula e imprima por pantalla, el mismo caracter en mayuscula """

Letra_Minuscula = input("Ingresa una letra en minúscula: ")
Letra_Mayuscula = chr(ord(Letra_Minuscula) - ord('a') + ord('A'))
print(f"La letra {Letra_Minuscula} en minúscula es {Letra_Mayuscula} en mayúscula.")

