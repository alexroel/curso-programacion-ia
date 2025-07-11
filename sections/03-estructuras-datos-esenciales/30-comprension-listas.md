# Comprensión de listas

## ⚡ ¿Qué es comprensión de listas? (1 minuto 30 segundos)

**Comprensión de listas** es una forma **súper rápida** de crear listas. Es como un **atajo mágico** que usan los programadores profesionales.

### 🎯 Comparación:

**Forma tradicional** (lo que ya sabes):

```python
numeros = []
for i in range(5):
    numeros.append(i * 2)
print(numeros)  # [0, 2, 4, 6, 8]
```

**Comprensión de listas** (¡el truco profesional!):

```python
numeros = [i * 2 for i in range(5)]
print(numeros)  # [0, 2, 4, 6, 8]
```

**¡Una línea en vez de cuatro!** ⚡

## 🚀 Sintaxis básica (2 minutos)

### Estructura simple:

```python
nueva_lista = [expresión for elemento in lista_original]
```

### Ejemplos fáciles:

**1. Números al cuadrado:**

```python
numeros = [1, 2, 3, 4, 5]
cuadrados = [n * n for n in numeros]
print(cuadrados)  # [1, 4, 9, 16, 25]
```

**2. Palabras en mayúsculas:**

```python
nombres = ["ana", "juan", "maría"]
nombres_mayus = [nombre.upper() for nombre in nombres]
print(nombres_mayus)  # ['ANA', 'JUAN', 'MARÍA']
```

## 🎯 Con condiciones (2 minutos)

### Filtrar elementos:

```python
# Solo números pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [n for n in numeros if n % 2 == 0]
print(pares)  # [2, 4, 6, 8, 10]
```

### Transformar y filtrar:

```python
# Solo nombres largos en mayúsculas
nombres = ["ana", "alejandro", "sofía", "juan"]
nombres_largos = [nombre.upper() for nombre in nombres if len(nombre) > 4]
print(nombres_largos)  # ['ALEJANDRO', 'SOFÍA']
```

## 🎮 Ejemplos prácticos (2 minutos)

### 1. Precios con descuento:

```python
precios = [100, 200, 150, 300]
precios_descuento = [precio * 0.8 for precio in precios]  # 20% descuento
print(precios_descuento)  # [80.0, 160.0, 120.0, 240.0]
```

### 2. Longitud de palabras:

```python
palabras = ["hola", "mundo", "python", "programación"]
longitudes = [len(palabra) for palabra in palabras]
print(longitudes)  # [4, 5, 6, 12]
```

### 3. Temperaturas Celsius a Fahrenheit:

```python
celsius = [0, 10, 20, 30, 40]
fahrenheit = [c * 9/5 + 32 for c in celsius]
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]
```

## 🧠 ¿Cuándo usarla? (1 minuto)

### ✅ Úsala cuando:

- Quieras **transformar** una lista
- Necesites **filtrar** elementos
- Busques código **más limpio**

### ❌ NO la uses cuando:

- La lógica es **muy complicada**
- Necesitas **múltiples líneas** de código
- Prefieres que sea **más fácil de leer**

## 🎯 Ejercicio rápido (30 segundos)

**¡Crea una lista de los primeros 10 números multiplicados por 3!**

```python
# Tu respuesta aquí:
multiplos_tres = [n * 3 for n in range(1, 11)]
print(multiplos_tres)
# ¿Qué resultado esperas?
```

## ✅ Lo que recordar

- **Comprensión** = crear listas en una línea
- **Estructura**: `[expresión for elemento in lista]`
- **Con filtro**: `[expresión for elemento in lista if condición]`
- **¡Hace el código más elegante!**

## ➡️ Próximo paso

En la siguiente lección aprenderemos **desempaquetado y enumerate**.

---

**💡 Tip**: ¡La comprensión de listas es como tener un superpoder - te hace ver como un programador profesional!
