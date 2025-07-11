# Alcance de variables

## 🎯 ¿Dónde viven las variables? (2 minutos)

El **alcance** (o scope) de una variable define dónde puede ser usada en tu programa. Es como preguntar: "¿En qué habitaciones de la casa puedo usar este objeto?"

## 🏠 Variables globales: Para toda la casa (2 minutos)

### Variables fuera de funciones:

```python
# Variable global - se puede usar en todo el programa
nombre = "Ana"

def saludar():
    print("Hola", nombre)  # Puede usar la variable global

def despedir():
    print("Adiós", nombre)  # También puede usarla

saludar()   # Hola Ana
despedir()  # Adiós Ana
```

## 🚪 Variables locales: Solo en su habitación (2 minutos)

### Variables dentro de funciones:

```python
def calcular():
    resultado = 10 + 5  # Variable local
    print(resultado)    # Funciona aquí

calcular()  # 15
print(resultado)  # ❌ ERROR - no existe fuera de la función
```

### Ejemplo claro:

```python
edad = 25  # Global

def celebrar_cumpleanos():
    nueva_edad = edad + 1  # Local (basada en global)
    print("Ahora tienes", nueva_edad, "años")

celebrar_cumpleanos()  # Ahora tienes 26 años
print(edad)            # 25 (la global no cambió)
```

## 🔄 Modificar variables globales (1 minuto)

```python
contador = 0  # Global

def incrementar():
    global contador  # Le decimos que use la global
    contador = contador + 1

print(contador)  # 0
incrementar()
print(contador)  # 1
```

## ✅ Ejercicio práctico

¿Qué imprime este código?

```python
mensaje = "Hola mundo"

def cambiar_mensaje():
    mensaje = "Nuevo mensaje"
    print("Dentro:", mensaje)

cambiar_mensaje()
print("Fuera:", mensaje)
```

**Respuesta:**

```
Dentro: Nuevo mensaje
Fuera: Hola mundo
```

## 💡 Regla simple para principiantes

1. **Variables fuera de funciones** = Se pueden usar en todas partes
2. **Variables dentro de funciones** = Solo en esa función
3. **Si necesitas cambiar una global** = Usa `global nombre_variable`

## ➡️ Próximo paso

En la siguiente lección aprenderemos **manejo básico de errores** - qué hacer cuando algo sale mal.

---

**💡 Recuerda**: Piensa en las variables como objetos en habitaciones - algunas están en la sala común, otras en habitaciones privadas.
