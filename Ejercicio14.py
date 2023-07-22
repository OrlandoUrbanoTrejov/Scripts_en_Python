""""Autor: Orlando Urbano Trejo (Lando) 
   Fecha: 13-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Calcula la cantidad de euros a monedas"""

print("-------- MENU DE CONVERSIONES --------")
print("1) Euros")
print("2) Dólares")

Opcion = int(input("Elige una opción: "))

if Opcion == 1:
    Dinero = int(input("Dinero: "))
    Euro = 0.053
    Resultado = Dinero / Euro
    print("Dinero: {:.2f} euros".format(Resultado))
elif Opcion == 2:
    Dinero = int(input("Dinero: "))
    Dolar = 16.89
    Resultado = Dinero / Dolar
    print("Dinero: {:.2f} dólares".format(Resultado))
else:
    print("Opción no válida")



