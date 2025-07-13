# Sintaxis y semántica

## 🎯 Las reglas del juego 

Al igual que el español tiene reglas de gramática, Python tiene sus propias reglas. Aprenderlas es clave para que la computadora te entienda perfectamente.

## 📝 Sintaxis: "¿Cómo se escribe?"

La **sintaxis** son las reglas de escritura de Python.

### ✅ Correcto:

```python
print("Hola mundo")
nombre = "Ana"
edad = 25
```

### ❌ Incorrecto:

```python
Print(Hola mundo)    # Texto sin comillas - Error
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


## 💡 Tips para evitar errores

1. **Usa un editor como VS Code** - resalta errores
2. **Lee los mensajes de error** - te dicen qué está mal
3. **Practica la sintaxis básica** - se vuelve automático
4. **Piensa en el significado** - ¿tiene sentido lo que escribes?

## ➡️ Próximo paso

En la siguiente lección aprenderemos sobre **variables** - cómo guardar información en la memoria de la computadora.

---

**💡 Recuerda**: Sintaxis = ¿cómo escribir? Semántica = ¿qué significa? ¡Ambas son importantes!
