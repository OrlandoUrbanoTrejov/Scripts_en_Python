"""Autor:  Orlando Urbano Trejo (Lando) 
   Fecha:  27-07-2023
   Correo: urbanoorlando79@gmail.com

 Ejercicio: Hacer un programa que considere las siguientes opciones: 1) Cubo de un numero,2) Numero par o impar, 3) Salir """

Opcion = int(input("-----MENU DE OPCIONES-----\n"
                  "1) Cubo de un numero\n"
                  "2) Numero par o impar\n"
                  "3) Salir\n"
                  "Elige una opcion: "))

if Opcion == 1:
    Numero = int(input("Numero: "))
    Cubo = Numero ** 3
    print(f"El cubo de {Numero} es {Cubo}")
elif Opcion == 2:
    Numero = int(input("Numero: "))
    if Numero % 2 == 0:
        print("Numero par")
    else:
        print("Numero impar")
elif Opcion == 3:
    print("Fin del programa")
else:
    print("Opción invalida")

