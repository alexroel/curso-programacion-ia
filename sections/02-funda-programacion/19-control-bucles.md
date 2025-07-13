# Control de bucles

## 🎯 Controlando tus ciclos

A veces necesitas más control sobre tus ciclos: salir antes de tiempo o saltar ciertas repeticiones. Python te da herramientas simples para esto.

## 🛑 break: Salir del ciclo

### Ejemplo básico:

```python
for numero in range(1, 11):
    print(numero)
    if numero == 5:
        break  # Sale del ciclo cuando llega a 5

print("Ciclo terminado")
```

**Resultado:**

```
1
2
3
4
5
Ciclo terminado
```

### Ejemplo práctico: Buscar un número:

```python
numeros = [10, 25, 30, 40, 50]

for numero in numeros:
    print("Revisando:", numero)
    if numero == 30:
        print("¡Encontrado!")
        break
```

## ⏭️ continue: Saltar a la siguiente repetición

### Ejemplo básico:

```python
for numero in range(1, 6):
    if numero == 3:
        continue  # Salta el 3
    print(numero)
```

**Resultado:**

```
1
2
4
5
```

### Ejemplo práctico: Solo números pares:

```python
for numero in range(1, 11):
    if numero % 2 != 0:  # Si es impar
        continue         # Salta al siguiente
    print(numero, "es par")
```

## 🎮 Ejemplo: Juego de adivinanza

```python
numero_secreto = 7

for intento in range(1, 4):  # 3 intentos
    print(f"Intento {intento}")
    numero = int(input("Adivina (1-10): "))

    if numero == numero_secreto:
        print("¡Ganaste! 🎉")
        break
    else:
        print("Incorrecto")

print("Fin del juego")
```

## ✅ Ejercicio práctico

Crea un programa que:

1. Cuente del 1 al 10
2. Pero salte el número 7 (usa `continue`)
3. Y se detenga en el 9 (usa `break`)

```python
for numero in range(1, 11):
    if numero == ___:
        continue
    if numero == ___:
        break
    print(numero)
```

## 🚀 Proyecto: Calculadora con Bucle Principal

Agreguemos un **bucle principal** para que el programa pueda usarse múltiples veces:

```python
# Versión 4: Con bucle principal y control
print("=== CALCULADORA DE EDAD ===")

# Bucle principal para repetir consultas
while True:
    print("\n" + "="*30)

    # Obtener información del usuario
    nombre = input("¿Cuál es tu nombre? ")
    print("Ingresa tu fecha de nacimiento:")
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    año = int(input("Año: "))

    # Validar datos básicos
    datos_validos = True

    if dia < 1 or dia > 31:
        print("⚠️ Día inválido")
        datos_validos = False

    if mes < 1 or mes > 12:
        print("⚠️ Mes inválido")
        datos_validos = False

    if año < 1900 or año > 2025:
        print("⚠️ Año inválido")
        datos_validos = False

    # Si los datos no son válidos, continuar al siguiente ciclo
    if not datos_validos:
        print("Por favor, ingresa datos válidos.")
        continue

    # Calcular edad
    año_actual = 2025
    edad = año_actual - año

    # Mostrar resultado
    print(f"\n🎉 Resultado para {nombre}:")
    print(f"Tienes {edad} años")

    # Clasificación
    if edad < 2:
        categoria = "🍼 Bebé"
    elif edad < 12:
        categoria = "👶 Niño"
    elif edad < 18:
        categoria = "🧒 Adolescente"
    elif edad < 30:
        categoria = "👤 Adulto joven"
    elif edad < 60:
        categoria = "👨 Adulto"
    else:
        categoria = "👴 Adulto mayor"

    print(f"Categoría: {categoria}")

    # Preguntar si continuar
    repetir = input("\n¿Deseas hacer otra consulta? (s/n): ").strip().lower()

    if repetir != 's':
        print("¡Gracias por usar la calculadora! ¡Hasta luego!")
        break
```

**Nuevo en esta versión:**

- ✅ Bucle principal con `while True`
- ✅ Uso de `continue` para datos inválidos
- ✅ Uso de `break` para salir del programa
- ✅ Opción de repetir o salir del programa

## 💡 ¿Cuándo usar cada uno?

- **`break`**: Cuando encuentras lo que buscabas
- **`continue`**: Cuando quieres saltar casos específicos

### Ejemplos reales:

- **break**: Buscar un archivo, encontrar un error, juego terminado
- **continue**: Procesar solo números pares, saltar archivos vacíos

## ➡️ Próximo paso

En la siguiente lección aprenderemos sobre **funciones** - cómo organizar nuestro código en bloques reutilizables.

---

**💡 Recuerda**: `break` = salir completamente, `continue` = saltar solo esta vez.
