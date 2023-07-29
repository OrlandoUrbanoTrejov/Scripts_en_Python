"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  28-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Visualizar la tarifa de luz segun el gasto de corriente electrica, para un gasto menor de: 1000 Kw, la tarifa es de 1.2 entre 1000, 1850 Kw la tarifa es 1.0 y mayor de 1850 la tarifa es de 0.9 """

Tarifa = int(input("Ingresa la tarifa de luz electrica: "))
if Tarifa < 1000:
    print("Tu tarifa es de 1.2")
elif 1000 <= Tarifa < 1850:
    print("Tu tarifa es de 1.0")
else:
     print("Tu tarifa es de 0.9")
