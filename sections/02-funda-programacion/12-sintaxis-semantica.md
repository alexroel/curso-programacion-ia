# Sintaxis y semántica

## 🎯 Las reglas del juego (1 minuto)

Al igual que el español tiene reglas de gramática, Python tiene sus propias reglas. Aprenderlas es clave para que la computadora te entienda perfectamente.

## 📝 Sintaxis: "¿Cómo se escribe?" (3 minutos)

La **sintaxis** son las reglas de escritura de Python.

### ✅ Correcto:

```python
print("Hola mundo")
nombre = "Ana"
edad = 25
```

### ❌ Incorrecto:

```python
Print("Hola mundo")     # P mayúscula - Error
nombre = Ana            # Falta comillas - Error
edad = 25 años          # Texto sin comillas - Error
```

### Reglas básicas de sintaxis:

1. **Texto entre comillas**: `"Hola"` o `'Hola'`
2. **Números sin comillas**: `25`, `3.14`
3. **Mayúsculas y minúsculas importan**: `print` no `Print`
4. **Paréntesis balanceados**: `print("Hola")`

## 🧠 Semántica: "¿Qué significa?" (3 minutos)

La **semántica** es el significado de lo que escribes.

### Código sintácticamente correcto, pero sin sentido:

```python
edad = "veinticinco"
edad_doble = edad * 2  # ¿Qué significa multiplicar texto?
```

### Código con sentido:

```python
edad = 25
edad_doble = edad * 2  # Ahora sí: 25 * 2 = 50
```

### Ejemplos de errores semánticos:

```python
# Sintácticamente correcto, semánticamente confuso
temperatura = "hace calor"
nueva_temperatura = temperatura + 10  # ¿?

# Mejor:
temperatura = 30
nueva_temperatura = temperatura + 10  # 40 grados
```

## 🔍 Errores comunes de principiantes (1 minuto)

### Error de sintaxis:

```python
print("Hola"  # Falta paréntesis de cierre
```

**Mensaje**: `SyntaxError: unexpected EOF while parsing`

### Error de semántica:

```python
edad = "25"           # Texto
edad_mayor = edad + 1 # Intentar sumar número a texto
```

**Mensaje**: `TypeError: can only concatenate str to str`

## ✅ Ejercicio práctico

Identifica qué está mal:

```python
# 1. ¿Sintaxis o semántica?
Print("Hola")

# 2. ¿Sintaxis o semántica?
nombre = Ana

# 3. ¿Sintaxis o semántica?
edad = "20"
edad_siguiente = edad + 1

# 4. ¿Está bien?
mensaje = "Bienvenido"
print(mensaje)
```

**Respuestas:**

1. Sintaxis - `Print` debe ser `print`
2. Sintaxis - `Ana` debe ser `"Ana"`
3. Semántica - sumar número a texto
4. ¡Perfecto! ✅

## 💡 Tips para evitar errores

1. **Usa un editor como VS Code** - resalta errores
2. **Lee los mensajes de error** - te dicen qué está mal
3. **Practica la sintaxis básica** - se vuelve automático
4. **Piensa en el significado** - ¿tiene sentido lo que escribes?

## ➡️ Próximo paso

En la siguiente lección aprenderemos sobre **variables** - cómo guardar información en la memoria de la computadora.

---

**💡 Recuerda**: Sintaxis = ¿cómo escribir? Semántica = ¿qué significa? ¡Ambas son importantes!
