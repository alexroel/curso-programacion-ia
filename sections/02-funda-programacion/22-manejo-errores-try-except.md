# Manejo básico de errores

## 🎯 Cuando las cosas salen mal

Los errores son normales en programación. En lugar de que tu programa se "rompa", podemos **capturar** los errores y manejarlos elegantemente.

## 🚨 Problema común: División por cero

### Sin manejo de errores:

```python
numero1 = 10
numero2 = 0
resultado = numero1 / numero2  # ¡ERROR! ZeroDivisionError
```

### Con manejo de errores:

```python
numero1 = 10
numero2 = 0

try:
    resultado = numero1 / numero2
    print("El resultado es:", resultado)
except:
    print("Error: No se puede dividir por cero")
```

## 🛡️ La estructura try-except

### Sintaxis básica:

```python
try:
    # Código que podría fallar
    codigo_peligroso()
except:
    # Qué hacer si falla
    print("Algo salió mal")
```

### Ejemplo práctico con input:

```python
try:
    edad = int(input("Tu edad: "))
    print("Tienes", edad, "años")
except:
    print("Error: Debes escribir un número")
```

**Sin try-except**: Si escribes "veinte" → Programa se rompe
**Con try-except**: Si escribes "veinte" → Mensaje amigable

## 🎮 Ejemplo: Calculadora segura

```python
print("=== CALCULADORA SEGURA ===")

try:
    num1 = int(input("Primer número: "))
    num2 = int(input("Segundo número: "))
    resultado = num1 / num2
    print("Resultado:", resultado)
except:
    print("Error: Verifica que sean números válidos")
    print("Y que no dividas por cero")
```

## ✅ Ejercicio práctico

Haz que este código sea "a prueba de errores":

```python
# Código original (puede fallar)
nombre = input("Tu nombre: ")
edad = int(input("Tu edad: "))
altura = float(input("Tu altura: "))

print(f"Hola {nombre}, tienes {edad} años y mides {altura}m")

# Tu versión mejorada:
try:
    # Tu código aquí
    pass
except:
    # Tu manejo de error aquí
    pass
```

## 🎯 Casos comunes donde usar try-except

- **Convertir texto a número**: `int()`, `float()`
- **Abrir archivos**: Archivo no existe
- **Dividir números**: División por cero
- **Conectar a internet**: Sin conexión

## 💡 Filosofía para principiantes

1. **Escribe código básico primero** - haz que funcione
2. **Identifica qué puede fallar** - input del usuario, cálculos
3. **Agrega try-except** - manejo elegante de errores
4. **Da mensajes útiles** - explica qué salió mal

## ➡️ Próximo paso

¡Felicidades! Ya conoces todos los fundamentos. En la siguiente lección crearemos nuestro **proyecto final**: una calculadora de edad completa.

---

**💡 Recuerda**: Los errores no son fracasos, son oportunidades para hacer tu código más robusto.
