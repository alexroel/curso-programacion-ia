# Listas: Creación, acceso y métodos básicos

## 📝 ¿Qué es una lista? (1 minuto)

Una **lista** es como una **caja con compartimientos** donde guardas varios elementos juntos.

### 🎯 Analogía fácil:

- **Lista de compras** → papel con varios productos
- **Lista de Python** → variable con varios valores

```python
# En vez de esto:
fruta1 = "manzana"
fruta2 = "banana"
fruta3 = "naranja"

# Hacemos esto:
frutas = ["manzana", "banana", "naranja"]
```

## 🚀 Crear tu primera lista (2 minutos)

### Sintaxis básica:

```python
# Lista vacía
mi_lista = []

# Lista con números
edades = [25, 30, 18, 45]

# Lista con texto
nombres = ["Ana", "Juan", "María"]

# Lista mixta (¡sí se puede!)
datos = ["Pedro", 28, "Madrid", True]
```

### ¡Pruébalo ahora!

```python
colores = ["rojo", "azul", "verde"]
print(colores)
```

**Resultado:**

```
['rojo', 'azul', 'verde']
```

## 🔍 Acceder a elementos (2 minutos)

### Los números empiezan en 0:

```python
frutas = ["manzana", "banana", "naranja"]
#           0          1         2

print(frutas[0])  # "manzana"
print(frutas[1])  # "banana"
print(frutas[2])  # "naranja"
```

### Desde el final (números negativos):

```python
print(frutas[-1])  # "naranja" (último)
print(frutas[-2])  # "banana" (penúltimo)
```

## ➕ Agregar elementos (1 minuto)

### Agregar al final:

```python
frutas = ["manzana", "banana"]
frutas.append("naranja")
print(frutas)
# ['manzana', 'banana', 'naranja']
```

### Agregar en posición específica:

```python
frutas.insert(1, "uva")  # Insertar en posición 1
print(frutas)
# ['manzana', 'uva', 'banana', 'naranja']
```

## ➖ Quitar elementos (1 minuto)

### Quitar por valor:

```python
frutas.remove("banana")  # Quita "banana"
print(frutas)
```

### Quitar por posición:

```python
frutas.pop(0)  # Quita elemento en posición 0
print(frutas)
```

## 🎮 Ejercicio práctico (30 segundos)

**¡Crea tu lista de películas favoritas!**

```python
peliculas = ["Avengers", "Toy Story"]
peliculas.append("Frozen")
print(peliculas[0])  # Tu primera película
```

## ✅ Lo que recordar

- **Las listas** usan corchetes `[]`
- **Los índices** empiezan en 0
- **append()** agrega al final
- **remove()** quita por valor
- **¡Las listas pueden cambiar!**

## ➡️ Próximo paso

En la siguiente lección aprenderemos sobre **tuplas y sets**.

---

**💡 Tip**: ¡Piensa en las listas como contenedores que puedes reorganizar cuando quieras!
