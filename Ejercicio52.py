"""Autor:  Orlando Urbano Trejo (Lando)
   Fecha:  28-07-2023
   Correo: urbanoorlando79@gmail.com

Ejercicio: Regresa el restante de la cadena a partir de la primera aparicion del caracter indicado """
  
Abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Corte = input("Letra donde quieres realizar el corte: ")

print("Nueva Cadena")
# Con rindex obtenemos el ultimo corte en la letra que se a indicado
Nueva_Cadena = Abecedario[Abecedario.rindex(Corte):]
print(Nueva_Cadena)



