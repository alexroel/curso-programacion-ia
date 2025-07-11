# Operadores aritméticos

## 🎯 ¿Qué son los operadores? (1 minuto)

Los **operadores** son símbolos que nos permiten hacer operaciones con nuestros datos. ¡Python es como una calculadora súper poderosa!

## ➕ Operadores matemáticos básicos (4 minutos)

### Las operaciones básicas:

```python
# Suma
resultado = 5 + 3        # 8
print(resultado)

# Resta
resultado = 10 - 4       # 6
print(resultado)

# Multiplicación
resultado = 6 * 7        # 42
print(resultado)

# División
resultado = 15 / 3       # 5.0
print(resultado)
```

### Con variables:

```python
precio = 20
descuento = 5

precio_final = precio - descuento
print(precio_final)      # 15
```

## 🔢 Operadores especiales (1 minuto)

```python
# Potencia (elevar a)
resultado = 2 ** 3       # 2 elevado a 3 = 8

# Módulo (resto de división)
resultado = 10 % 3       # 1 (porque 10÷3 = 3 sobra 1)
```

## 💰 Ejemplo práctico: Calculadora de propina (1 minuto)

```python
# Datos del restaurante
cuenta = 50
porcentaje_propina = 15

# Calcular propina
propina = cuenta * porcentaje_propina / 100
total = cuenta + propina

print("Cuenta:")
print(cuenta)
print("Propina:")
print(propina)
print("Total a pagar:")
print(total)
```

## ✅ Ejercicio práctico

Crea una calculadora de edad:

```python
año_actual = 2025
año_nacimiento = ___  # Tu año de nacimiento

# Calcula tu edad
mi_edad = año_actual - año_nacimiento

print("Mi edad es:")
print(mi_edad)
```

## 📊 Orden de operaciones

Python sigue las reglas matemáticas:

```python
resultado = 2 + 3 * 4    # 14 (no 20)
resultado = (2 + 3) * 4  # 20 (con paréntesis)
```

## ➡️ Próximo paso

En la siguiente lección aprenderemos sobre **entrada de datos** - cómo hacer que nuestros programas sean interactivos con `input()`.

---

**💡 Recuerda**: Los operadores te permiten hacer cálculos. ¡Experimenta con diferentes combinaciones!
