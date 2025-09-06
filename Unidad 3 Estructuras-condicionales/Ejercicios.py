#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
    #deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad "))
if edad>=18:
    print("Es mayor de edad")



#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
    #mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
    #mensaje “Desaprobado”.

nota = int(input("Ingrese la nota obtenida "))
if nota>=6:
    print("Aprobado")
else:
    print("Desaprobado")



#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
    #número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
    #contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
    #operador de módulo (%) en Python para evaluar si un número es par o impar.

numero_usuario=int(input("Ingrese un numero "))
if numero_usuario % 2 == 0:
    print ("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")



#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
    #siguientes categorías pertenece: 
    #● Niño/a: menor de 12 años. 
    #● Adolescente: mayor o igual que 12 años y menor que 18 años. 
    #● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
    #● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad <= 18:
    print("Adolescente")
elif edad >= 18 and edad <30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")



#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
    #(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
    #pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
    #pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
    #de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
    #como una lista o un string.

contraseña = input("Ingrese una contraseña que tenga entre 8 a 14 caracteres ")
if 8 <= len(contraseña) <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")



#6)escribir un programa que tome la lista 
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media > mediana:
    sesgo = "Sesgo positivo"
elif media < mediana:
    sesgo = "Sesgo negativo"
else:
    sesgo = "No hay sesgo"

print("Numeros aleatorios", numeros_aleatorios)
print(f"Moda: {moda}")
print(f"Medina: {mediana}")
print(f"Media: {media}") 
print(f"Resultado : {sesgo}")     



#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
#pantalla. 
frase = input("Ingrese una frase o palabra ").lower()
frase_final = frase.strip()
ultima_letra = frase_final[-1]
vocales = "aeiou"
if ultima_letra in vocales:
    frase_final += "!"
    print(frase_final)
else:
    print(frase_final)



#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre = input("Ingrese su nombre ")
print ("Ingrese la opcion de deseada\n 1. Si quiere su nombre en mayuscula \n 2. Si quiere su nombre en minuscula \n 3. Si quiere su nombre con la primera letra en mayuscula")
opcion = int(input())
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opcion no valida")



#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 
terremoto = float(input("Ingrese la magnitud de un terremeto para saber que en escala de Richter se encuentra "))
if terremoto < 3:
    print("Muy leve (imperceptible)\U0001F60C")
elif 3 <= terremoto < 4:
    print ("Leve (ligeramente perceptible)\U0001F440" )
elif 4 <= terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)\U0001F62C")
elif 5 <= terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles)\U0001F630")
elif 6 <= terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos)\U0001F631")
elif terremoto >= 7:
    print("Extremo (puede causar graves daños a gran escala) \u2620")



#10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio = input("En que hemisferio te encuentras? Norte o Sur? ").title()
mes = int(input("En que mes?"))
dia = int(input("En que dia?"))
estacion = ""

if hemisferio == "Sur":
    if (dia >= 21 and mes == 12) or (mes == 1) or (mes == 2) or (mes == 3 and dia <=20):
        estacion = ("Verano \u2600\uFE0F")
    elif (dia >=21 and mes ==3) or (mes == 4) or (mes == 5) or (mes == 6 and dia <=20):
        estacion = ("Otoño \U0001F342")
    elif (dia >=21 and mes == 6) or (mes == 7) or (mes ==8) or (mes == 9 and dia <=20):
        estacion = ("Invierno:\u2744\uFE0F")
    else:
        estacion = ("Primavera \U0001F331")

elif hemisferio == "Norte":
    if (dia >=21 and mes == 12) or (mes == 1) or (mes == 2) or (mes == 3 and dia <=20):
        estacion = ("Invierno:\u2744\uFE0F")
    elif (dia >=21 and mes == 3) or (mes == 4) or (mes == 5) or (mes == 6 and dia <=20):
        estacion = ("Primavera \U0001F331")
    elif (dia >=21 and mes == 6) or (mes == 7) or (mes == 8) or (mes == 9 and dia <=20):
        estacion = ("Verano \u2600\uFE0F")
    else:
        estacion = ("Otoño \U0001F342")

if estacion:
   print(f"Estas en {estacion}")
