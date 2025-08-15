# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 
num1 = int(input("Ingrese su primer numero: "))
num2 = int(input("Ingrese su segundo numero: "))
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
cociente = num1 / num2
print(f"La suma de sus numero es: {suma}")
print(f"La resta de sus numero es: {resta}")
print(f"La multiplicacion/producto de sus numeros es: {producto}")
print(f"La division/cociente de sus numero es {cociente}")
