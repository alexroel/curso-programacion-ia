# Iterando estructuras de datos

## 🚶‍♂️ ¿Qué es iterar? (1 minuto)

**Iterar** significa **recorrer todos los elementos** uno por uno. Como pasar lista en clase o revisar cada cajón de tu cómoda.

### 🎯 Analogía simple:

- **Lista de compras** → Leer cada producto uno por uno
- **Iterar en Python** → Procesar cada elemento uno por uno

## 🔄 Recorriendo listas (2 minutos)

### Forma básica con `for`:

```python
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)
```

**Resultado:**

```
manzana
banana
naranja
```

### Con mensajes personalizados:

```python
colores = ["rojo", "azul", "verde"]

for color in colores:
    print(f"Me gusta el color {color}")
```

## 📚 Recorriendo diccionarios (2 minutos)

### Recorrer solo las claves:

```python
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

for clave in persona:
    print(clave)
# nombre
# edad
# ciudad
```

### Recorrer claves y valores juntos:

```python
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
```

**Resultado:**

```
nombre: Ana
edad: 25
ciudad: Madrid
```

## 🔢 Con números e índices (1 minuto 30 segundos)

### Usando `range()`:

```python
# Números del 0 al 4
for i in range(5):
    print(f"Número: {i}")
```

### Con `enumerate()` para listas:

```python
animales = ["perro", "gato", "pájaro"]

for indice, animal in enumerate(animales):
    print(f"{indice}: {animal}")
```

**Resultado:**

```
0: perro
1: gato
2: pájaro
```

## 🎮 Ejercicios prácticos (2 minutos)

### 1. Lista de compras:

```python
compras = ["pan", "leche", "huevos", "queso"]

print("🛒 Lista de compras:")
for item in compras:
    print(f"- {item}")
```

### 2. Información personal:

```python
yo = {
    "nombre": "Juan",
    "edad": 25,
    "hobby": "programar"
}

print("👤 Información personal:")
for dato, valor in yo.items():
    print(f"{dato.capitalize()}: {valor}")
```

### 3. Contador simple:

```python
print("⏱️ Conteo regresivo:")
for numero in range(5, 0, -1):
    print(f"{numero}...")
print("¡Despegue! 🚀")
```

## 🛠️ Trucos útiles (30 segundos)

### Saltarse elementos:

```python
numeros = [1, 2, 3, 4, 5]

for num in numeros:
    if num == 3:
        continue  # Salta el 3
    print(num)
```

### Parar el bucle:

```python
for num in numeros:
    if num == 3:
        break  # Para en el 3
    print(num)
```

## ✅ Lo que recordar

- **for** recorre elementos automáticamente
- **for clave, valor in diccionario.items()** para diccionarios
- **enumerate()** da índice y elemento
- **range()** genera secuencias de números
- **continue** salta, **break** para

## ➡️ Próximo paso

En la siguiente lección aprenderemos **comprensión de listas** - ¡el truco de los profesionales!

---

**💡 Tip**: ¡Iterar es súper útil para procesar datos masivos, como todos los usuarios de una app o todos los productos de una tienda!
