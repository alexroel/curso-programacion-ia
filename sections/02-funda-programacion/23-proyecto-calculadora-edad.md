# Proyecto: Calculadora de Edad

## 🎯 Tu primer proyecto completo (1 minuto)

¡Es hora de aplicar todo lo que has aprendido! Vamos a crear una **calculadora de edad** que combine todos los conceptos: variables, input, operadores, condicionales y funciones.

## 🚀 Versión 1: Básica (2 minutos)

```python
# Calculadora de edad básica
print("=== CALCULADORA DE EDAD ===")

# Pedir información
nombre = input("¿Cómo te llamas? ")
año_nacimiento = input("¿En qué año naciste? ")

# Convertir a número y calcular
año_nacimiento = int(año_nacimiento)
año_actual = 2025
edad = año_actual - año_nacimiento

# Mostrar resultado
print("Hola", nombre)
print("Tienes", edad, "años")
```

## 📊 Versión 2: Con más datos (2 minutos)

```python
print("=== CALCULADORA DE EDAD AVANZADA ===")

# Obtener datos
nombre = input("¿Cómo te llamas? ")
año_nacimiento = int(input("¿En qué año naciste? "))

# Cálculos
año_actual = 2025
edad_actual = año_actual - año_nacimiento
edad_en_2030 = 2030 - año_nacimiento
años_para_100 = 100 - edad_actual

# Resultados
print("\n--- RESULTADOS ---")
print("Hola", nombre, "!")
print("Tienes", edad_actual, "años")
print("En 2030 tendrás", edad_en_2030, "años")
print("Te faltan", años_para_100, "años para cumplir 100")
```

## 🎯 Versión 3: Con funciones (2 minutos)

```python
def calcular_edad(año_nacimiento):
    año_actual = 2025
    return año_actual - año_nacimiento

def calcular_edad_futura(año_nacimiento, año_futuro):
    return año_futuro - año_nacimiento

def main():
    print("=== CALCULADORA DE EDAD PROFESIONAL ===")

    # Obtener datos
    nombre = input("¿Cómo te llamas? ")
    año_nacimiento = int(input("¿En qué año naciste? "))

    # Usar las funciones
    edad_actual = calcular_edad(año_nacimiento)
    edad_2030 = calcular_edad_futura(año_nacimiento, 2030)

    # Mostrar resultados
    print(f"\nHola {nombre}!")
    print(f"Tienes {edad_actual} años")
    print(f"En 2030 tendrás {edad_2030} años")

    # Condicional
    if edad_actual >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

# Ejecutar programa
main()
```

## ✅ Tu desafío personal

Mejora el proyecto agregando:

1. **Más cálculos**:

   - Días vividos (edad × 365)
   - Horas vividas (días × 24)

2. **Más condicionales**:

   - Si puede votar (≥18)
   - Si puede jubilarse (≥65)

3. **Bucle para múltiples personas**:

```python
for i in range(3):
    print(f"\n--- PERSONA {i+1} ---")
    # Tu código aquí
```

## 🎮 Ejemplo completo con todo

```python
def calcular_datos_edad(año_nacimiento):
    año_actual = 2025
    edad = año_actual - año_nacimiento
    dias_vividos = edad * 365
    return edad, dias_vividos

def clasificar_por_edad(edad):
    if edad < 13:
        return "niño/a"
    elif edad < 18:
        return "adolescente"
    elif edad < 65:
        return "adulto/a"
    else:
        return "adulto/a mayor"

def main():
    print("🎂 CALCULADORA DE EDAD SÚPER COMPLETA 🎂")

    nombre = input("¿Cómo te llamas? ")
    año_nacimiento = int(input("¿En qué año naciste? "))

    edad, dias = calcular_datos_edad(año_nacimiento)
    categoria = clasificar_por_edad(edad)

    print(f"\n🎉 ¡Hola {nombre}!")
    print(f"📅 Tienes {edad} años")
    print(f"⏰ Has vivido aproximadamente {dias} días")
    print(f"👤 Eres un/a {categoria}")

main()
```

## 📝 Lo que has usado en este proyecto

✅ **Variables**: nombre, edad, año_nacimiento
✅ **Tipos de datos**: string, int
✅ **Operadores**: suma, resta
✅ **Input/Output**: input(), print()
✅ **Condicionales**: if/else
✅ **Funciones**: organización del código

## 🎉 ¡Felicidades!

¡Has creado tu primer proyecto real! Este programa:

- Es interactivo
- Hace cálculos
- Toma decisiones
- Está bien organizado

## ➡️ Próximo paso

En la siguiente lección haremos un **resumen** de todo lo aprendido y veremos qué viene después.

---

**💡 Orgullo**: ¡Acabas de crear un programa que usa TODOS los conceptos fundamentales de programación!
