# Manejo básico de errores

## 🎯 Cuando las cosas salen mal

Los errores son normales en programación. En lugar de que tu programa se "rompa", podemos **capturar** los errores y manejarlos elegantemente.

## 🚨 Problema común: División por cero

### Sin manejo de errores:

```python
numero1 = 10
numero2 = 0
resultado = numero1 / numero2  # ¡ERROR! ZeroDivisionError
```

### Con manejo de errores:

```python
numero1 = 10
numero2 = 0

try:
    resultado = numero1 / numero2
    print("El resultado es:", resultado)
except:
    print("Error: No se puede dividir por cero")
```

## 🛡️ La estructura try-except

### Sintaxis básica:

```python
try:
    # Código que podría fallar
    codigo_peligroso()
except:
    # Qué hacer si falla
    print("Algo salió mal")
```

### Ejemplo práctico con input:

```python
try:
    edad = int(input("Tu edad: "))
    print("Tienes", edad, "años")
except:
    print("Error: Debes escribir un número")
```

**Sin try-except**: Si escribes "veinte" → Programa se rompe
**Con try-except**: Si escribes "veinte" → Mensaje amigable

## 🎮 Ejemplo: Calculadora segura

```python
print("=== CALCULADORA SEGURA ===")

try:
    num1 = int(input("Primer número: "))
    num2 = int(input("Segundo número: "))
    resultado = num1 / num2
    print("Resultado:", resultado)
except:
    print("Error: Verifica que sean números válidos")
    print("Y que no dividas por cero")
```

## ✅ Ejercicio práctico

Haz que este código sea "a prueba de errores":

```python
# Código original (puede fallar)
nombre = input("Tu nombre: ")
edad = int(input("Tu edad: "))
altura = float(input("Tu altura: "))

print(f"Hola {nombre}, tienes {edad} años y mides {altura}m")

# Tu versión mejorada:
try:
    # Tu código aquí
    pass
except:
    # Tu manejo de error aquí
    pass
```

## 🚀 Proyecto: Calculadora Final con Manejo de Errores

Ahora completaremos nuestra calculadora agregando **manejo robusto de errores**:

```python
# Versión FINAL: Calculadora completa con manejo de errores
from datetime import date

def obtener_datos_usuario():
    """Función para obtener datos con validación de errores"""
    while True:
        try:
            nombre = input("¿Cuál es tu nombre? ")
            if not nombre.strip():  # Verificar que no esté vacío
                print("⚠️ El nombre no puede estar vacío")
                continue

            print("Ingresa tu fecha de nacimiento:")
            dia = int(input("Día: "))
            mes = int(input("Mes: "))
            año = int(input("Año: "))

            # Validaciones básicas
            if not (1 <= dia <= 31):
                print("⚠️ El día debe estar entre 1 y 31")
                continue
            if not (1 <= mes <= 12):
                print("⚠️ El mes debe estar entre 1 y 12")
                continue
            if not (1900 <= año <= 2025):
                print("⚠️ El año debe estar entre 1900 y 2025")
                continue

            return nombre, dia, mes, año

        except ValueError:
            print("⚠️ Error: Asegúrate de ingresar números válidos para día, mes y año")
            print("Inténtalo de nuevo...")

def calcular_edad(dia, mes, año):
    """Función para calcular edad con manejo de errores"""
    try:
        hoy = date.today()
        nacimiento = date(año, mes, dia)

        edad = hoy.year - año
        if (hoy.month, hoy.day) < (mes, dia):
            edad -= 1

        return edad

    except ValueError:
        # Si la fecha no es válida (ej: 31 de febrero)
        return -1

def clasificar_edad(edad):
    """Función para clasificar edad"""
    if edad < 0:
        return "❌ Fecha inválida"
    elif edad < 2:
        return "🍼 Bebé"
    elif edad < 12:
        return "👶 Niño"
    elif edad < 18:
        return "🧒 Adolescente"
    elif edad < 30:
        return "👤 Adulto joven"
    elif edad < 60:
        return "👨 Adulto"
    else:
        return "👴 Adulto mayor"

def mostrar_resultado(nombre, edad, categoria):
    """Función para mostrar resultados"""
    print(f"\n🎉 Resultado para {nombre}:")
    if edad >= 0:
        print(f"Tienes {edad} años")
        print(f"Categoría: {categoria}")
    else:
        print("⚠️ No se pudo calcular la edad debido a una fecha inválida")

# Programa principal con manejo de errores
print("=== CALCULADORA DE EDAD FINAL ===")
print("Esta calculadora maneja errores automáticamente")

# Bucle principal para repetir consultas
while True:
    try:
        print("\n" + "="*40)

        # Obtener datos con validación
        nombre, dia, mes, año = obtener_datos_usuario()

        # Calcular edad
        edad = calcular_edad(dia, mes, año)

        # Clasificar y mostrar
        categoria = clasificar_edad(edad)
        mostrar_resultado(nombre, edad, categoria)

    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido por el usuario")
        break
    except Exception as e:
        print(f"⚠️ Error inesperado: {e}")
        print("Continuando con el programa...")

    # Preguntar si continuar con manejo de errores
    try:
        repetir = input("\n¿Deseas hacer otra consulta? (s/n): ").strip().lower()
        if repetir != 's':
            print("¡Gracias por usar la calculadora! ¡Hasta luego!")
            break
    except KeyboardInterrupt:
        print("\n👋 ¡Hasta luego!")
        break
```

**Características de la versión final:**

- ✅ Manejo completo de errores con `try-except`
- ✅ Validación de entrada de datos
- ✅ Manejo de fechas inválidas (como 31 de febrero)
- ✅ Manejo de interrupción del usuario (Ctrl+C)
- ✅ Bucles de reintento para datos incorrectos
- ✅ Mensajes de error claros y útiles
- ✅ Programa robusto que no se "rompe" fácilmente

## 🎯 Casos comunes donde usar try-except

- **Convertir texto a número**: `int()`, `float()`
- **Abrir archivos**: Archivo no existe
- **Dividir números**: División por cero
- **Conectar a internet**: Sin conexión

## 💡 Filosofía para principiantes

1. **Escribe código básico primero** - haz que funcione
2. **Identifica qué puede fallar** - input del usuario, cálculos
3. **Agrega try-except** - manejo elegante de errores
4. **Da mensajes útiles** - explica qué salió mal

## ➡️ Próximo paso

¡Felicidades! Has completado los fundamentos de programación y construido una **calculadora de edad completa**. En la siguiente lección tendrás el **proyecto final** para practicar todo lo aprendido.

**Lo que has logrado:**

- 📥 Entrada y salida de datos
- 🔀 Condicionales para tomar decisiones
- 🔄 Ciclos para repetir acciones
- 🛑 Control de bucles con break/continue
- 📦 Funciones para organizar código
- 🔍 Alcance de variables
- 🛡️ Manejo de errores robusto

**Tu calculadora final incluye:**

- ✅ Interfaz amigable al usuario
- ✅ Validación completa de datos
- ✅ Cálculo exacto de edad
- ✅ Clasificación por categorías
- ✅ Manejo de errores completo
- ✅ Código bien organizado con funciones

---

**💡 Recuerda**: Los errores no son fracasos, son oportunidades para hacer tu código más robusto.
