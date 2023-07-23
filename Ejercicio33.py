"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  18-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Ejercicio: Los alumnos de primer semestre de la carrera de Ingeniería en Sistemas Computacionales tienen que organizarse para el desfile del 20 de noviembre. Cada alumno deberá ir vestido de acuerdo al taller en el que está inscrito: Presentaran un espectáculo en la Plaza Manuel Ávila Camacho de Jilotepec (El valor por esta actividades de 1 crédito). Los Alumnos que hayan participado en la carrera tendrán 1 crédito, si logro quedar en uno de los 3 primeros lugares, tendrá 1 crédito más. Imprime el total de créditos. """

Credito = int(input("Estás inscrito a un taller (1 = Si y 2 = No): "))

if Credito == 1:
    print("Tienes un crédito")
    print("")
    Carrera = int(input("Participaste en la carrera (1 = si y 2 = No): "))

    if Carrera == 1:
        print("Tienes otro crédito")
        Lugar = int(input("Quedaste en uno de los 3 primeros lugares: "))

        if Lugar == 1:
            print("Genial, tienes tres créditos")
        elif Lugar == 2:
            print("Tienes dos créditos")
    elif Carrera == 2:
        print("Tienes solo un crédito")

elif Credito == 2:
    print("Inscríbete a un taller por favor")
    Carrera = int(input("Participaste en la carrera (1 = si y 2 = No): "))

    if Carrera == 1:
        print("Tienes un crédito")
        Lugar = int(input("Quedaste en uno de los 3 primeros lugares: "))

        if Lugar == 1:
            print("Tienes dos créditos")
        elif Lugar == 2:
            print("Tienes un crédito")
    elif Carrera == 2:
        print("No tienes créditos")
else:
    print("Opción Inválida")

