#1) Crear una lista con las notas de 10 estudiantes. 
#• Mostrar la lista completa. 
#• Calcular y mostrar el promedio. 
#• Indicar la nota más alta y la más baja. 

#creaamos lista con notas e iniciamos variable suma y contador en 0
lista_notas = [6, 7.5, 8, 9, 10, 5, 4, 8.5, 2, 9.5]
suma = 0
contador = 0
#imprimimos las notas en lista (usamos la variable nota como iterador )
print("Listado de notas de estudiantes")
for nota in (lista_notas):
    print (nota)

#sumamos las notas y dividimos por la cantidad de estudiantes
for nota in (lista_notas):
    suma += nota 
    contador +=1

#calculammos el promedio 
promedio = suma / contador
print (f"El promedio de notas de los estudiantes es {promedio}")

#iniciamos valores para la nota mas alta y la mas baja tomando el primer elemento de la lista
nota_mas_alta = lista_notas[0]
nota_mas_baja = lista_notas[0]

#recorremos la lista con bucle for
for nota in (lista_notas):
    #verificamos cual es la nota mas alta con if y le damos el nuevo valor a la variable
    if nota > nota_mas_alta:
        nota_mas_alta = nota
    if nota < nota_mas_baja:
        nota_mas_baja = nota

#Damos el valor de la nota mas alta y la mas baja
print(f"La nota mas alta fue:{nota_mas_alta}")
print(f"La nota mas baja fue:{nota_mas_baja}")


print("--------------------------------------------------------------------------------")


#2) Pedir al usuario que cargue 5 productos en una lista. 
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

#Iniciammos una variable vacia para la lista nueva 
Lista_productos = []

#iniciamos bucle for para pedirle al usuario los productos
for i in range(5):
    productos_usuario = input (f"Por favor, ingrese el producto {i+1} de 5: ")
    #agregamos los productos del usuario a la lista productos
    Lista_productos.append (productos_usuario)

#ordenamos la lista de manera alfabetica con funcion sorted()
productos_ordenados = sorted(Lista_productos)

#creamos bucle para listar los productos ordenados
print("Lista de productos ordenados alfabeticamente")
for i in (productos_ordenados):
    print(i)

#iniciamos bucle while en caso que el producto no se encuentre en la lista o el usuario se haya equivocado en el nombre
while True:
    #iniciamoms otra variable en la que le preguntamos al usuario si quiere eliminar un producto y cual
    producto_para_eliminar = input("Si quiere eliminar algun producto, mencione cual: ")
    #validamos si el producto mencionado esta en la lista 
    if producto_para_eliminar in Lista_productos:
        #si el proucto esta en la lista, lo eliminamos
        Lista_productos.remove(producto_para_eliminar)
        print(f"El producto {producto_para_eliminar} fue eliminado de la lista de productos")
        break #para salir del codigo
    else:
        print(f"El producto {producto_para_eliminar} no se encuenta en la lista de productos")
        #Commo el producto no esta en la lista, le preguntamos si quiere continuar
        #utilizamos .strip()para eliminar espacios vacios y .lower() para llevar el strg a minuscula
        continuar = input("Desea continuar y eliminar otro producto si/no: ").strip().lower() 
        if continuar != "si":
            break #si la respuesta del usuario es no, cortamos el codigo y seguimos con la lista actualizada

#Lista actualizada
print("Lista de productos final y actualizada")
for i in (Lista_productos):
    print(i)


print("--------------------------------------------------------------------------------")


#3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
#• Crear una lista con los pares y otra con los impares. 
#• Mostrar cuántos números tiene cada lista. 

#importamos random de la biblioteca, para que nos genere numeros al azar
import random
#creamos la lista con los parametros deseados
lista_azar = [random.randint(1,100) for i in range(15)]

#creamos listas para numero pares y para impares
numeros_pares = []
numeros_impares = []

#recorremos la lista de numeros al azar con bucle for y se lo sumamos a cada lista (pares/impares)
for i in (lista_azar):
    if i % 2 == 0:
        numeros_pares.append (i)
    else:
        numeros_impares.append (i)

#Mostramos los numeros de la lista al azar
print("Para los numeros")
print(lista_azar)
print("------------------------------------------------------")
#Mostramos cantidad de numeros por lista
print("La cantidad de numeros por lista es:")
print(f"Para la lista general son {len(lista_azar)} numeros")
print(f"En la lista de numeros pares, contamos con {len(numeros_pares)} numeros")
print(f"Y para la lista de numeros impares, tenemos un total de {len(numeros_impares)} numeros")


print("--------------------------------------------------------------------------------")


#4) Dada una lista con valores repetidos: 
# datos =[1, 3, 5, 3, 7, 1, 9, 5, 3]
#• Crear una nueva lista sin elementos repetidos. 
#• Mostrar el resultado.

#datos repetidos
print("Lista con elementos repetidos")
datos =[1, 3, 5, 3, 7, 1, 9, 5, 3]
print(datos)

#nueva lista
nueva_lista = []

for i in (datos):
    if i not in nueva_lista:
        nueva_lista.append (i)
print("-----------------------------------------")
print("Lista actuzalidad sin elementos repetidos")
print(nueva_lista)


print("--------------------------------------------------------------------------------")


#5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
#• Mostrar la lista final actualizada.

#Creamos lista con nombre de 8 estudiantes
lista_estudiantes = ["renato", "luis", "cristobal", "carla", "marina", "gaston", "natalia", "fabian"]
print("Esta es la lista original de estudiantes")
for i in (lista_estudiantes):
    print(i)


#Iniciammos bucle while por si el usuario quiere elminar o agragar un nombre
while True:
    #con la funcion strip eliminammos espacios en blancos y con lower convertimos la entrada en minuscula 
    continuar = input("Desea eliminar o agragar algun nombre de la lista? si/no: ").strip().lower()
    if continuar == "si":
        #iniciamos una variable para guardar la decision del usuario
        decision = input("Desea eliminar o agregar un estudiante?: ").strip().lower()
        if decision == "agregar":
            #igualammos la decision del usuario a una nueva variable
            agregar = input("Mencione el nommbre del estudiante a agregar: ").strip().lower()
            #agregamos el nuevo nombre a la lista
            lista_estudiantes.append (agregar)
            print("El estudiante ha sido agragado")
            
        elif decision =="eliminar":
            #iniciamos otro bucle while y seguimmos pidiendo el nombre hasta que sea valido
            while True:
                #iniciamos nueva variable con decision del usuario
                eliminar =input("Ingrese el nombre del estudiante a eliminar: ").strip().lower()
                #igualamos la decision de usuario a nueva variable
                if eliminar in(lista_estudiantes):
                    #elminamos el nombre de la lista
                    lista_estudiantes.remove(eliminar)
                    print("El estudiante ha sido eliminado")
                    break #cortamos el bucle para que no siga funcionando 
                else:
                    #si el estudiante no se encuenta en la lista, le preguntamos nuevamente al ususaro si quire continuar y repetimos el bucle
                    continuar = input("El estudiante no se encuentra en el listado, desea intentar nuevamente? si/no: ").strip().lower()
                    #en caso que el usuario no quiera seguir, cortamos el bucle con un break mas abajo 
                    if continuar!="si":
                        break

    elif continuar == "no":
        break #corte de bucle
    else:
        ("Opcion no valida, responda por 'si' o 'no' ")
print("--------------------------------")
#Mostramos la lista actualizada 
print("Lista actualizada de estudiantes")
for i in (lista_estudiantes):
    print(i)
print()
print("Gracias vuelva prontos")


print("--------------------------------------------------------------------------------")


#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
#último pasa a ser el primero).

#inciamos lista original
#la hice con numeros consecutivos para que sea mas facil de leer
lista_original = [1, 2, 3, 4, 5, 6, 7]

#imprimimos por pantalla la lista orignal de los numero para luego compararla con la actualizada
print("Lista original de numeros")

#recorremmos la lista con bucle for e imprimimos la lista
for i in (lista_original):
    print(i) 

#inicimoa nueva variable para obtener el ultimo numero y movemos hacia la derecha
ultimo_numero = lista_original[-1]
#recorremos la lista de atras hacia adelante con bucle for
for i in range(len(lista_original)-1, 0, -1):
    #movemos cada elemento hacia le derecha
    lista_original[i] = lista_original[i-1]
#colocamos el ultimo elemento(numero) en la primer posicion,asignando al primer elemento (0) de la lista_original
# a la variable ultimo_numero
lista_original[0] = ultimo_numero

#mostramos la lista con la correccion hecha con bucle for
print("-----------------------------------------")
print("Lista final con elementos movidos una posicion hacia la izquieda")
for i in (lista_original):
    print(i)


print("--------------------------------------------------------------------------------")


#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
#semana. 
#• Calcula r el promedio de las mínimas y el de las máximas. 
#• Mostrar en qué día se registró la mayor amplitud térmica. 

#Primero hacemos una lista con los nombre de la semana
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

#Ahora creamos lista con temperaturas
temperaturas = [
    [23, 26],
    [21, 25],
    [19, 27],
    [15, 28],
    [20, 24],
    [18, 23],
    [22, 25]
]

#ahora creamos la matriz con las temperaturas y sus dias y la deajamos vacia para luego agregarle los valores corresponientes
matriz_temperatura = []
#recorremos la lista dias con bucle for i in range len para que recoora el largo de la lista 
for i in range (len(dias)):
    #con funcion append le agregamos a lista matriz_temperatira la lista dias y tambien lista temperatura,
    #citando cada lista y su elemento correspondiente
     matriz_temperatura.append([dias[i], temperaturas[i][0], temperaturas[i][1]]) 
#imprimimos por pantalla la matriz de las temperaturas  con sus respectivos dias 
print("Temperatura semanal")
#Aca hice una especie de encabezado, ya que luego de probar, no me gustaba como aparecia sin sus nombre respectivos
print("Dia, Maxima, Minima")
for i in (matriz_temperatura):
    #imprimimos las filas, llamando a cada elemento en su lugar
    print(i[0], i[1], i[2])
    
#iniciamos variables para minimas y maximas
temp_minima = 0
temp_maxima = 0
#tambien iniciamos las variables para determinar la maxima amplitud termica y que dia fue
max_amplitud_termica = 0
dia_maxima_amplitud = "" #La iniciamos con un string vacio para luego otorgarle un dia segun max_amplitud_termica

#recorremos la lista temperatura con bule for
for i in range (len(temperaturas)):
     #sumamos la minima(ubicada en posicion 0) y la maxima(posiscion 1) a cada variable
     temp_minima += temperaturas[i][0]
     temp_maxima += temperaturas[i][1]
    
     #teniendo los parametros de  las maximas y minimas, calculamos la amplitud con nueva variable(restando sus elementos)
     amplitud = temperaturas[i][1] - temperaturas[i][0]
     
     #verificamos cual es mayor con if
     if amplitud > max_amplitud_termica:
          max_amplitud_termica = amplitud
          dia_maxima_amplitud = dias[i] #accedemos a la lista de días usando el mismo índice i que se está utilizando en el bucle for



     
#Calculamos el promedio de ambas con funcion len, para tomar el largo de la lista
promedio_temp_min = temp_minima//len(temperaturas)
promedio_temp_max = temp_maxima//len(temperaturas)
print("-------------------------------------")
#imprimimos resultado por pantalla
print(f"El promedio de las temperaturas bajas fue de {promedio_temp_min}° centigrados")
print(f"EL promedio de las temperaturas altas fue de {promedio_temp_max}° centigrados")
print("-------------------------------------")
print(f"El dia con mayor amplituid termica fue el {dia_maxima_amplitud} con una amplitud de {max_amplitud_termica}° centigrados ")


print("--------------------------------------------------------------------------------")


#8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
#• Mostrar el promedio de cada estudiante. 
#• Mostrar el promedio de cada materia. 

#creamos lista de notas estudiantes
notas_estudiantes = [
    [8, 7, 10],
    [9, 4, 7],
    [5, 8, 6],
    [10, 7, 6],
    [7, 7, 7]
]

#Creamos nueva listas para promedios estudiantes y otra para las materias
promedio_estudiantes = []
suma_materias = [0, 0, 0]
#recorremos la lista con bucle for con indices
for i in range(len(notas_estudiantes)):
    #iniciamos una variable nueva para otorgarle los valores de la lista notas_estudiantes
    total = 0
    #seguimos recorriendo el bucle pero ahora con el indice j para leer el subindice de i(cada elementos de la lista)
    for j in range (len(notas_estudiantes[i])):
        #sumammos las notas en la variable total
        total += notas_estudiantes[i][j] #accedemos a las notas por su indice
        suma_materias[j]+=notas_estudiantes[i][j] 
    #fuera del segundo bucle, sacamos el promedio dividiendo el total porque el indice i (que seria la cantidad de alumnos en este caso)
    promedio = total/len(notas_estudiantes[i])
    #le agregamos el promedio a la lista promedio_estudiantes
    promedio_estudiantes.append(promedio)

#iniciamos lista nueva para promedio de materias
promedio_materias = []
for suma in (suma_materias):
    #dividimos la suma por la cantidad de estudiantes
    promedio = suma/len(notas_estudiantes)
    #agregamos el promedio de las materias a la lista 
    promedio_materias.append(promedio)


#imprimimos los promedios de cada estudiante 
for i in range(len(promedio_estudiantes)):
    print(f"El promedio del estudiante {i+1} fue de {promedio_estudiantes[i]:.2f}") 
    # estuve buscando una funcion que me ayude a recortar los numeros decimales, ya que el resultado 
    # me daba con varios y encontre esta ( :.2f ), espero que este bien que la haya utilizado 
print("-------------------------------------------")
#imprimimos promedio de materias 
for k in range(len(promedio_materias)):
    print(f"El promedio de la materia {k+1} es de {promedio_materias[k]:.2f}")


print("--------------------------------------------------------------------------------")


#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
#• Inicializarlo con guiones "-" representando casillas vacías. 
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
#• Mostrar el tablero después de cada jugada.


# Inicio de tablero 3x3 con guiones para representar casillas vacías
tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    # Mostramos el tablero con bucle for 
    for fila in tablero:
        # Imprimimos resultado con .join para mostrar cada fila del tablero de manera más legible
        print(" ".join(fila))
    print()  # Línea en blanco para mejor legibilidad

def ganador(tablero):
    # Con bucle for comprobamos en filas, columnas y diagonales 
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != "-":
            return tablero[i][0]  # Definimos ganador en fila
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != "-":
            return tablero[0][i]  # Definimos ganador en columna
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != "-":
        return tablero[0][0]  # Definimos ganador en diagonal 1
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != "-":
        return tablero[0][2]  # Definimos ganador en diagonal 2
    
    return None  # Cuando no hay ganador

# Bucle principal del juego
while True:
    # Reiniciar el tablero
    tablero = [["-" for _ in range(3)] for _ in range(3)]
    
    # Definimos jugadores
    jugadores = ["X", "O"]
    # Hacemos que empieza el jugador X
    turno = 0 

    # Con bucle for recorremos el tablero e iniciamos bucle de juego
    for _ in range(9):  # Máximo de 9 turnos
        mostrar_tablero(tablero)
        print(f"Turno del jugador {jugadores[turno]}")

        # Iniciamos bucle para validar entradas de fila
        while True:
            try:
                # Iniciamos variable para saber en qué fila quiere jugar
                fila = int(input("Ingrese la fila (0, 1, 2): "))
                if fila in [0, 1, 2]:
                    # Salimos del bucle si la fila es válida
                    break
                else:
                    print("Por favor, ingrese un número entre 0 y 2.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")

        # Iniciamos bucle para validar entrada de columna
        while True:
            try:
                columna = int(input("Ingrese la columna (0, 1, 2): "))
                if columna in [0, 1, 2]:
                    break
                else:
                    print("Por favor, ingrese un número entre 0 y 2.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")

        # Verificamos que la posición sea válida
        if tablero[fila][columna] == "-":
            # Colocamos la marca del jugador
            tablero[fila][columna] = jugadores[turno]
        else:
            print("Esta casilla está ocupada. Intente con otra.")
            # Volvemos al inicio del ciclo con continue
            continue

        # Verificamos si hay un ganador
        ganador_final = ganador(tablero)
        if ganador_final:
            mostrar_tablero(tablero)
            print(f"¡El jugador {ganador_final} ha ganado!")
            break

        # Alternamos entre jugadores 
        turno = 1 - turno

    else:
        mostrar_tablero(tablero)
        print("¡Es un empate!")

    # Preguntar si quieren jugar de nuevo
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_de_nuevo != 's':
        break  # Salir del bucle si no quieren jugar de nuevo


    print("--------------------------------------------------------------------------------")


 #10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
#• Mostrar el total vendido por cada producto. 
#• Mostrar el día con mayores ventas totales. 
#• Indicar cuál fue el producto más vendido en la semana. 

# Inicializar la matriz de ventas (4 productos x 7 días)
ventas = [
    50, 10, 8, 9, 12, 5, 9,   #Venta Producto 1
    15, 1, 6, 4, 25, 6, 2,    #Venta Producto 2
    7, 8, 12, 3, 5, 16, 5,    #Venta Producto 3
    9, 14, 11, 9, 8, 13, 7    #Venta Producto 4
]

#iniciamoms lista para saber el total vendido de cada producto
productos_vendidos = [0] * 4 

#Iniciamos un bucle for 
#primero para los productos
for producto in range(4):
    #segundo ahora para los dias 
    for dia in range(7):
       #iniciamos variable para calcular el indice
       indice = producto * 7 + dia 
       productos_vendidos[producto] += ventas[indice]

    #imprimimos el total vendido por cada producto
    print(f"Total vendido del producto {producto + 1}: {productos_vendidos[producto]}")

#Iniciamos una lista para calcular el dia con mayores ventas
ventas_dia = [0] * 7

for dia in range(7):
    for producto in range(4):
        indice = producto * 7 + dia
        ventas_dia[dia] += ventas[indice]

#imprimismo totales por dia
for dia in range(7):
    print(f"EL total vendido en el dia {dia + 1} es: {ventas_dia[dia]}")

dia_mas_ventas = ventas_dia.index(max(ventas_dia))
print(f"El dia con mayor ventas fue: Dia {dia_mas_ventas + 1}")

#iniciamos varibale para productos ams vendidos
productos_mas_vendidos = productos_vendidos.index(max(productos_vendidos))
print(f"El producto mas vendido fue: Producto {productos_mas_vendidos + 1}")


print("--------------------------------------------------------------------------------")
