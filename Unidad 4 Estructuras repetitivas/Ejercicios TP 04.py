#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

for i in range (101):
    print(i)


print("--------------------------------------------------------------------------------")


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.

numero = int(input("Ingrese un numero entero: "))

if numero == 0:
    cantidad_digitos = 1
else:
    cantidad_digitos = 0
    while numero >0:
        numero = numero // 10
        cantidad_digitos +=1

print("La cantidad de digitos en su numero es de", cantidad_digitos)


print("--------------------------------------------------------------------------------")


#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores. 

#Se le pide al usuario que ingrese dos numeros y asignamos valores a las variables 
print("Ingrese dos numeros enteros para saber la suma entre sus numeros: ")
num1 = int(input("1: "))
num2 = int(input("2: "))
suma = 0

# Aseguramos que num1 sea menor que num2 para que pueda suceder la suma entre sus numeros, sino siempre daria 0 de resultado
if num1 > num2:
    num1, num2 = num2, num1

# Se suman los números entre num1 y num2, excluyendo los extremos
for i in range (num1 +1, num2):
    suma += i 

#resultado de la suma entre las partes comprendidas
print("La suma de los numeros comprendidos entre ", num1 ,"y", num2 ,"es de", suma  )


print("--------------------------------------------------------------------------------")


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0. 

#Se le pide al usuario que ingrese los numeros y se asignan valores a las variables 
print("Ingrese la cantidad de numeros enteros que desee para saber la suma entre ellos. Ingrese 0 cuando decida parar")
suma = 0
corte = 0

#ingreso un contador para que aparezca al lado cada vez que se le pide un numero al usuario
contador = 1
num = int(input(f"Numero {contador}: " ))

#inicio con el bucle 
while num!= corte: 
    suma += num
    contador += 1
    num = int(input(f"Número {contador}: "))

#Se imprime resultado final     
print("La suma total de sus numeros es: ", suma )


print("--------------------------------------------------------------------------------")


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

#Se importa la libreria para generar un numero aleatorio
import random 

#Se da valor a las variables
num_aleatorio = random.randint(0,9)
intentos = 0
num_usuario = -1

#Iniciamos el juego dandole los parametros al usuario y seguido a eso, empezamos con el bucle 
print("Adivina un numero entre 0 y 9")


while num_usuario != num_aleatorio:
    num_usuario = int(input("Numero elegido: "))
    
    #Validamos el rango por si el usuario ingresa un numero diferente a lo establecido
    if num_usuario <0 or num_usuario >9:
        print("Por favor elija numeros entre 0 y 9")
        #Usamos el comando continue para que siga con el bucle 
        continue
    intentos += 1


#Finalizamos codigo diciendo cual era el numero aleatorio y en cuando intentos lo logro 
print("Felicitaciones! el numero era", num_aleatorio,",y lo logaste en", intentos," intentos")


print("--------------------------------------------------------------------------------")


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente.

#se empieza desde el 100 hasta el -1 para que tambien contenga al 0 y se le decrementa en -2 
#para asegurar que los numeros impresos sean pares
for i in range (100,-1,-2):
    print(i)


print("--------------------------------------------------------------------------------")


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.

#le pedimos al usuario que ingrese un numero y se lo asignamos a esa variable
num_1 = int(input("Por favor ingrese un numero: "))
#asignamos variables para la suma
suma = 0

#iniciamos bucle for range para recorrer los numero entre el 0 y el numero del usuario
for i in range (num_1 + 1):
    suma += i
print("La suma de los numeros comprendidos entre el 0 y su numero elegido es",suma)


print("--------------------------------------------------------------------------------")


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

#Establecemos un limite de numeros para luego poder usar ese limite en un bucle
limite = 100

#Iniciamos variables de contadores en 0 para :
numeros_positivos = 0
numeros_negativos = 0
numeros_pares = 0
numeros_impares = 0

#iniciamos el bucle for con el limite
for i in range (limite):
    #Le pedimos al usuario que ingrese un numero y le indicamos en que posicion se encuentra dentro del limite
    num = int(input(f"Por favor, ingrese el numero {i+1} de {limite}: "))

    #verificamos si el numero ingresado es par o no y se lo sumamos a su respectivo contador
    if num % 2 == 0:
        numeros_pares +=1 
    else:
        numeros_impares +=1
    
    #verificamos si el numero es negativo o positivo 
    if num > 0:
        numeros_positivos +=1
    else:
        numeros_negativos +=1

#imprimimos resultados para el usuario
print("Para los numeros ingresados, estos son sus resultados:")
print("Usted ingreso un total de:", limite,"numeros, entre los cuales")
print(numeros_pares,"Son numeros pares")
print(numeros_impares, "Son numeros impares")
print(numeros_positivos, "Son numeros positivos")
print(numeros_negativos, "Son numeros negativos")


print("--------------------------------------------------------------------------------")


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor). 

#Establecemos limite de numeros para usarlo luego en el bucle e iniciamos variable suma e iterador en 0
limite = 2
suma = 0
iterador = 0

#Iniciamos bucle while 
while iterador < limite:
    num = int (input(f"Ingrese el numero {iterador+1} de {limite}: "))
    suma += num
    iterador += 1
#calculamos la media
media = suma / limite
print(f"La media o premedio entre sus numeros dados es {media}")


print("--------------------------------------------------------------------------------")


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

#Le pedimos al usuario que ingrese un numero 
num = int(input("Ingrese un numero para invertir el orden del mismo: "))

centenas = num // 100
decenas = (num // 10) % 10
unidades = num % 10

#Ordenamos el numero invertido
num_invertido = unidades * 100 + decenas * 10 + centenas

print(f"El numero invertido de su numero es {num_invertido}")
