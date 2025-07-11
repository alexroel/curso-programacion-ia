# Control de bucles

## 🎯 Controlando tus ciclos (1 minuto)

A veces necesitas más control sobre tus ciclos: salir antes de tiempo o saltar ciertas repeticiones. Python te da herramientas simples para esto.

## 🛑 break: Salir del ciclo (3 minutos)

### Ejemplo básico:

```python
for numero in range(1, 11):
    print(numero)
    if numero == 5:
        break  # Sale del ciclo cuando llega a 5

print("Ciclo terminado")
```

**Resultado:**

```
1
2
3
4
5
Ciclo terminado
```

### Ejemplo práctico: Buscar un número:

```python
numeros = [10, 25, 30, 40, 50]

for numero in numeros:
    print("Revisando:", numero)
    if numero == 30:
        print("¡Encontrado!")
        break
```

## ⏭️ continue: Saltar a la siguiente repetición (2 minutos)

### Ejemplo básico:

```python
for numero in range(1, 6):
    if numero == 3:
        continue  # Salta el 3
    print(numero)
```

**Resultado:**

```
1
2
4
5
```

### Ejemplo práctico: Solo números pares:

```python
for numero in range(1, 11):
    if numero % 2 != 0:  # Si es impar
        continue         # Salta al siguiente
    print(numero, "es par")
```

## 🎮 Ejemplo: Juego de adivinanza (1 minuto)

```python
numero_secreto = 7

for intento in range(1, 4):  # 3 intentos
    print(f"Intento {intento}")
    numero = int(input("Adivina (1-10): "))

    if numero == numero_secreto:
        print("¡Ganaste! 🎉")
        break
    else:
        print("Incorrecto")

print("Fin del juego")
```

## ✅ Ejercicio práctico

Crea un programa que:

1. Cuente del 1 al 10
2. Pero salte el número 7 (usa `continue`)
3. Y se detenga en el 9 (usa `break`)

```python
for numero in range(1, 11):
    if numero == ___:
        continue
    if numero == ___:
        break
    print(numero)
```

## 💡 ¿Cuándo usar cada uno?

- **`break`**: Cuando encuentras lo que buscabas
- **`continue`**: Cuando quieres saltar casos específicos

### Ejemplos reales:

- **break**: Buscar un archivo, encontrar un error, juego terminado
- **continue**: Procesar solo números pares, saltar archivos vacíos

## ➡️ Próximo paso

En la siguiente lección aprenderemos sobre **funciones** - cómo organizar nuestro código en bloques reutilizables.

---

**💡 Recuerda**: `break` = salir completamente, `continue` = saltar solo esta vez.
