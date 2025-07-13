# Alcance de variables

## 🎯 ¿Dónde viven las variables?

El **alcance** (o scope) de una variable define dónde puede ser usada en tu programa. Es como preguntar: "¿En qué habitaciones de la casa puedo usar este objeto?"

## 🏠 Variables globales: Para toda la casa

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

## 🚪 Variables locales: Solo en su habitación

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

## 🔄 Modificar variables globales

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

## 🚀 Proyecto: Entendiendo Variables en Funciones

Veamos cómo el **alcance de variables** afecta nuestra calculadora:

```python
# Versión 5.1: Explorando alcance de variables
from datetime import date

# Variables globales (disponibles en todo el programa)
año_actual = 2025
versión_programa = "Calculadora v5.1"

def obtener_datos_usuario():
    """Las variables aquí son locales a esta función"""
    nombre = input("¿Cuál es tu nombre? ")
    print("Ingresa tu fecha de nacimiento:")
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    año = int(input("Año: "))
    # Estas variables solo existen dentro de esta función
    return nombre, dia, mes, año

def calcular_edad(dia, mes, año):
    """Esta función puede usar variables globales"""
    hoy = date.today()
    nacimiento = date(año, mes, dia)

    # Usamos la variable global año_actual
    edad = año_actual - año
    if (hoy.month, hoy.day) < (mes, dia):
        edad -= 1

    return edad

def mostrar_info_programa():
    """Función que usa variable global"""
    global versión_programa  # Indicamos que queremos usar la global
    print(f"Usando: {versión_programa}")
    print(f"Año de referencia: {año_actual}")

def clasificar_edad(edad):
    """Variables locales para clasificación"""
    # Estas variables solo existen en esta función
    limite_bebe = 2
    limite_niño = 12
    limite_adolescente = 18
    limite_adulto_joven = 30
    limite_adulto = 60

    if edad < limite_bebe:
        return "🍼 Bebé"
    elif edad < limite_niño:
        return "👶 Niño"
    elif edad < limite_adolescente:
        return "🧒 Adolescente"
    elif edad < limite_adulto_joven:
        return "👤 Adulto joven"
    elif edad < limite_adulto:
        return "👨 Adulto"
    else:
        return "👴 Adulto mayor"

# Programa principal
print("=== CALCULADORA DE EDAD ===")
mostrar_info_programa()

while True:
    print("\n" + "="*30)

    # Las variables aquí son locales al bucle principal
    nombre, dia, mes, año = obtener_datos_usuario()
    edad = calcular_edad(dia, mes, año)
    categoria = clasificar_edad(edad)

    print(f"\n🎉 Resultado para {nombre}:")
    print(f"Tienes {edad} años")
    print(f"Categoría: {categoria}")

    repetir = input("\n¿Deseas hacer otra consulta? (s/n): ").strip().lower()
    if repetir != 's':
        print("¡Gracias por usar la calculadora! ¡Hasta luego!")
        break
```

**Conceptos demostrados:**

- ✅ Variables globales (`año_actual`, `versión_programa`)
- ✅ Variables locales en cada función
- ✅ Uso de `global` para modificar variables globales
- ✅ Cómo las funciones pueden acceder a variables globales
- ✅ Variables que solo existen dentro de su función

## 💡 Regla simple para principiantes

1. **Variables fuera de funciones** = Se pueden usar en todas partes
2. **Variables dentro de funciones** = Solo en esa función
3. **Si necesitas cambiar una global** = Usa `global nombre_variable`

## ➡️ Próximo paso

En la siguiente lección aprenderemos **manejo básico de errores** - qué hacer cuando algo sale mal.

---

**💡 Recuerda**: Piensa en las variables como objetos en habitaciones - algunas están en la sala común, otras en habitaciones privadas.
