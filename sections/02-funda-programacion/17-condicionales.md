# Condicionales

## 🎯 ¿Qué son los condicionales?

Los **condicionales** permiten que tu programa tome decisiones. Es como decir: "**SI** pasa esto, **ENTONCES** haz aquello".

## 🚦 La estructura if

### Sintaxis básica:

```python
if condición:
    # Código que se ejecuta si es verdadero
    print("Se cumple la condición")
```

### Ejemplo práctico:

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
```

**¡Importante!** Nota la **indentación** (4 espacios) después del `:`

### Con input():

```python
nombre = input("¿Cómo te llamas? ")

if nombre == "Ana":
    print("¡Hola Ana! ¡Qué nombre más bonito!")
```

## ⚖️ Operadores de comparación

```python
# Igual a
if edad == 18:
    print("Tienes exactamente 18 años")

# Mayor que
if edad > 18:
    print("Eres mayor de 18")

# Menor que
if edad < 18:
    print("Eres menor de 18")

# Mayor o igual
if edad >= 18:
    print("Eres mayor o igual a 18")

# Menor o igual
if edad <= 17:
    print("Eres menor o igual a 17")

# Diferente de
if edad != 18:
    print("No tienes 18 años")
```

## 🔄 if-else: Dos opciones

```python
edad = int(input("¿Cuántos años tienes? "))

if edad >= 18:
    print("Puedes votar")
else:
    print("Aún no puedes votar")
```

## ✅ Ejercicio práctico

Crea un programa que:

1. Pregunte la edad del usuario
2. Si es mayor o igual a 18, diga "Eres adulto"
3. Si es menor a 18, diga "Eres menor de edad"

```python
# Tu código aquí
edad = int(input("¿Cuántos años tienes? "))

if ___:
    print("___")
else:
    print("___")
```

## 🎮 Ejemplo: Juego simple

```python
numero_secreto = 7
intento = int(input("Adivina el número (1-10): "))

if intento == numero_secreto:
    print("¡Ganaste! 🎉")
else:
    print("Incorrecto. El número era 7")
```

## 💡 Tips importantes

1. **Usa `==` para comparar** (no `=`)
2. **La indentación es obligatoria** (4 espacios)
3. **No olvides los dos puntos** `:`

## ➡️ Próximo paso

En la siguiente lección aprenderemos sobre **ciclos** - cómo repetir acciones automáticamente.

---

**💡 Recuerda**: Los condicionales hacen que tus programas sean inteligentes. ¡Pueden tomar decisiones!
