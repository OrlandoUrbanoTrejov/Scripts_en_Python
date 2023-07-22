"""Autor: Orlando Urbano Trejo (Lando)
   Fecha: 13-07-2023
   Correo: urbanoorlando79@gmail.com

 Ejercicio: Realice un algoritmo que determine el sueldo semanal de N trabajadores considerando que se les descuenta
5% de su sueldo si ganan entre 0 y 150 pesos. Se les descuenta 7% si ganan mas de 150 pero menos de 300, y 
9% si ganan mas de 300 pero menos de 450. Los datos son horas trabajadas, sueldo por hora, y nombre de cada trabajador """

Trabajadores = int(input("Número de trabajadores: "))

for i in range(Trabajadores):
    Nombres = input(f"Nombre del trabajador {i+1}: ")
    Horas_Trabajadas = float(input("Horas trabajadas: "))
    Sueldo_Hora = float(input("Sueldo por hora: "))

    Salario = Horas_Trabajadas * Sueldo_Hora
    Nuevo_Salario = 0

    if Salario >= 0 and Salario <= 150:
        Nuevo_Salario = Salario * 0.95
    elif Salario > 150 and Salario <= 300:
        Nuevo_Salario = Salario * 0.93
    elif Salario > 300 and Salario <= 450:
        Nuevo_Salario = Salario * 0.91

    Total = Salario - Nuevo_Salario
    print(f"Trabajador: {Nombres}")
    print(f"Salario final: {Total:.2f}")

