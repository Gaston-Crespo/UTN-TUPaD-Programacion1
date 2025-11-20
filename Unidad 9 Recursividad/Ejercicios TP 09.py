# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario 

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

numero = int(input("Ingrese un numero entero positivo: "))
    
if numero < 1:
    print("Por favor, ingrese un numero positivo.")
else:
    print(f"\nFactoriales de los numeros del 1 al {numero}:")
    print("-" * 38)
    
    for i in range(1, numero + 1):
        resultado = factorial(i)
        print(f"{i}! = {resultado}")



# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique. 

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

num_pos = int(input("Ingrese la posicion deseada hasta la cual mostrar la serie de Fibonacci: "))
    
if num_pos < 0:
    print("Por favor, ingrese un numero positivo.")
else:
    print(f"\nSerie de Fibonacci hasta la posicion {num_pos}:")
    print("-" * 40)
    
    # Mostrar la serie completa
    for i in range(num_pos + 1):
        valor = fibonacci(i)
        print(f"Posicion {i}: {valor}")



# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general. 

def potencia(n, m):
    if m == 0:
        return 1
    if m == 1:
        return n
    return n * potencia(n, m - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

if exponente < 0:
    print("Opcion invalida. Esta funcion solo trabaja con exponentes positivos.")
else:
    resultado = potencia(base, exponente)
    print(f"Resultado: {base}^{exponente} = {resultado}")
    


# 4) Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto. 

def decimal_a_binario(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return decimal_a_binario(num // 2) + str(num % 2)

numero = int(input("Ingrese un numero entero positivo: "))
if numero < 0:
    print("Opcion invalida. El numero debe ser positivo.")
else:
    binario = decimal_a_binario(numero)
    print(f"\nEL numero {numero} en decimal se traduce a {binario} en binario")



# 5.Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
# lo es. 
#      Requisitos: 
# La solución debe ser recursiva. 
# No se debe usar [::-1] ni la función reversed(). 

def es_palindromo(palabra):
    # Si la palabra tiene 0 o 1 letra, es palindromo por defecto 
    if len(palabra) <= 1:
        return True
    # En caso contrario comparamos el primer caracter con el ultimo 
    elif palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False
    
palabra = input("Ingrese una palabra: ").lower()
if es_palindromo(palabra):
    print(f"'{palabra}' es un palindromo")
else:
    print(f"'{palabra}' no es un palindromo")



# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
# número entero positivo y devuelva la suma de todos sus dígitos. 
#      Restricciones: 
# No se puede convertir el número a string. 
# Usá operaciones matemáticas (%, //) y recursión. 
# Ejemplos: 
# suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
# suma_digitos(9)      → 9 
# suma_digitos(305)    → 8   (3 + 0 + 5) 

def suma_digitos(n):
    # <10 , porque si es menos de ese valor, solo hay que devolver dicho valor
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingrese un numero entero positivo: "))        
if numero < 0:
    print("Opcion invalida. El numero debe ser positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los digitos de {numero} es: {resultado}")



# Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
# último nivel con un solo bloque. 
#  
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
# pirámide. 
#  
#       Ejemplos: 
# contar_bloques(1)   → 1         (1) 
# contar_bloques(2)   → 3         (2 + 1) 
# contar_bloques(4)   → 10        (4 + 3 + 2 + 1)

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

base = int(input("Ingrese el numero de bloques en la base: "))
        
if base < 1:
    print("Opcion invalida. El numero debe ser mayor o igual a 1.")
else:
    total_bloques = contar_bloques(base)
    print(f"Para una piramide con {base} bloques en la base:")
    print(f"Se necesitan un total de {total_bloques} bloques para completarla")
    secuencia = ""
    for i in range(base, 0, -1):
        secuencia += str(i)
        if i != 1:
            secuencia += " + "
    print(f"Con una secuencia de: {secuencia} = {total_bloques}")


# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
# aparece ese dígito dentro del número. 
#       Ejemplos: 
# contar_digito(12233421, 2)   → 3   
# contar_digito(5555, 5)       → 4   
# contar_digito(123456, 7)     → 0   

def contar_digito(numero, digito):
    # Si queda un solo dígito, lo comparamos directamente
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        ultimo_digito = numero % 10
        resto_numero = numero // 10
        if ultimo_digito == digito:
            return 1 + contar_digito(resto_numero, digito)
        else:
            return contar_digito(resto_numero, digito)

numero = int(input("Ingrese un numero entero positivo: "))
digito = int(input("Ingrese el digito a buscar (0-9): "))

if numero < 0:
    print("Opcion invalida. El numero debe ser positivo.")
elif digito < 0 or digito > 9:
    print("Opcion invalida. El digito debe estar entre 0 y 9.")
else:
    resultado = contar_digito(numero, digito)
    print(f"El digito {digito} aparece {resultado} veces en el numero {numero}")