#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
# modo: IMC = kg/(altura)**2  
print("Ingrese los siguientes datos para saber cual es su IMC")
peso = int(input("Cuantos KG pesa?: "))
altura = float(input("Cual es su altura en mts?: "))
imc = peso / (altura)**2
print(f"Su indice de masa corporal(IMC) es: {imc} ")