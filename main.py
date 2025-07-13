from datetime import date  # Importamos para trabajar con fechas

def obtener_datos_usuario():
    nombre = input("¿Cuál es tu nombre? ")
    print("Ingresa tu fecha de nacimiento:")
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    año = int(input("Año: "))
    return nombre, dia, mes, año

def calcular_edad(dia, mes, año):
    hoy = date.today()
    try:
        nacimiento = date(año, mes, dia)
    except ValueError:
        return -1
    edad = hoy.year - año
    if (hoy.month, hoy.day) < (mes, dia):
        edad -= 1
    return edad

def clasificar_edad(edad):
    if edad < 0:
        return "Fecha inválida"
    elif edad < 2:
        return "Bebé"
    elif edad < 12:
        return "Niño"
    elif edad < 18:
        return "Adolescente"
    elif edad < 30:
        return "Adulto joven"
    elif edad < 60:
        return "Adulto"
    else:
        return "Adulto mayor"

def mostrar_resultado(nombre, edad, categoria):
    print("\nResultado:")
    print(f"Hola {nombre}, tienes {edad} años.")
    print(f"Categoría: {categoria}")

# Bucle principal para repetir consultas
while True:
    try:
        nombre, dia, mes, año = obtener_datos_usuario()
        edad = calcular_edad(dia, mes, año)
        categoria = clasificar_edad(edad)
        mostrar_resultado(nombre, edad, categoria)

    except ValueError:
        print("\nError: Por favor, asegúrate de ingresar números válidos para el día, mes y año.")

    repetir = input("\n¿Deseas hacer otra consulta? (s/n): ").strip().lower()
    if repetir != 's':
        print("Gracias por usar el programa. ¡Hasta luego!")
        break
    