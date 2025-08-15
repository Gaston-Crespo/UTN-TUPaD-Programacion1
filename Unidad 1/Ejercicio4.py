#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
# su perímetro.
import math
radio = float(input("Ingrese el radio del circulo para obtener el area y su perimetro "))
area = math.pi * radio**2
perimetro = 2 * math.pi * radio
print(f"El Area es: {area}")
print(f"El Perimetro es: {perimetro}")