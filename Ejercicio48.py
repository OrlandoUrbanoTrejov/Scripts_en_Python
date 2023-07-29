"""Autor:  Orlando Urbano Trejo (Lando) 
   Fecha:  28-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Una compania de refrescos comercializa tres productos: de cola, de naranja y de limon. Se desea realizar un programa que calcule las ventas realizadas de cada producto. Para ello, se leera la cantidad vendida (maximo 5000000) y el precio en euros de cada producto y se mostrara un informe de ventas como el que sigue: """

Ventas_Cola = float(input("Ingresa la cantidad de ventas de cola: "))
Precio_Cola = float(input("Precio del producto: "))
Total_Cola = Ventas_Cola * Precio_Cola

Ventas_Naranja = float(input("Ingresa la cantidad de ventas de naranja: "))
Precio_Naranja = float(input("Precio del producto: "))
Total_Naranja = Ventas_Naranja * Precio_Naranja

Ventas_Limon = float(input("Ingresa la cantidad de ventas de limón: "))
Precio_Limon = float(input("Precio del producto: "))
Total_Limon = Ventas_Limon * Precio_Limon

Total_Final = Total_Cola + Total_Naranja + Total_Limon

print("Producto   Ventas    Precio Total")
print("--------------------------------------")
print(f"Cola       {Ventas_Cola}\t      {Precio_Cola}\t  {Total_Cola}")
print(f"Naranja    {Ventas_Naranja}\t      {Precio_Naranja}\t  {Total_Naranja}")
print(f"Limon      {Ventas_Limon}\t      {Precio_Limon}\t  {Total_Limon}")
print(f"                    TOTAL         {Total_Final}")



