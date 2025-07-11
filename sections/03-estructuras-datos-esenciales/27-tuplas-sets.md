# Tuplas y Sets

## 🔒 ¿Qué es una tupla? (2 minutos)

Una **tupla** es como una **lista que NO puede cambiar**. Una vez creada, ¡es permanente!

### 📦 Analogía:

- **Lista** = caja con compartimientos movibles
- **Tupla** = caja sellada que no se puede abrir

### Crear tuplas:

```python
# Con paréntesis
coordenadas = (10, 20)
colores_rgb = (255, 0, 128)

# Sin paréntesis también funciona
punto = 5, 15
```

### ¿Cuándo usar tuplas?

- **Coordenadas** → `(x, y)`
- **Fechas** → `(año, mes, día)`
- **Datos que NO deben cambiar**

## 🎯 Acceder a elementos de tuplas (1 minuto)

```python
punto = (10, 20)
print(punto[0])  # 10
print(punto[1])  # 20

# ¡Pero NO puedes cambiarlos!
# punto[0] = 5  ← Esto da ERROR
```

## 🎪 ¿Qué es un Set? (2 minutos)

Un **set** es una **colección SIN elementos repetidos**. ¡Como un club exclusivo!

### 🎭 Analogía:

- **Lista** → puede tener elementos repetidos
- **Set** → cada elemento aparece solo UNA vez

### Crear sets:

```python
# Con llaves
numeros = {1, 2, 3, 4}
colores = {"rojo", "azul", "verde"}

# Desde una lista (quita duplicados automáticamente)
lista_con_duplicados = [1, 2, 2, 3, 3, 3]
numeros_unicos = set(lista_con_duplicados)
print(numeros_unicos)  # {1, 2, 3}
```

## ✨ Magia de los sets (1 minuto 30 segundos)

### Eliminar duplicados automáticamente:

```python
frutas_repetidas = ["manzana", "banana", "manzana", "naranja", "banana"]
frutas_unicas = set(frutas_repetidas)
print(frutas_unicas)
# {'banana', 'naranja', 'manzana'}
```

### Agregar elementos:

```python
colores = {"rojo", "azul"}
colores.add("verde")
print(colores)  # {'rojo', 'azul', 'verde'}
```

## 🔍 Comparación rápida (30 segundos)

| Estructura | Cambiar | Duplicados | Orden | Símbolo |
| ---------- | ------- | ---------- | ----- | ------- |
| **Lista**  | ✅ Sí   | ✅ Sí      | ✅ Sí | `[]`    |
| **Tupla**  | ❌ No   | ✅ Sí      | ✅ Sí | `()`    |
| **Set**    | ✅ Sí   | ❌ No      | ❌ No | `{}`    |

## 🎮 Ejercicio práctico

**¡Experimenta con estos ejemplos!**

```python
# Tupla de tu información personal
yo = ("Juan", 25, "Madrid")
print(yo[0])  # Tu nombre

# Set de tus hobbies favoritos
hobbies = {"leer", "programar", "cocinar", "leer"}
print(hobbies)  # ¿Cuántos elementos hay?
```

## ✅ Lo que recordar

- **Tuplas** → No cambian, usan `()`
- **Sets** → Sin duplicados, usan `{}`
- **Tuplas** → para datos permanentes
- **Sets** → para elementos únicos

## ➡️ Próximo paso

En la siguiente lección aprenderemos sobre **diccionarios** - ¡la estructura más útil!

---

**💡 Tip**: Tuplas para cosas fijas, sets para eliminar duplicados. ¡Cada estructura tiene su superpoder!
