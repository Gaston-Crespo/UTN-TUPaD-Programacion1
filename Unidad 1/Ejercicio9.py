#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# Temp Fahren = 9/5 * temp celsius + 32
print("A continuacion haremos un cambio de unidad de medida de temperatura de Celsius a Fahrenheit")
celsius = float(input("Ingrese la temperatura celsius deseada: "))
fahrenheit = 9/5 * celsius + 32
print(f"El equivalente a {celsius} grados Celsius es {fahrenheit} grados Fharenheit")