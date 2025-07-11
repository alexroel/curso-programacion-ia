# Funciones

## 🎯 ¿Qué son las funciones? (1 minuto)

Una **función** es como una mini-máquina que hace una tarea específica. Le das algo (entrada), hace su trabajo, y te devuelve un resultado.

**Analogía**: Una licuadora es una función - le das frutas, las procesa, y te devuelve un jugo.

## 🔧 Crear tu primera función (3 minutos)

### Sintaxis básica:

```python
def nombre_funcion():
    # Código de la función
    print("¡Hola desde la función!")

# Llamar (usar) la función
nombre_funcion()
```

### Ejemplo práctico:

```python
def saludar():
    print("¡Hola!")
    print("¿Cómo estás?")
    print("¡Que tengas buen día!")

# Usar la función
saludar()
```

### Función que calcula:

```python
def sumar_dos_numeros():
    resultado = 5 + 3
    print("El resultado es:", resultado)

sumar_dos_numeros()  # El resultado es: 8
```

## 📥 Funciones con parámetros (2 minutos)

### Recibir información:

```python
def saludar_persona(nombre):
    print("¡Hola", nombre, "!")
    print("¡Qué gusto verte!")

# Usar la función con diferentes nombres
saludar_persona("Ana")
saludar_persona("Carlos")
```

### Función calculadora:

```python
def sumar(numero1, numero2):
    resultado = numero1 + numero2
    print("La suma es:", resultado)

# Usar con diferentes números
sumar(5, 3)     # La suma es: 8
sumar(10, 20)   # La suma es: 30
```

## 📤 Funciones que devuelven valores (1 minuto)

```python
def multiplicar(a, b):
    resultado = a * b
    return resultado

# Guardar el resultado en una variable
mi_resultado = multiplicar(4, 5)
print(mi_resultado)  # 20

# O usar directamente
print(multiplicar(3, 7))  # 21
```

## ✅ Ejercicio práctico

Crea estas funciones:

1. **Función de presentación**:

```python
def presentarme():
    # Tu código: imprime tu nombre, edad y ciudad
    pass  # Reemplaza esto

presentarme()
```

2. **Función calculadora de edad**:

```python
def calcular_edad(año_nacimiento):
    año_actual = 2025
    edad = año_actual - año_nacimiento
    print("Tienes", edad, "años")

calcular_edad(2000)  # Debería imprimir: Tienes 25 años
```

## 🎮 Ejemplo: Función para juegos

```python
def lanzar_dado():
    import random
    numero = random.randint(1, 6)
    print("Sacaste:", numero)
    return numero

# Usar la función
resultado = lanzar_dado()
```

## 💡 ¿Por qué usar funciones?

- **Organización**: Código más limpio
- **Reutilización**: Escribes una vez, usas muchas veces
- **Fácil de leer**: Cada función tiene un propósito claro
- **Menos errores**: Cambias en un solo lugar

## ➡️ Próximo paso

¡Felicidades! Ya conoces los fundamentos. En la siguiente lección crearemos nuestro **proyecto final**: una calculadora de edad completa.

---

**💡 Recuerda**: Las funciones hacen tu código más organizado y reutilizable. ¡Son como bloques de LEGO que puedes combinar!
