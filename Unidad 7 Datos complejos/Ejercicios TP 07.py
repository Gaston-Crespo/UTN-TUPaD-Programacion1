# 1. Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
# 1450} 
# Añadir las siguientes frutas con sus respectivos precios: 
# ● Naranja = 1200 
# ● Manzana = 1500 
# ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)


print("---------------------------------")


# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# ● Banana = 1330 
# ● Manzana = 1700 
# ● Melón = 2800 

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

print(precios_frutas)


print("---------------------------------")


# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# precios. 

frutas = list(precios_frutas.keys())

print(frutas)


print("---------------------------------")


# 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe.


contactos = {}

print("# Carga de Contactos #")
print("Por favor, ingresa 5 contactos:")

# Cargar 5 contactos
for i in range(5):
    nombre = input(f"\nContacto {i+1} - Ingresa el nombre: ").strip()
    telefono = input(f"Contacto {i+1} - Ingresa el telefono: ").strip()
    
    # Almacenar en el diccionario
    contactos[nombre] = telefono

print(f"\nSe han cargado {len(contactos)} contactos correctamente")

# Consulta de contactos

print("\n# Consulta de Contactos #")

while True:
    nombre_consulta = input("\nIngresa el nombre a consultar (o 'salir' para terminar): ").strip()
    
    if nombre_consulta.lower() == 'salir':
        print("Cerrando sistema. Llama a esa persona que hace mucho no llamas <3 ")
        break
    
    if nombre_consulta in contactos:
        print(f"Telefono de {nombre_consulta}: {contactos[nombre_consulta]}")
    else:
        print(f"El contacto '{nombre_consulta}' no existe en la agenda")


print("---------------------------------")


# 5) Solicita al usuario una frase e imprime: 
# • Las palabras únicas (usando un set). 
# • Un diccionario con la cantidad de veces que aparece cada palabra.


def cant_veces(frecuencia):
    if frecuencia == 1:
        return "vez"
    else:
        return "veces"
    
frase = input("Ingrese una frase: ")

palabras = frase.lower().split()

palabras_unicas = set(palabras)

frecuencia_palabras = {}

for palabra in palabras:
    frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1

print("\n # Resultado #")

print(f"\n 1.Palabras Unicas ({len(palabras_unicas)}) palabra: ")
print(sorted(palabras_unicas))

print("\n 2.Frecuencia de palabras: ")
for palabra, frecuencia in sorted(frecuencia_palabras.items()):
    print(f"  '{palabra}': {frecuencia} {cant_veces(frecuencia)}")


print("---------------------------------")


#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
#Luego, mostrá el promedio de cada alumno. 

alumnos = {}

print("# Sistema de Registro de Alumnos #")
print("Ingresa los datos de 3 alumnos:")

for i in range(3):
    print(f"\n# Alumno {i+1} #")
    nombre = input("Nombre del alumno: ").strip()
    
    # Solicitar las 3 notas
    notas = []
    for j in range(3):
        while True:
            nota = float(input(f"Nota {j+1}: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Opcion invalida: La nota debe estar entre 0 y 10")
    
    # almacenar como tupla en el diccionario
    alumnos[nombre] = tuple(notas)

# calcular y mostrar promedios

print("\n Alumnos y sus promedios ")


for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"\n{nombre}:")
    print(f"- Notas: {notas}")
    print(f"- Promedio: {promedio:.2f}")


print("---------------------------------")


# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
# y Parcial 2: 
# • Mostrá los que aprobaron ambos parciales. 
# • Mostrá los que aprobaron solo uno de los dos. 
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).


#Sets originales 
parcial_1 = {1, 2, 3, 4, 5, 6, 7}
parcial_2 = {3, 4, 5, 8, 9, 10}

# Mostrar los sets originales
print("\nEstudiantes que aprobaron el Parcial 1:")
print(sorted(parcial_1))

print("\nEstudiantes que aprobaron el Parcial 2:")
print(sorted(parcial_2))


# Estudiantes que aprobaron ambos parciales
ambos = parcial_1 & parcial_2
print("\nEstudiantes que aprobaron ambos parciales:")
print(sorted(ambos))

# Estudiantes que aprobaron solo uno de los dos 
solo_uno = parcial_1 ^ parcial_2
print("\nEstudiantes que aprobaron solo uno de los dos:")
print(sorted(solo_uno))

# Detalle de los que aprobaron solo cada parcial
solo_parcial_1 = parcial_1 - parcial_2
solo_parcial_2 = parcial_2 - parcial_1
print(f"- Solo Parcial 1: {sorted(solo_parcial_1)}")
print(f"- Solo Parcial 2: {sorted(solo_parcial_2)}")

# Total de estudiantes que aprobaron al menos un parcial
al_menos_uno = parcial_1 | parcial_2
print("\nLista total de estudiantes que aprobaron al menos un parcial:")
print(sorted(al_menos_uno))
print(f"Total: {len(al_menos_uno)} estudiantes")


print("---------------------------------")

#
#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario: 
#• Consultar el stock de un producto ingresado. 
#• Agregar unidades al stock si el producto ya existe. 
#• Agregar un nuevo producto si no existe. 

stock_productos = {
    "cafe": 50,
    "leche": 30,
    "pan": 25,
    "yerba": 40,
}

print("# Sistema de Gestion de Stock #")

def mostrar_stock():
    print(f"\n# Stock ({len(stock_productos)} productos):")
    for producto, cantidad in sorted(stock_productos.items()):
        print(f" - {producto}: {cantidad} unidades")

while True:
    print("\n" + "-"*50)
    print("Opciones:")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades a producto existente")
    print("3. Agregar nuevo producto")
    print("4. Ver todo el stock")
    print("5. Salir")
    
    opcion = input("\nSelecciona una opcion (1-5): ").strip()
    
    if opcion == "1":
        # Consultar stock
        producto = input("Ingresa el nombre del producto a consultar: ").strip().lower()
        if producto in stock_productos:
            print(f"Stock de {producto}: {stock_productos[producto]} unidades")
        else:
            print(f"El producto '{producto}' no existe en el inventario")
    
    elif opcion == "2":
        # Agregar unidades a producto existente
        producto = input("Ingresa el nombre del producto: ").strip().lower()
        if producto in stock_productos:
            unidades = int(input(f"Cuantas unidades agregar a {producto}? "))
            if unidades > 0:
                stock_productos[producto] += unidades
                print(f"Se agregaron {unidades} unidades a {producto}")
                print(f"# Nuevo stock: {stock_productos[producto]} unidades")
            else:
                print("Debes ingresar un numero positivo")
        else:
            print(f"El producto '{producto}' no existe. Usa la opción 3 para agregarlo.")
    
    elif opcion == "3":
        # Agregar nuevo producto
        producto = input("Ingresa el nombre del nuevo producto: ").strip().lower()
        if producto in stock_productos:
            print(f"El producto '{producto}' ya existe en el inventario")
        else:
            stock_inicial = int(input(f"Stock inicial para {producto}: "))
            if stock_inicial >= 0:
                stock_productos[producto] = stock_inicial
                print(f"Producto '{producto}' agregado con {stock_inicial} unidades")
            else:
                print("El stock no puede ser negativo")
    
    elif opcion == "4":
        # Ver todo el stock
        mostrar_stock()
    
    elif opcion == "5":
        # Salir
        print("\nResumen:")
        mostrar_stock()
        print("\nSistema Cerrado. No te olvides de comer frutas :)")
        break
    
    else:
        print("Error. Opcion no valida. Selecciona 1-5")


print("---------------------------------")


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
# Permití consultar qué actividad hay en cierto día y hora. 

agenda = {
    ("lunes", "10:00"): "Hacer las compras",
    ("martes", "08:00"): "Clase de yoga",
    ("miercoles", "21:30"): "Cena en casa",
    ("jueves", "13:00"): "Terminar proyecto",
    ("viernes", "18:00"): "Merecido descanso"
}

def clave_orden(item):
    orden_dias = {
        "lunes": 1,
        "martes": 2,
        "miercoles": 3,
        "jueves": 4,
        "viernes": 5,
        "sabado": 6,
        "domingo": 7
    }
    
    (dia, hora) = item[0]
    return (orden_dias[dia], hora)

def mostrar_agenda_completa():
    print("\nAgenda Completa:")
    if not agenda:
        print(" - La agenda esta vacia")
        return
    
    for (dia, hora), evento in sorted(agenda.items(), key=clave_orden):
        print(f"- {dia:10} {hora:5} -> {evento}")

def consultar_evento(dia, hora):
    clave = (dia.lower(), hora)
    if clave in agenda:
        return f"{dia} a las {hora}: {agenda[clave]}"
    else:
        return f"No hay eventos programados para {dia} a las {hora}"

def agregar_evento(dia, hora, evento):
    clave = (dia.lower(), hora)
    if clave in agenda:
        return f"Ya existe un evento para {dia} a las {hora}: {agenda[clave]}"
    else:
        agenda[clave] = evento
        return f"Evento agregado: {dia} a las {hora} -> {evento}"

def eliminar_evento(dia, hora):
    clave = (dia.lower(), hora)
    if clave in agenda:
        evento_eliminado = agenda.pop(clave)
        return f"Evento eliminado: {dia} a las {hora} -> {evento_eliminado}"
    else:
        return f"No existe evento para {dia} a las {hora}"

# Programa principal
print("# AGENDA PERSONAL #")
print("Dias validos: lunes, martes, miercoles, jueves, viernes, sabado, domingo")
print("Formato de hora: HH:mm (ej: 09:30, 14:00, 16:45)")

while True:
    print("\n" + "-"*50)
    print("Opciones:")
    print("1. Consultar evento")
    print("2. Agregar evento")
    print("3. Eliminar evento")
    print("4. Ver agenda completa")
    print("5. Salir")
    
    opcion = input("\nSelecciona una opcion (1-5): ").strip()
    
    if opcion == "1":
        # Consultar evento
        dia = input("Ingresa el dia: ").strip()
        hora = input("Ingresa la hora (HH:mm): ").strip()
        print(consultar_evento(dia, hora))
    
    elif opcion == "2":
        # Agregar evento
        dia = input("Ingresa el dia: ").strip()
        hora = input("Ingresa la hora (HH:mm): ").strip()
        evento = input("Ingresa el evento: ").strip()
        print(agregar_evento(dia, hora, evento))
    
    elif opcion == "3":
        # Eliminar evento
        dia = input("Ingresa el dia: ").strip()
        hora = input("Ingresa la hora (HH:mm): ").strip()
        print(eliminar_evento(dia, hora))
    
    elif opcion == "4":
        # Ver agenda completa
        mostrar_agenda_completa()
    
    elif opcion == "5":
        # Salir
        print("\nResumen:")
        mostrar_agenda_completa()
        print("\nHasta Luego")
        break
    
    else:
        print("Opcion no valida. Selecciona 1-5")


print("---------------------------------")


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde: 
# • Las capitales sean las claves. 
# • Los países sean los valores.

# Diccionario original 
original = {
    "Argentina": "Buenos Aires",
    "Peru": "Lima",
    "Ecuador": "Quito",
    "Australia": "Canberra",
    "Cuba": "La habana",
}

# Diccionario invertido
invertido = {capital: pais for pais, capital in original.items()}

print("- Diccionario original: -")
print(original)
print("\n- Diccionario invertido: -")
print(invertido)