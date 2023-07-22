"""Autor: Orlando Urbano Trejo (Lando) 
   Fecha: 13-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: En un hospital existen 3 áreas: Urgencias, Pediatría y Traumatología. 
 * El presupuesto anual del hospital se reparte de la siguiente manera: 
 * Pediatría 42% y Traumatología 21% """

Presupuesto = int(input("Presupuesto anual: "))

Urgencias = Presupuesto * 0.37
Pediatria = Presupuesto * 0.42
Traumatologia = Presupuesto * 0.21

print("Presupuesto Urgencias: ${:.2f}".format(Urgencias))
print("Presupuesto Pediatria: ${:.2f}".format(Pediatria))
print("Presupuesto Traumatologia: ${:.2f}".format(Traumatologia))


