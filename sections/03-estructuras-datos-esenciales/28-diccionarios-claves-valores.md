# Diccionarios: Claves y valores

## 📚 ¿Qué es un diccionario? (2 minutos)

Un **diccionario** es como una **agenda telefónica digital**. Cada contacto tiene un **nombre** (clave) y un **teléfono** (valor).

### 🎯 Analogía perfecta:

**Agenda física:**

- Juan → 123-456-789
- María → 987-654-321

**Diccionario Python:**

```python
contactos = {
    "Juan": "123-456-789",
    "María": "987-654-321"
}
```

## 🚀 Crear diccionarios (2 minutos)

### Sintaxis básica:

```python
# Diccionario vacío
mi_diccionario = {}

# Diccionario con datos
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}

# También funciona así:
colores = {"rojo": "red", "azul": "blue", "verde": "green"}
```

### ¡Pruébalo!

```python
mi_perfil = {
    "nombre": "Tu nombre",
    "hobby": "programar",
    "edad": 20
}
print(mi_perfil)
```

## 🔍 Acceder a valores (1 minuto 30 segundos)

### Buscar por clave:

```python
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

print(persona["nombre"])    # "Ana"
print(persona["edad"])      # 25
print(persona["ciudad"])    # "Madrid"
```

### Método seguro (no da error):

```python
print(persona.get("trabajo", "No especificado"))
# Si no existe "trabajo", muestra "No especificado"
```

## ➕ Agregar y modificar (1 minuto)

### Agregar nueva información:

```python
persona["trabajo"] = "Programadora"
persona["email"] = "ana@email.com"
print(persona)
```

### Cambiar información existente:

```python
persona["edad"] = 26  # Cumpleaños!
print(persona["edad"])  # 26
```

## 🔄 Operaciones útiles (1 minuto)

### Ver todas las claves:

```python
print(persona.keys())
# dict_keys(['nombre', 'edad', 'ciudad', 'trabajo', 'email'])
```

### Ver todos los valores:

```python
print(persona.values())
# dict_values(['Ana', 26, 'Madrid', 'Programadora', 'ana@email.com'])
```

### Verificar si existe una clave:

```python
if "nombre" in persona:
    print("Tiene nombre!")
```

## 🎮 Ejemplo práctico (1 minuto 30 segundos)

**¡Crea un diccionario de tu videojuego favorito!**

```python
juego = {
    "nombre": "Minecraft",
    "año": 2011,
    "género": "Sandbox",
    "jugadores": "Multijugador",
    "precio": 26.95
}

print(f"Mi juego favorito es {juego['nombre']}")
print(f"Salió en {juego['año']}")
print(f"Cuesta ${juego['precio']}")
```

## ✅ Lo que recordar

- **Diccionarios** usan llaves `{}`
- **Clave: valor** → como nombre: teléfono
- **Acceso** con `diccionario["clave"]`
- **Agregar** con `diccionario["nueva_clave"] = valor`
- **¡Súper útiles para organizar información!**

## ➡️ Próximo paso

En la siguiente lección aprenderemos a **recorrer** todas estas estructuras.

---

**💡 Tip**: ¡Los diccionarios son perfectos cuando necesitas conectar dos cosas, como nombre→edad, país→capital, etc.!
