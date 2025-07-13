# Operadores aritméticos y lógicos

En programación, los operadores son símbolos especiales que nos permiten realizar operaciones sobre variables y valores. Son como las herramientas matemáticas que usábamos en el colegio, pero aplicadas a la programación.

## ¿Qué son los operadores?

Los operadores son símbolos que le dicen al programa qué operación realizar. Por ejemplo, el símbolo `+` le dice al programa que sume dos números, así como lo haríamos en matemáticas.

## Operadores Aritméticos

Los operadores aritméticos nos permiten realizar operaciones matemáticas básicas:

### Operadores básicos

| Operador | Nombre          | Descripción                    | Ejemplo       |
| -------- | --------------- | ------------------------------ | ------------- |
| `+`      | Suma            | Suma dos números               | `5 + 3 = 8`   |
| `-`      | Resta           | Resta dos números              | `5 - 3 = 2`   |
| `*`      | Multiplicación  | Multiplica dos números         | `5 * 3 = 15`  |
| `/`      | División        | Divide dos números             | `6 / 3 = 2.0` |
| `//`     | División entera | División sin decimales         | `7 // 3 = 2`  |
| `%`      | Módulo          | Resto de una división          | `7 % 3 = 1`   |
| `**`     | Potenciación    | Eleva un número a una potencia | `2 ** 3 = 8`  |

### Ejemplos prácticos

```python
# Operaciones básicas
numero1 = 10
numero2 = 3

suma = numero1 + numero2        # 13
resta = numero1 - numero2       # 7
multiplicacion = numero1 * numero2  # 30
division = numero1 / numero2    # 3.333...
division_entera = numero1 // numero2  # 3
modulo = numero1 % numero2      # 1
potencia = numero1 ** numero2   # 1000

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"División entera: {division_entera}")
print(f"Módulo: {modulo}")
print(f"Potencia: {potencia}")
```

### ¿Cuándo usar cada operador?

- **División (`/`)**: Cuando necesitas el resultado exacto con decimales
- **División entera (`//`)**: Cuando solo necesitas la parte entera del resultado
- **Módulo (`%`)**: Para saber si un número es par/impar, o para ciclos repetitivos

```python
# Ejemplo: Saber si un número es par o impar
numero = 7
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
```

## Operadores Lógicos

Los operadores lógicos nos permiten combinar condiciones y trabajar con valores verdadero/falso (booleanos).

### Operadores básicos

| Operador | Nombre    | Descripción                                      | Ejemplo                |
| -------- | --------- | ------------------------------------------------ | ---------------------- |
| `and`    | Y lógico  | Verdadero si ambas condiciones son verdaderas    | `True and True = True` |
| `or`     | O lógico  | Verdadero si al menos una condición es verdadera | `True or False = True` |
| `not`    | NO lógico | Invierte el valor de verdad                      | `not True = False`     |

### Tabla de verdad

#### Operador `and`

| A     | B     | A and B |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

#### Operador `or`

| A     | B     | A or B |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

#### Operador `not`

| A     | not A |
| ----- | ----- |
| True  | False |
| False | True  |

### Ejemplos prácticos

```python
# Variables para los ejemplos
edad = 20
tiene_licencia = True
es_estudiante = False

# Operador AND - ambas condiciones deben ser verdaderas
puede_conducir = edad >= 18 and tiene_licencia
print(f"¿Puede conducir? {puede_conducir}")  # True

# Operador OR - al menos una condición debe ser verdadera
descuento = edad < 18 or es_estudiante
print(f"¿Tiene descuento? {descuento}")  # False

# Operador NOT - invierte el valor
no_es_estudiante = not es_estudiante
print(f"¿No es estudiante? {no_es_estudiante}")  # True

# Combinando operadores
acceso_especial = (edad >= 18 and tiene_licencia) or es_estudiante
print(f"¿Tiene acceso especial? {acceso_especial}")  # True
```

## Operadores de Comparación

Estos operadores comparan valores y devuelven `True` o `False`:

| Operador | Nombre        | Descripción                            | Ejemplo           |
| -------- | ------------- | -------------------------------------- | ----------------- |
| `==`     | Igual a       | Verifica si dos valores son iguales    | `5 == 5` → `True` |
| `!=`     | Diferente de  | Verifica si dos valores son diferentes | `5 != 3` → `True` |
| `>`      | Mayor que     | Verifica si el primer valor es mayor   | `5 > 3` → `True`  |
| `<`      | Menor que     | Verifica si el primer valor es menor   | `3 < 5` → `True`  |
| `>=`     | Mayor o igual | Mayor que o igual a                    | `5 >= 5` → `True` |
| `<=`     | Menor o igual | Menor que o igual a                    | `3 <= 5` → `True` |

### Ejemplo de comparaciones

```python
a = 10
b = 5

print(f"{a} == {b}: {a == b}")  # False
print(f"{a} != {b}: {a != b}")  # True
print(f"{a} > {b}: {a > b}")    # True
print(f"{a} < {b}: {a < b}")    # False
print(f"{a} >= {b}: {a >= b}")  # True
print(f"{a} <= {b}: {a <= b}")  # False
```

## Precedencia de Operadores

La precedencia determina el orden en que se evalúan las operaciones:

1. **Paréntesis** `()`
2. **Potenciación** `**`
3. **Multiplicación, División, Módulo** `*`, `/`, `//`, `%`
4. **Suma, Resta** `+`, `-`
5. **Comparaciones** `==`, `!=`, `>`, `<`, `>=`, `<=`
6. **Operadores lógicos** `not`, `and`, `or`

### Ejemplo de precedencia

```python
# Sin paréntesis
resultado1 = 2 + 3 * 4  # Primero 3*4=12, luego 2+12=14
print(resultado1)  # 14

# Con paréntesis
resultado2 = (2 + 3) * 4  # Primero 2+3=5, luego 5*4=20
print(resultado2)  # 20

# Ejemplo más complejo
edad = 25
es_estudiante = False
resultado = edad >= 18 and not es_estudiante or edad < 16
print(resultado)  # True
```

## Ejercicios Prácticos

### Ejercicio 1: Calculadora básica

```python
# Pide dos números al usuario y realiza todas las operaciones
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
if num2 != 0:
    print(f"División: {num1 / num2}")
else:
    print("No se puede dividir por cero")
```

### Ejercicio 2: Verificador de condiciones

```python
# Programa que verifica si una persona puede votar
edad = int(input("Ingresa tu edad: "))
es_ciudadano = input("¿Eres ciudadano? (si/no): ").lower() == "si"

puede_votar = edad >= 18 and es_ciudadano
print(f"¿Puede votar? {puede_votar}")
```

### Ejercicio 3: Número par o impar

```python
numero = int(input("Ingresa un número: "))
es_par = numero % 2 == 0

if es_par:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")
```

## Consejos para Principiantes

1. **Usa paréntesis**: Cuando tengas dudas sobre la precedencia, usa paréntesis para aclarar el orden
2. **Prueba paso a paso**: Si una expresión es compleja, divídela en partes más pequeñas
3. **El módulo es útil**: El operador `%` es muy útil para verificar divisibilidad
4. **Cuidado con la división por cero**: Siempre verifica que no estés dividiendo por cero
5. **Los operadores lógicos son poderosos**: Permiten crear condiciones más complejas y útiles

## Errores Comunes

1. **Confundir `=` con `==`**:

   - `=` asigna un valor
   - `==` compara dos valores

2. **División por cero**:

   ```python
   # ❌ Error
   resultado = 10 / 0

   # ✅ Correcto
   if divisor != 0:
       resultado = 10 / divisor
   ```

3. **Precedencia incorrecta**:

   ```python
   # ❌ Puede ser confuso
   resultado = 2 + 3 * 4 > 10 and True

   # ✅ Más claro
   resultado = ((2 + (3 * 4)) > 10) and True
   ```

## Resumen

Los operadores son herramientas fundamentales en programación:

- **Operadores aritméticos**: Para cálculos matemáticos
- **Operadores lógicos**: Para combinar condiciones
- **Operadores de comparación**: Para comparar valores
- **Precedencia**: Determina el orden de evaluación

¡Practica con estos operadores ya que los usarás constantemente en tus programas!
