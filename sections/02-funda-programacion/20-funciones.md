# Funciones

## 🎯 ¿Qué son las funciones?

Una **función** es como una mini-máquina que hace una tarea específica. Le das algo (entrada), hace su trabajo, y te devuelve un resultado.

**Analogía**: Una licuadora es una función - le das frutas, las procesa, y te devuelve un jugo.

## 🔧 Crear tu primera función

### Sintaxis básica:

```python
def nombre_funcion():
    # Código de la función
    print("¡Hola desde la función!")

# Llamar (usar) la función
nombre_funcion()
```

### Ejemplo práctico:

```python
def saludar():
    print("¡Hola!")
    print("¿Cómo estás?")
    print("¡Que tengas buen día!")

# Usar la función
saludar()
```

### Función que calcula:

```python
def sumar_dos_numeros():
    resultado = 5 + 3
    print("El resultado es:", resultado)

sumar_dos_numeros()  # El resultado es: 8
```

## 📥 Funciones con parámetros

### Recibir información:

```python
def saludar_persona(nombre):
    print("¡Hola", nombre, "!")
    print("¡Qué gusto verte!")

# Usar la función con diferentes nombres
saludar_persona("Ana")
saludar_persona("Carlos")
```

### Función calculadora:

```python
def sumar(numero1, numero2):
    resultado = numero1 + numero2
    print("La suma es:", resultado)

# Usar con diferentes números
sumar(5, 3)     # La suma es: 8
sumar(10, 20)   # La suma es: 30
```

## 📤 Funciones que devuelven valores

```python
def multiplicar(a, b):
    resultado = a * b
    return resultado

# Guardar el resultado en una variable
mi_resultado = multiplicar(4, 5)
print(mi_resultado)  # 20

# O usar directamente
print(multiplicar(3, 7))  # 21
```

## ✅ Ejercicio práctico

Crea estas funciones:

1. **Función de presentación**:

```python
def presentarme():
    # Tu código: imprime tu nombre, edad y ciudad
    pass  # Reemplaza esto

presentarme()
```

2. **Función calculadora de edad**:

```python
def calcular_edad(año_nacimiento):
    año_actual = 2025
    edad = año_actual - año_nacimiento
    print("Tienes", edad, "años")

calcular_edad(2000)  # Debería imprimir: Tienes 25 años
```

## 🚀 Proyecto: Organizando con Funciones

Ahora **organizaremos** nuestro código usando funciones para hacerlo más limpio y reutilizable:

```python
# Versión 5: Código organizado con funciones
from datetime import date  # Para trabajar con fechas

def obtener_datos_usuario():
    """Función para obtener los datos del usuario"""
    nombre = input("¿Cuál es tu nombre? ")
    print("Ingresa tu fecha de nacimiento:")
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    año = int(input("Año: "))
    return nombre, dia, mes, año

def calcular_edad(dia, mes, año):
    """Función para calcular la edad exacta"""
    hoy = date.today()
    nacimiento = date(año, mes, dia)

    edad = hoy.year - año
    # Ajustar si aún no ha sido el cumpleaños este año
    if (hoy.month, hoy.day) < (mes, dia):
        edad -= 1

    return edad

def clasificar_edad(edad):
    """Función para clasificar la edad en categorías"""
    if edad < 2:
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
    """Función para mostrar el resultado final"""
    print(f"\n🎉 Resultado para {nombre}:")
    print(f"Tienes {edad} años")
    print(f"Categoría: {categoria}")

# Programa principal
print("=== CALCULADORA DE EDAD ===")

while True:
    print("\n" + "="*30)

    # Usar nuestras funciones
    nombre, dia, mes, año = obtener_datos_usuario()
    edad = calcular_edad(dia, mes, año)
    categoria = clasificar_edad(edad)
    mostrar_resultado(nombre, edad, categoria)

    # Preguntar si continuar
    repetir = input("\n¿Deseas hacer otra consulta? (s/n): ").strip().lower()
    if repetir != 's':
        print("¡Gracias por usar la calculadora! ¡Hasta luego!")
        break
```

**Nuevo en esta versión:**

- ✅ Código organizado en funciones específicas
- ✅ Cálculo exacto de edad considerando mes y día
- ✅ Funciones reutilizables y bien documentadas
- ✅ Uso de `return` para devolver valores
- ✅ Importación del módulo `datetime` para fechas

## 🎮 Ejemplo: Función para juegos

```python
def lanzar_dado():
    import random
    numero = random.randint(1, 6)
    print("Sacaste:", numero)
    return numero

# Usar la función
resultado = lanzar_dado()
```

## 💡 ¿Por qué usar funciones?

- **Organización**: Código más limpio
- **Reutilización**: Escribes una vez, usas muchas veces
- **Fácil de leer**: Cada función tiene un propósito claro
- **Menos errores**: Cambias en un solo lugar

## ➡️ Próximo paso

¡Felicidades! Ya conoces los fundamentos. En la siguiente lección crearemos nuestro **proyecto final**: una calculadora de edad completa.

---

**💡 Recuerda**: Las funciones hacen tu código más organizado y reutilizable. ¡Son como bloques de LEGO que puedes combinar!
