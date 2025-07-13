# Entrada y salida de datos

## 🎯 Programas interactivos

Hasta ahora nuestros programas solo muestran información. ¡Es hora de hacerlos **interactivos**! Aprenderemos a pedirle información al usuario.

## 📥 La función input()

### Pedir información:

```python
nombre = input("¿Cómo te llamas? ")
print("Hola")
print(nombre)
```

**Lo que pasa:**

1. El programa pregunta: "¿Cómo te llamas? "
2. El usuario escribe su respuesta
3. Se guarda en la variable `nombre`
4. Se muestra el saludo

### Más ejemplos:

```python
edad = input("¿Cuántos años tienes? ")
ciudad = input("¿De dónde eres? ")

print("Te llamas:")
print(nombre)
print("Tienes años:")
print(edad)
print("Eres de:")
print(ciudad)
```

## 🔢 Importante: input() siempre da texto

```python
# ❌ Problema: input() siempre devuelve texto
edad = input("Tu edad: ")
siguiente_año = edad + 1  # ¡ERROR!

# ✅ Solución: convertir a número
edad = input("Tu edad: ")
edad_numero = int(edad)
siguiente_año = edad_numero + 1

print("El próximo año tendrás:")
print(siguiente_año)
```

### Conversiones útiles:

```python
# Texto a número entero
numero = int(input("Un número: "))

# Texto a número decimal
decimal = float(input("Un decimal: "))
```

## 💻 Ejemplo completo: Calculadora simple

```python
print("=== CALCULADORA SIMPLE ===")

# Pedir números
numero1 = input("Primer número: ")
numero2 = input("Segundo número: ")

# Convertir a números
num1 = int(numero1)
num2 = int(numero2)

# Calcular
suma = num1 + num2

# Mostrar resultado
print("La suma es:")
print(suma)
```

## ✅ Ejercicio práctico

Crea un programa que:

1. Pregunte tu nombre
2. Pregunte tu edad
3. Calcule en qué año cumplirás 100 años
4. Muestre el resultado

```python
# Tu código aquí
nombre = input("___")
# ... continúa
```

## � Proyecto: Comenzando la Calculadora de Edad

A partir de esta lección, comenzaremos a construir una **calculadora de edad completa**. Empezaremos con los fundamentos:

```python
# Versión 1: Recopilar datos básicos
print("=== CALCULADORA DE EDAD ===")

# Obtener información del usuario
nombre = input("¿Cuál es tu nombre? ")
print("Ingresa tu fecha de nacimiento:")
dia = input("Día: ")
mes = input("Mes: ")
año = input("Año: ")

# Mostrar los datos (por ahora solo mostrar)
print(f"\nHola {nombre}!")
print(f"Naciste el {dia}/{mes}/{año}")
print("(En las próximas lecciones calcularemos tu edad)")
```

**En cada lección iremos agregando más funcionalidad:**

- Lección 17: Agregar condicionales para validar datos
- Lección 18: Usar ciclos para repetir el programa
- Lección 20: Organizar el código con funciones
- Lección 22: Manejar errores de entrada

## �📤 Resumen: input() y print()

- **`print()`**: Muestra información al usuario
- **`input()`**: Pide información al usuario
- **`int()`**: Convierte texto a número entero

## ➡️ Próximo paso

En la siguiente lección aprenderemos **condicionales** - cómo hacer que nuestros programas tomen decisiones.

---

**💡 Recuerda**: `input()` siempre devuelve texto. ¡Convierte a número cuando necesites hacer matemáticas!
