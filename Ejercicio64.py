"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  28-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Escribir en lenguaje C un programa que:
1) Pida por teclado una hora en tres variables: horas, minutos y segundos (datos enteros).
2) Muestre por pantalla:
"HORA CORRECTA", en el caso de que la hora sea valida.
"HORA INCORRECTA", en el caso de que la hora no sea valida.
Nota: para que una hora sea valida, se tiene que cumplir que:
    Las horas deben ser mayor o igual que 0 y menor o igual que 23.
    Los minutos deben ser mayor o igual que 0 y menor o igual que 59.
    Los segundos deben ser mayor o igual que 0 y menor o igual que 59.""" 

Horas = int(input("Ingresa las horas: "))
Minutos = int(input("Ingresa los minutos: "))
Segundos = int(input("Ingresa los segundos: "))

if 0 <= Horas <= 23 and 0 <= Minutos <= 59 and 0 <= Segundos <= 59:
    print("HORA CORRECTA")
else:
    print("HORA INCORRECTA")

