"""Autor: Orlando Urbano Trejo (Lando) 
   Fecha: 13-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Escriba un algoritmo que dada la cantidad de monedas de 5-10-20 pesos, 
 * diga la cantidad de dinero que se tiene en total"""

Cajero = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50]
Cantidad = 0

for i in range(len(Cajero)):
    C = int(input("Cantidad de {:.2f} que tiene: ".format(Cajero[i])))
    Cantidad += C * Cajero[i]
    print("Total: ${:.2f}".format(Cantidad))

