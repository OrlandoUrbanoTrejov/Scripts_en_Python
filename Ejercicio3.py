"""Autor: Orlando Urbano Trejo (Lando) 
   Fecha: 13-07-2023
   Correo: urbanoorlando79@gmail.com

 Ejercicio: Se desea saber el total de una caja registradora de un almacén, se conoce el numero de billetes y monedas asi como su valor
 """
Dinero = [1000, 500, 200, 100, 50, 20, 5, 2, 1, 0.50, 0.20, 0.10]
Resultado = 0

for i in range(12):
    print("Cantidad de dinero que tiene: %.2f pesos" % dinero[i])
    Convertidor = int(input())
    Resultado = Resultado + (Convertidor * dinero[i])
    print("Total almacenado: $",Resultado)



