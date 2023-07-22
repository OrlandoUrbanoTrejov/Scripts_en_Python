"""Autor: Orlando Urbano Trejo (Lando)
   Fecha: 13-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Calcular el nuevo salario de un empleado si se le descuenta el 20% de su salario actual """

Nombre = input("Nombre: ")
Salario = float(input("Salario: "))

Total = Salario - (Salario * 0.20)
print("Empleado:", Nombre, "su salario es:", "{:.2f}".format(Total))

