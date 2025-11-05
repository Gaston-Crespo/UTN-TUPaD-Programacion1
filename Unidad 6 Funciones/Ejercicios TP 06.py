# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: 
# “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    return print("Hola Mundo!")

imprimir_hola_mundo()


print("---------------------------------")


# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un 
# saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: 
# “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario

def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")

saludar_usuario("Lucas")


print("---------------------------------")


# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro
# parámetros e imprima: “Soy[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu ciudad de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)


print("---------------------------------")


# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva 
# el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva
# el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingresa el radio del circulo: "))
    
if radio <= 0:
    print("Error: El radio debe ser un numero positivo.")
else:
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"Area: {area:.2f}")
    print(f"Perimetro: {perimetro:.2f}")


    print("---------------------------------")


 # 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro
 # y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado
 # usando esta función

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = float(input("Ingresa la cantidad de segundos: "))
    
if segundos < 0:
    print("Error: La cantidad de segundos no puede ser negativo.")
else:
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas")


print("---------------------------------")


# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima
# la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} × {i} = {resultado}")

numero = int(input("Ingresa un numero para generar su tabla de multiplicar: "))
tabla_multiplicar(numero)


print("---------------------------------")


# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva
# una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por 0"
    
    return suma, resta, multiplicacion, division

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

resultados = operaciones_basicas(num1, num2)

print(f"Resultados para {num1} y {num2}")
print(f"Suma: {num1} + {num2} = {resultados[0]}")
print(f"Resta: {num1} - {num2} = {resultados[1]}")
print(f"Multiplicacion: {num1} × {num2} = {resultados[2]}")
print(f"Division: {num1} ÷ {num2} = {resultados[3]}")


print("---------------------------------")


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros,
# y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
# para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingresa tu peso en kgs: "))
altura = float(input("Ingresa tu altura en metros: "))

if peso <= 0 or altura <= 0:
    print("Error: El peso y la altura deben ser valores positivos.")
else:
    imc = calcular_imc(peso, altura)
    print(f"Tu indice de Masa Corporal (IMC) es: {imc:.2f}")


    print("---------------------------------")


# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y
# devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el 
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
     return (celsius * 9/5) + 32

celsius = float(input("Ingresa la temperatura en grados Celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")


print("---------------------------------")


# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva
# el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(num1, num2, num3):
    return (num1 + num2 + num3) / 3

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
num3 = float(input("Ingresa el tercer numero: "))

promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}") 
