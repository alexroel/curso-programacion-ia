# Proyecto: Inventario de productos

## 🏪 ¿Qué vamos a crear? (1 minuto)

Un **sistema simple de inventario** para una tienda. ¡Como los que usan las tienditas del barrio!

### 🎯 Funciones del programa:

- ✅ **Ver productos** disponibles
- ✅ **Agregar** nuevos productos
- ✅ **Buscar** productos específicos
- ✅ **Calcular** valor total del inventario

## 🗂️ Planificación (1 minuto)

### Estructura de datos:

```python
# Cada producto será un diccionario
producto = {
    "nombre": "Manzanas",
    "cantidad": 50,
    "precio": 2.5
}

# El inventario será una lista de productos
inventario = [producto1, producto2, producto3...]
```

## 💻 Código paso a paso (4 minutos)

### Paso 1: Crear el inventario inicial

```python
# inventario.py
inventario = [
    {"nombre": "Manzanas", "cantidad": 50, "precio": 2.5},
    {"nombre": "Pan", "cantidad": 20, "precio": 1.2},
    {"nombre": "Leche", "cantidad": 15, "precio": 3.0},
    {"nombre": "Huevos", "cantidad": 30, "precio": 4.5}
]

print("🏪 ¡Inventario creado!")
```

### Paso 2: Función para mostrar productos

```python
def mostrar_inventario():
    print("\n📦 INVENTARIO ACTUAL:")
    print("-" * 40)

    for i, producto in enumerate(inventario, 1):
        nombre = producto["nombre"]
        cantidad = producto["cantidad"]
        precio = producto["precio"]
        total = cantidad * precio

        print(f"{i}. {nombre}")
        print(f"   Cantidad: {cantidad}")
        print(f"   Precio: ${precio}")
        print(f"   Valor total: ${total:.2f}")
        print("-" * 20)

# Probar la función
mostrar_inventario()
```

### Paso 3: Agregar productos

```python
def agregar_producto():
    print("\n➕ AGREGAR NUEVO PRODUCTO")
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio por unidad: $"))

    nuevo_producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    }

    inventario.append(nuevo_producto)
    print(f"✅ {nombre} agregado al inventario!")

# Probar agregar un producto
agregar_producto()
mostrar_inventario()
```

### Paso 4: Buscar productos

```python
def buscar_producto():
    print("\n🔍 BUSCAR PRODUCTO")
    busqueda = input("Nombre del producto: ").lower()

    encontrado = False
    for producto in inventario:
        if busqueda in producto["nombre"].lower():
            print(f"\n✅ Encontrado:")
            print(f"   Nombre: {producto['nombre']}")
            print(f"   Cantidad: {producto['cantidad']}")
            print(f"   Precio: ${producto['precio']}")
            encontrado = True

    if not encontrado:
        print("❌ Producto no encontrado")

# Probar búsqueda
buscar_producto()
```

### Paso 5: Calcular valor total

```python
def valor_total_inventario():
    total = 0

    for producto in inventario:
        valor_producto = producto["cantidad"] * producto["precio"]
        total += valor_producto

    print(f"\n💰 Valor total del inventario: ${total:.2f}")

# Probar cálculo
valor_total_inventario()
```

## 🎮 Programa completo (1 minuto)

### ¡Junta todo en un solo archivo!

```python
# inventario_completo.py

# Inventario inicial
inventario = [
    {"nombre": "Manzanas", "cantidad": 50, "precio": 2.5},
    {"nombre": "Pan", "cantidad": 20, "precio": 1.2},
    {"nombre": "Leche", "cantidad": 15, "precio": 3.0}
]

def mostrar_inventario():
    print("\n📦 INVENTARIO:")
    for i, producto in enumerate(inventario, 1):
        nombre = producto["nombre"]
        cantidad = producto["cantidad"]
        precio = producto["precio"]
        print(f"{i}. {nombre} - Cantidad: {cantidad} - Precio: ${precio}")

def agregar_producto():
    nombre = input("Nombre: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: $"))

    inventario.append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
    print("✅ Producto agregado!")

# Menu principal
while True:
    print("\n🏪 GESTIÓN DE INVENTARIO")
    print("1. Ver inventario")
    print("2. Agregar producto")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_inventario()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida")
```

## ✅ Lo que lograste

🎉 **¡Felicidades! Creaste un sistema real de inventario usando:**

- ✅ **Listas** para almacenar múltiples productos
- ✅ **Diccionarios** para organizar información de cada producto
- ✅ **Bucles** para recorrer el inventario
- ✅ **Funciones** para organizar el código
- ✅ **Interacción** con el usuario

## ➡️ Próximo paso

En la siguiente lección haremos el **resumen** de toda la sección.

---

**💡 ¡Increíble!**: ¡Acabas de crear tu primer sistema de gestión! Esto es exactamente lo que usan las empresas reales, solo que más complejo.
