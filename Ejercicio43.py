"""Autor:  Orlando Urbano Trejo (Lando) 
   Fecha:  27-07-2023
   Correo: urbanoorlando79@gmail.com

 Ejercicio: Hacer un programa que simule un cajero automatico con un salario inicial de 1000 """
 
print("1) Ingresar dinero")
print("2) Retirar dinero")
print("3) Salir")
Saldo = 1000
Dinero, Nuevo_Saldo = 0,0
Opcion = int(input("Elige una opcion: "))
if Opcion == 1:
    Dinero = int(input("Cuanto dinero vas a ingresar: "))
    Nuevo_Saldo = Dinero + Saldo
    print("Tu nuevo saldo es de: ",Nuevo_Saldo)
elif Opcion == 2:
    Dinero = int(input("Cuanto dinero vas a retirar: "))
    if Dinero < 1000:    
        Nuevo_Saldo = Saldo - Dinero
        print("Tu nuevo saldo es de: ",Nuevo_Saldo)
    else:
        print("Saldo insuficiente")
elif Opcion == 3:
    print("Fin del programa")
else:
    print("Opcion invalida")
