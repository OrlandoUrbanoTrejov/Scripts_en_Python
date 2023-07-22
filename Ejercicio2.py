"""Autor:  Orlando Urbano Trejo (Lando) 
   Fecha:  13-07-2023
   Correo: urbanoorlando79@gmail.com

 Ejercicio: Realice un algoritmo que calcule el precio total del boleto de una persona, ingresando el precio por kilometro y  la cantidad de kilometros a recorrer. Represente el diagrama de flujo, el pseudocodigo correspondiente
 """
Precio_Kilometro = float(input("Precio por kilometro:"))
Distancia = float(input("Kilometros a recorrer:"))
Boleto = Precio_Kilometro * Distancia
print("Precio boleto: $",Boleto)
