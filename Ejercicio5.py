"""Autor: Orlando Urbano Trejo (Lando) 
   Fecha: 13-07-2023
   Correo: urbanoorlando79@gmail.com

 Ejercicio: Un vendedor a realizado N ventas y desea saber cuantas fueron por 10,000 o menos,cuantas fueron por mas de 10,000 pero por menos de 20,000 y cuanto fue el monto de las ventas de cada una, y el monto global, realice el algoritmo para determinar los totales"""
def calcular_totales(ventas):
    total_10000_o_menos = 0
    total_10000_a_20000 = 0
    total_global = 0   

   for venta in ventas:
        if venta <= 10000:
            total_10000_o_menos += venta
        elif venta > 10000 and venta < 20000:
            total_10000_a_20000 += venta

        total_global += venta

    return total_10000_o_menos, total_10000_a_20000, total_global


# Obtener la cantidad de ventas y los montos
n = int(input("Ingrese la cantidad de ventas: "))
ventas = []

for i in range(n):
    venta = float(input(f"Ingrese el monto de la venta {i+1}: "))
    ventas.append(venta)

# Calcular los totales
total_10000_o_menos, total_10000_a_20000, total_global = calcular_totales(ventas)

# Imprimir los resultados
print(f"Total de ventas de 10,000 o menos: {total_10000_o_menos}")
print(f"Total de ventas de más de 10,000 pero menos de 20,000: {total_10000_a_20000}")
print(f"Monto total de todas las ventas: {total_global}")

