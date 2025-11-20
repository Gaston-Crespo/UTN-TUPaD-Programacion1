nombre_archivo = "productos.txt"

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
# formato:
def mostrar_productos(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
            print("--- Lista de Productos ---")
            for linea in archivo:
                datos = linea.strip().split(',')
                nombre = datos[0]
                precio = datos[1]
                cantidad = datos[2]
                print(f"Producto: {nombre.capitalize()} | Precio: ${precio} | Cantidad: {cantidad}")


print("---------------------------------")


# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

# Mostramos productos existentes
mostrar_productos(nombre_archivo)

# Agregar nuevo producto
print("\n--- Agregar Nuevo Producto ---")
nombre = input("Ingrese el nombre del producto: ").strip().lower()
precio = input("Ingrese el precio del producto: ").strip()
cantidad = input("Ingrese la cantidad del producto: ").strip()

# Agregar al archivo sin borrar el contenido existente
with open(nombre_archivo, 'a') as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

print(f"EL producto '{nombre.capitalize()}' fue agregado con exito!")


print("---------------------------------")


# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
# una lista llamada productos, donde cada elemento sea un diccionario con claves: 
# nombre, precio, cantidad.

productos = []
with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            if not linea.strip():
                continue

            nombre, precio_str, cantidad_str = linea.strip().split(',')
            
            producto_dic = {
                'nombre': nombre,
                'precio': float(precio_str),
                'cantidad': int(cantidad_str)
            }
            
            productos.append(producto_dic)

print(productos)


print("---------------------------------")


# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
# no existe, mostrar un mensaje de error


busqueda_usuario = input("Ingrese el nombre del producto a buscar: ").lower()

producto_encontrado = False

for producto in productos:
    if producto['nombre'].lower() == busqueda_usuario:
        print("\nProducto:")
        print(f"Nombre:   {producto['nombre'].capitalize()}")
        print(f"Precio:   ${producto['precio']:.2f}")
        print(f"Cantidad: {producto['cantidad']}")
        producto_encontrado = True
        break

if not producto_encontrado:
    print(f"\nEl producto '{busqueda_usuario}' no se encuentra en el inventario.")


print("---------------------------------")


# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado 
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
# productos actualizados desde la lista. 


with open(nombre_archivo, 'w') as archivo:
            for producto in productos:
                linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
                archivo.write(linea)
        
print(f"\nSus productos estan guardados en '{nombre_archivo}'.")
print("\nGracias por usar el sistema")
