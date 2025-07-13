# Ciclos

## 🎯 ¿Qué son los ciclos?

Los **ciclos** (o bucles) permiten repetir código automáticamente. En lugar de escribir lo mismo 100 veces, ¡le dices a Python que lo repita!

## 🔄 El ciclo for

### Repetir un número específico de veces:

```python
for i in range(3):
    print("¡Hola!")
```

**Resultado:**

```
¡Hola!
¡Hola!
¡Hola!
```

### Contar del 1 al 5:

```python
for numero in range(1, 6):
    print(numero)
```

**Resultado:**

```
1
2
3
4
5
```

### Ejemplo práctico: Tabla de multiplicar

```python
numero = 5

for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
```

## 🔢 range() explicado

```python
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(2, 10, 2) # 2, 4, 6, 8 (de 2 en 2)
```

## 🎮 Ejemplo: Contador regresivo

```python
print("Cuenta regresiva:")

for numero in range(10, 0, -1):
    print(numero)

print("¡Despegue! 🚀")
```

## ✅ Ejercicio práctico

1. **Ejercicio 1**: Imprimir tu nombre 5 veces

```python
for i in range(___):
    print("___")
```

2. **Ejercicio 2**: Contar del 1 al 10

```python
for numero in range(___, ___):
    print(___)
```

3. **Ejercicio 3**: Sumar números del 1 al 5

```python
suma = 0
for numero in range(1, 6):
    suma = suma + numero
print("La suma es:", suma)
```

## 🚀 Proyecto: Calculadora con Cálculo de Edad

Ahora agreguemos el **cálculo real de la edad** y clasificación por categorías:

```python
# Versión 3: Calculando la edad real
print("=== CALCULADORA DE EDAD ===")

# Obtener información del usuario
nombre = input("¿Cuál es tu nombre? ")
print("Ingresa tu fecha de nacimiento:")
dia = int(input("Día: "))
mes = int(input("Mes: "))
año = int(input("Año: "))

# Calcular edad (versión simple)
año_actual = 2025
edad = año_actual - año

# Clasificar por edad usando condicionales
print(f"\nHola {nombre}!")
print(f"Tienes aproximadamente {edad} años.")

# Clasificación en categorías
print("\nTu categoría es:")
if edad < 2:
    print("🍼 Bebé")
elif edad < 12:
    print("👶 Niño")
elif edad < 18:
    print("🧒 Adolescente")
elif edad < 30:
    print("👤 Adulto joven")
elif edad < 60:
    print("👨 Adulto")
else:
    print("👴 Adulto mayor")

# Mostrar algunos años importantes
print(f"\nDatos curiosos:")
for i in range(5):
    año_futuro = año_actual + i
    edad_futura = edad + i
    print(f"En {año_futuro} tendrás {edad_futura} años")
```

**Nuevo en esta versión:**

- ✅ Cálculo básico de edad (año actual - año nacimiento)
- ✅ Clasificación en categorías de edad
- ✅ Uso de ciclos para mostrar años futuros
- ✅ Datos curiosos sobre edades futuras

## 🎯 Ejemplo con input(): Preguntar varias veces

```python
for i in range(3):
    nombre = input("Dime un nombre: ")
    print("Hola", nombre)
```

## 💡 ¿Cuándo usar ciclos?

- Repetir saludos
- Hacer cálculos múltiples
- Procesar listas de datos
- Crear juegos con turnos
- ¡Cualquier cosa repetitiva!

## ➡️ Próximo paso

En la siguiente lección aprenderemos sobre **funciones** - cómo organizar nuestro código en bloques reutilizables.

---

**💡 Recuerda**: Los ciclos evitan escribir código repetitivo. ¡Python hace el trabajo pesado por ti!
