# GitHub Copilot: Sugerencias en tiempo real

## 👨‍💻 Tu compañero de programación (1 minuto)

**GitHub Copilot** es como tener un **programador experto sentado a tu lado** que:

- **Sugiere código** mientras escribes
- **Completa funciones** automáticamente
- **Entiende lo que quieres** hacer
- **Te ayuda a escribir** más rápido

### 🎯 Analogía simple:

Es como el **autocompletado del teléfono**, pero para código. Cuando empiezas a escribir, ¡adivina qué quieres hacer!

## 💰 ¿Cuánto cuesta? (30 segundos)

- **GitHub Copilot**: $10/mes (vale cada centavo)
- **Alternativas gratuitas**:
  - **Codeium** (muy bueno y gratis)
  - **TabNine** (versión gratis limitada)

**Para principiantes: ¡Empieza con Codeium gratis!**

## 🚀 Cómo instalar Codeium en VS Code (2 minutos)

### Paso 1: Ir a extensiones

1. **Abre VS Code**
2. **Ctrl + Shift + X** (o busca el ícono de extensiones)

### Paso 2: Buscar e instalar

1. **Busca**: "Codeium"
2. **Instala** la extensión oficial
3. **Reinicia** VS Code

### Paso 3: Configurar cuenta

1. **Se abrirá** una página web
2. **Crea cuenta** gratis con GitHub o email
3. **Autoriza** la conexión
4. ¡**Listo**! Ya tienes IA programando contigo

## 🎮 Cómo funciona en la práctica (2 minutos 30 segundos)

### **Ejemplo 1: Autocompletado inteligente**

**Tú escribes:**

```python
# Función para calcular el área de un círculo
def area_circulo(
```

**Copilot sugiere (en gris):**

```python
# Función para calcular el área de un círculo
def area_circulo(radio):
    import math
    return math.pi * radio ** 2
```

**Presionas TAB → ¡Se completa automáticamente!**

### **Ejemplo 2: Comentarios se vuelven código**

**Tú escribes:**

```python
# Crear una lista de números del 1 al 10
```

**Copilot sugiere:**

```python
# Crear una lista de números del 1 al 10
numeros = list(range(1, 11))
```

### **Ejemplo 3: Patrones inteligentes**

**Tú escribes:**

```python
frutas = ["manzana", "banana", "naranja"]
# Imprimir cada fruta con su posición
```

**Copilot sugiere:**

```python
for i, fruta in enumerate(frutas):
    print(f"{i+1}. {fruta}")
```

## 🎯 Trucos para usar Copilot efectivamente (1 minuto 30 segundos)

### **1. Comentarios descriptivos:**

```python
# Función que valide si un email es correcto
# Debe verificar que tenga @ y punto
def validar_email(email):
    # Copilot completará automáticamente
```

### **2. Nombres de variables claros:**

```python
# Solo con el nombre, Copilot entiende qué hacer
lista_estudiantes = [
    # Sugerirá estructura de diccionarios para estudiantes
```

### **3. Empezar funciones:**

```python
def calcular_promedio(
    # Copilot sugerirá los parámetros y la lógica
```

### **4. Usar ejemplos:**

```python
# Ejemplo: convertir_celsius_fahrenheit(0) -> 32
def convertir_celsius_fahrenheit(celsius):
    # Copilot usará el ejemplo para entender
```

## ⚡ Teclas útiles (30 segundos)

- **TAB** → Aceptar sugerencia completa
- **Ctrl + →** → Aceptar palabra por palabra
- **Alt + ]** → Siguiente sugerencia
- **Alt + [** → Sugerencia anterior
- **Esc** → Rechazar sugerencia

## 🌟 Casos de uso perfectos para principiantes (1 minuto)

### **1. Aprender sintaxis:**

Copilot te muestra la sintaxis correcta mientras escribes.

### **2. Generar código boilerplate:**

```python
# Programa principal con menú
def main():
    # Copilot sugerirá estructura completa de menú
```

### **3. Aprender buenas prácticas:**

Copilot sugiere código que sigue convenciones profesionales.

### **4. Acelerar tareas repetitivas:**

```python
# Crear 10 estudiantes de ejemplo
estudiantes = [
    # Copilot generará la lista completa
```

## ⚠️ Cuidados importantes (30 segundos)

### **❌ NO hagas esto:**

- **Aceptar código** sin entenderlo
- **Copiar todo** sin revisar
- **Depender 100%** de las sugerencias

### **✅ SÍ haz esto:**

- **Entiende** cada línea sugerida
- **Modifica** si no es exactamente lo que necesitas
- **Aprende** de las sugerencias
- **Usa como herramienta**, no como reemplazo

## 🎮 Ejercicio práctico

**¡Prueba Copilot ahora!**

1. **Instala Codeium** en VS Code
2. **Crea un archivo** `practica_copilot.py`
3. **Escribe este comentario**:

```python
# Función que calcule si un número es par o impar
```

4. **Presiona Enter** y ve qué sugiere
5. **Acepta con TAB** si te gusta la sugerencia

## ✅ Lo que recordar

- **Copilot = compañero de programación inteligente**
- **Codeium** es gratis y muy bueno para empezar
- **Comentarios claros** → mejores sugerencias
- **TAB** para aceptar, **Esc** para rechazar
- **Entiende siempre** el código antes de usarlo
- **¡Te acelera, pero TÚ sigues siendo el programador!**

## ➡️ Próximo paso

En la siguiente lección aprenderemos sobre **ventajas y límites** de la IA en programación.

---

**💡 Tip**: ¡Copilot es increíble para aprender! Te muestra código profesional que puedes estudiar y entender.
