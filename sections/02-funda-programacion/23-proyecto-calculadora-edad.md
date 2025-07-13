# Proyecto Final: Calculadora de Edad Completa

## 🎯 ¡Construye tu calculadora desde cero!

A lo largo de las lecciones anteriores has visto cómo evoluciona una calculadora de edad. Ahora es tu turno de construir la **versión completa** aplicando todos los conceptos aprendidos.

## � Conceptos que aplicarás

- ✅ **Entrada/Salida**: `input()` y `print()`
- ✅ **Condicionales**: `if`, `elif`, `else`
- ✅ **Ciclos**: `while`, `for`, `break`, `continue`
- ✅ **Funciones**: Organizar código en bloques reutilizables
- ✅ **Variables**: Alcance local y global
- ✅ **Manejo de errores**: `try-except` para robustez

## 🎮 El código completo a construir

Aquí tienes el código final que debes entender y poder escribir:

````python
def calcular_edad(año_nacimiento):
    año_actual = 2025
    return año_actual - año_nacimiento

def calcular_edad_futura(año_nacimiento, año_futuro):
    return año_futuro - año_nacimiento

def main():
    print("=== CALCULADORA DE EDAD PROFESIONAL ===")

    # Obtener datos
    nombre = input("¿Cómo te llamas? ")
    año_nacimiento = int(input("¿En qué año naciste? "))

    # Usar las funciones
    edad_actual = calcular_edad(año_nacimiento)
    edad_2030 = calcular_edad_futura(año_nacimiento, 2030)

    # Mostrar resultados
    print(f"\nHola {nombre}!")
    print(f"Tienes {edad_actual} años")
    print(f"En 2030 tendrás {edad_2030} años")

    # Condicional
    if edad_actual >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

```python
from datetime import date  # Importamos para trabajar con fechas

def obtener_datos_usuario():
    """Función para obtener datos del usuario con validación"""
    nombre = input("¿Cuál es tu nombre? ")
    print("Ingresa tu fecha de nacimiento:")
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    año = int(input("Año: "))
    return nombre, dia, mes, año

def calcular_edad(dia, mes, año):
    """Función para calcular la edad exacta"""
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
    """Función para clasificar la edad en categorías"""
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
    """Función para mostrar el resultado final"""
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
````

## 🔍 Analizando el código paso a paso

### 1. Importación y configuración

```python
from datetime import date  # Para trabajar con fechas exactas
```

### 2. Función para obtener datos

```python
def obtener_datos_usuario():
    # Pide nombre y fecha de nacimiento
    # Retorna todos los datos de una vez
```

### 3. Función para calcular edad

```python
def calcular_edad(dia, mes, año):
    # Calcula edad exacta considerando mes y día
    # Maneja fechas inválidas retornando -1
```

### 4. Función para clasificar

```python
def clasificar_edad(edad):
    # Usa condicionales múltiples (if/elif/else)
    # Retorna la categoría de edad apropiada
```

### 5. Bucle principal

```python
while True:
    # Bucle infinito hasta que el usuario decida salir
    # Maneja errores con try-except
    # Usa break para salir del programa
```

## ✅ Desafíos de práctica

### Desafío 1: Versión básica (10 minutos)

Escribe solo la parte esencial sin funciones:

```python
# Tu código aquí: versión simple sin funciones
print("=== CALCULADORA SIMPLE ===")
# Completa...
```

### Desafío 2: Agregar validaciones (15 minutos)

Mejora el código agregando:

- Validar que el día esté entre 1-31
- Validar que el mes esté entre 1-12
- Validar que el año sea razonable (1900-2025)

### Desafío 3: Más características (20 minutos)

Agrega estas funcionalidades:

- Calcular cuántos días has vivido
- Mostrar en qué día de la semana naciste
- Calcular cuándo cumplirás 100 años

## 🎯 Conceptos aplicados en el proyecto

| Concepto              | Dónde se usa                              | Lección    |
| --------------------- | ----------------------------------------- | ---------- |
| **input()**           | Obtener datos del usuario                 | Lección 16 |
| **Condicionales**     | Validar datos y clasificar edad           | Lección 17 |
| **Ciclos**            | Repetir el programa (`while True`)        | Lección 18 |
| **Control de bucles** | `break` para salir                        | Lección 19 |
| **Funciones**         | Organizar código en bloques               | Lección 20 |
| **Variables**         | Locales en funciones, globales para datos | Lección 21 |
| **Manejo de errores** | `try-except` para entrada inválida        | Lección 22 |

## 🎉 ¡Felicidades por completar el proyecto!

Has construido una aplicación completa que:

- ✅ Es fácil de usar (interfaz amigable)
- ✅ Es robusta (maneja errores)
- ✅ Es precisa (cálculos exactos de fecha)
- ✅ Es reutilizable (se puede usar múltiples veces)
- ✅ Está bien organizada (código en funciones)

Esta calculadora demuestra que dominas los **fundamentos de programación**.

## ➡️ Próximo paso

En la siguiente lección haremos un **resumen** de todo lo aprendido y veremos qué viene después.

---

**💡 Orgullo**: ¡Acabas de crear un programa que usa TODOS los conceptos fundamentales de programación!
