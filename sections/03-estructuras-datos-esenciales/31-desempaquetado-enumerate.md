# Desempaquetado y enumerate

## 📦 ¿Qué es desempaquetado? (2 minutos)

**Desempaquetado** es como **abrir una caja** y poner cada cosa en su lugar específico.

### 🎯 Analogía simple:

Imagina una caja con 3 regalos y 3 personas. El desempaquetado sería dar un regalo a cada persona directamente.

### Ejemplo básico:

```python
# En vez de hacer esto:
punto = (10, 20)
x = punto[0]  # 10
y = punto[1]  # 20

# Haces esto (¡desempaquetado!):
x, y = (10, 20)
print(x)  # 10
print(y)  # 20
```

## 🎮 Ejemplos prácticos (2 minutos)

### 1. Intercambiar variables:

```python
# ¡El truco más genial de Python!
a = 5
b = 10

# Intercambio en una línea
a, b = b, a

print(a)  # 10
print(b)  # 5
```

### 2. Información personal:

```python
persona = ("Ana", 25, "Madrid")
nombre, edad, ciudad = persona

print(f"Hola, soy {nombre}")
print(f"Tengo {edad} años")
print(f"Vivo en {ciudad}")
```

### 3. Con listas también funciona:

```python
colores = ["rojo", "verde", "azul"]
primero, segundo, tercero = colores

print(f"Mi color favorito es {primero}")
```

## 🔢 ¿Qué es enumerate? (2 minutos)

**enumerate()** te da el **índice Y el elemento** al mismo tiempo. ¡Súper útil!

### Sin enumerate (tedioso):

```python
frutas = ["manzana", "banana", "naranja"]

for i in range(len(frutas)):
    print(f"{i}: {frutas[i]}")
```

### Con enumerate (¡elegante!):

```python
frutas = ["manzana", "banana", "naranja"]

for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")
```

**Resultado:**

```
0: manzana
1: banana
2: naranja
```

## 🎯 Casos de uso reales (1 minuto 30 segundos)

### 1. Lista numerada:

```python
tareas = ["lavar ropa", "hacer compras", "estudiar"]

print("📝 Lista de tareas:")
for num, tarea in enumerate(tareas, 1):  # Empezar en 1
    print(f"{num}. {tarea}")
```

**Resultado:**

```
📝 Lista de tareas:
1. lavar ropa
2. hacer compras
3. estudiar
```

### 2. Posición de elementos:

```python
nombres = ["Juan", "María", "Pedro"]

for posicion, nombre in enumerate(nombres):
    if nombre == "María":
        print(f"María está en la posición {posicion}")
```

## 🌟 Desempaquetado avanzado (1 minuto)

### Con el operador `*` (resto):

```python
numeros = [1, 2, 3, 4, 5]

primero, *resto, ultimo = numeros
print(f"Primero: {primero}")    # 1
print(f"Último: {ultimo}")      # 5
print(f"Resto: {resto}")        # [2, 3, 4]
```

### Solo algunos elementos:

```python
datos = ("Ana", 25, "Madrid", "Programadora", "ana@email.com")

nombre, edad, *otros = datos
print(f"{nombre} tiene {edad} años")
# Ignora el resto de información
```

## 🎮 Ejercicio práctico (30 segundos)

**¡Crea un ranking de tus películas favoritas!**

```python
peliculas = ["Avengers", "Toy Story", "Frozen", "Cars"]

print("🎬 Mis películas favoritas:")
for posicion, pelicula in enumerate(peliculas, 1):
    print(f"{posicion}° lugar: {pelicula}")
```

## ✅ Lo que recordar

- **Desempaquetado** = asignar elementos directamente
- **enumerate()** = índice + elemento juntos
- **`a, b = b, a`** = intercambio instantáneo
- **Hace el código más limpio**

## ➡️ Próximo paso

En la siguiente lección haremos un **proyecto real**: ¡un sistema de inventario!

---

**💡 Tip**: ¡Desempaquetado y enumerate son trucos que distinguen a los programadores principiantes de los intermedios!
