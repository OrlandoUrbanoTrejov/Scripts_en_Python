"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  28-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Realiza un programa que calcule la aceptacion de una solicitud en base a los siguientes parametros: edad, nota y sexo.
* Minimo: Nota (5), edad (18), sexo M -> POSIBLE
* Minimo: Nota (5), edad (18), sexo F -> ACEPTADA
* Otros casos -> NO ACEPTADA  """

Nota = input("Ingresa tu calificación obtenida: ")
Edad = input("Ingresa tu edad: ")
Sexo = input("Ingresa sexo: ")

if Nota == "5" and Edad == "18" and Sexo == "M":
     print(f"Solicitud ({Nota}), Edad ({Edad}), sexo ({Sexo}) ---> SOLICITUD POSIBLE")
elif Nota == "5" and Edad == "18" and Sexo == "F":
    print(f"Solicitud ({Nota}), Edad ({Edad}), sexo ({Sexo}) ---> SOLICITUD ACEPTADA")
else:
    print("SOLICITUD NO ACEPTADA")


