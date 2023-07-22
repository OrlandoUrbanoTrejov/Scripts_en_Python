"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  17-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Un vendedor de vestidos ofrece 3 diferentes tallas, con diferentes precios, la grande con un precio
de $500 por vestido, la mediana con un costo de $400 y la chica de $300. Selecciona la talla a comprar
y solicita el número de vestidos que desee, Posteriormente, calculo el monto final"""

print("----VESTIDOS----")
print("1) Grande $500")
print("2) Mediana $400")
print("3) Chica $300")

Vestido = int(input("Elige la marca que deseas comprar (1-3): "))
if Vestido == 1:
    Cantidad = int(input("Numero de vestidos que deseas comprar: "))
    Total = Cantidad  * 500
elif Vestido == 2:
    Cantidad = int(input("Numero de vestidos que deseas comprar: "))  
    Total = Cantidad  * 400
elif Vestido == 3:
    Cantidad = int(input("Numero de vestidos que deseas comprar: "))
    Total = Cantidad  * 300
else:
    print("Opcion no valida")

print("Monto total de la venta: $",Total)


