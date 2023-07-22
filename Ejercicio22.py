"""Autor: Orlando Urbano Trejo (Lando) 
   Fecha: 13-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Un vendedor recibe un sueldo base más un 10% por comision de sus ventas el vendedor desea
saber cuanto dinero obtendra por concepto de comisiones por las 3 ventas que realiza en el mes 
y el total que recibira en el mes tomando en cunta su base y comisiones """

Sueldo = float(input("Sueldo fijo: "))
Ventas = int(input("Ventas realizadas: "))

Comision = 0

for i in range(Ventas):
    Precio_Venta = float(input("Precio de la venta {}: ".format(i+1)))
    Comision += Precio_Venta * 0.10

Total = Comision + Sueldo

print("Comisión: ${:.2f}".format(Comision))
print("Sueldo: ${:.2f}".format(Total))

