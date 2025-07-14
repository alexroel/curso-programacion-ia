from datetime import date  # Importamos para trabajar con fechas

def calcular_edad(dia, mes, año):
    hoy = date.today()
    try:
        nacimiento = date(año, mes, dia)
    except ValueError:
        return -1
    
    if (hoy.year, hoy.month, hoy.day) < (año, mes, dia):
        edad = hoy.year - año
        if (hoy.month, hoy.day) < (mes, dia):
            edad -= 1
    return edad


# Bucle principal para repetir consultas
while True:
    try:
        nombre = input("¿Cuál es tu nombre? ")
        print("Ingresa tu fecha de nacimiento:")
        dia = int(input("Día: "))
        mes = int(input("Mes: "))
        año = int(input("Año: "))

        edad = calcular_edad(dia, mes, año)
        print("\nResultado:")
        print(f"Hola {nombre}, tienes {edad} años.")

    except ValueError:
        print("\nError: Por favor, asegúrate de ingresar números válidos para el día, mes y año.")

    repetir = input("\n¿Deseas hacer otra consulta? (s/n): ").strip().lower()
    if repetir != 's':
        print("Gracias por usar el programa. ¡Hasta luego!")
        break
    