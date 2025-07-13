# Ciclos

## 🎯 ¿Qué son los ciclos?

Los **ciclos** (o bucles) permiten repetir código automáticamente. En lugar de escribir lo mismo 100 veces, ¡le dices a Python que lo repita!

## 🔄 El ciclo for

### Repetir un número específico de veces:

```python
for i in range(3):
    print("¡Hola!")
```

**Resultado:**

```
¡Hola!
¡Hola!
¡Hola!
```

### Contar del 1 al 5:

```python
for numero in range(1, 6):
    print(numero)
```

**Resultado:**

```
1
2
3
4
5
```

### Ejemplo práctico: Tabla de multiplicar

```python
numero = 5

for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
```

## 🔢 range() explicado

```python
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(2, 10, 2) # 2, 4, 6, 8 (de 2 en 2)
```

## 🎮 Ejemplo: Contador regresivo

```python
print("Cuenta regresiva:")

for numero in range(10, 0, -1):
    print(numero)

print("¡Despegue! 🚀")
```

## ✅ Ejercicio práctico

1. **Ejercicio 1**: Imprimir tu nombre 5 veces

```python
for i in range(___):
    print("___")
```

2. **Ejercicio 2**: Contar del 1 al 10

```python
for numero in range(___, ___):
    print(___)
```

3. **Ejercicio 3**: Sumar números del 1 al 5

```python
suma = 0
for numero in range(1, 6):
    suma = suma + numero
print("La suma es:", suma)
```

## 🎯 Ejemplo con input(): Preguntar varias veces

```python
for i in range(3):
    nombre = input("Dime un nombre: ")
    print("Hola", nombre)
```

## 💡 ¿Cuándo usar ciclos?

- Repetir saludos
- Hacer cálculos múltiples
- Procesar listas de datos
- Crear juegos con turnos
- ¡Cualquier cosa repetitiva!

## ➡️ Próximo paso

En la siguiente lección aprenderemos sobre **funciones** - cómo organizar nuestro código en bloques reutilizables.

---

**💡 Recuerda**: Los ciclos evitan escribir código repetitivo. ¡Python hace el trabajo pesado por ti!
