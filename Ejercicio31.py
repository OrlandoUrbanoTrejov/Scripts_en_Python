"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  18-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: En la cafetería de Tesji hay una urna con pelotas de colores. verde, roja y amarilla. Cada una aplica un desucento diferente en el total de tu compra. La pelota verde ofrece un 10% de descuento, la amarilla un 5% y la roja un 15%. Con base a esos datos, imprime el monto final a pagar, ya con el descuento """ 

print("-----CAFETERIA TESJI-----")
print("1) Pelota Verde")
print("2) Pelota Roja")
print("3) Pelota Amarilla")

Pelota = int(input("Elige una opcion: "))

if Pelota == 1:
    print("Descuento 10%")
    Compra = float(input("Total de tu compra: "))
    Resultado = Compra - (Compra * 0.10)
    print(f"Monto total: ${Resultado:.2f}")
elif Pelota == 2:
    print("Descuento 5%")
    Compra = float(input("Total de tu compra: "))
    Resultado = Compra - (Compra * 0.05)
    print(f"Monto total: ${Resultado:.2f}")
elif Pelota == 3:
    print("Descuento 15%")
    Compra = float(input("Total de tu compra: "))
    Resultado = Compra - (Compra * 0.15)
    print(f"Monto total: ${Resultado:.2f}")
else:
    print("Opcion no valida")

