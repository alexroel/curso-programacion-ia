# IA para depurar errores y mejorar código

## 🔧 Tu detective de errores personal (1 minuto)

La **IA es como un detective súper experto** que puede encontrar errores en segundos y explicarte exactamente qué está mal y cómo arreglarlo.

### 🕵️ ¿Por qué es increíble?

- **Encuentra errores** instantáneamente
- **Explica qué está mal** en palabras simples
- **Te da el código corregido** listo para usar
- **Te enseña** a evitar el error en el futuro
- **¡Nunca más te frustres con errores misteriosos!**

## 🚨 Template para depurar errores (2 minutos)

### **Fórmula mágica:**

```
"Tengo un error en mi código Python.

Mi código:
[PEGA AQUÍ TU CÓDIGO COMPLETO]

Error que me sale:
[PEGA AQUÍ EL MENSAJE DE ERROR COMPLETO]

Contexto:
- Soy principiante en Python
- Estoy aprendiendo [TEMA QUE PRACTICAS]
- Quiero entender qué hice mal

Por favor:
1. Dime qué está mal en palabras simples
2. Muéstrame el código corregido
3. Explica por qué pasó el error
4. Dame tips para evitarlo en el futuro"
```

## 🎮 Ejemplos reales de debugging (3 minutos)

### **Error 1: SyntaxError (Falta de dos puntos)**

**Tu código con error:**

```python
for i in range(5)
    print(i)
```

**Prompt a la IA:**

```
"Tengo un error en mi código Python.

Mi código:
for i in range(5)
    print(i)

Error que me sale:
SyntaxError: invalid syntax

Contexto:
- Soy principiante en Python
- Estoy aprendiendo bucles for
- No entiendo qué está mal

Por favor ayúdame como expliqué arriba."
```

**Respuesta típica de IA:**

```
"❌ Problema: Te falta ':' después de range(5)

✅ Código corregido:
for i in range(5):
    print(i)

🧠 Explicación:
En Python, los bucles for SIEMPRE necesitan ':' al final de la primera línea.
Es como decir 'para cada número, HAZ LO SIGUIENTE:'

💡 Tip futuro:
Recuerda: if, for, while, def siempre terminan con ':'"
```

### **Error 2: NameError (Variable no definida)**

**Tu código con error:**

```python
edad = 25
nombre = "Ana"
print(f"Hola {nombe}, tienes {edad} años")
```

**Prompt a la IA:**

```
"Tengo un error en mi código Python.

Mi código:
edad = 25
nombre = "Ana"
print(f"Hola {nombe}, tienes {edad} años")

Error que me sale:
NameError: name 'nombe' is not defined

Contexto: Estoy practicando f-strings y variables.
¿Puedes ayudarme?"
```

### **Error 3: IndentationError (Problemas de indentación)**

**Tu código con error:**

```python
if edad >= 18:
print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

## 🔄 Template para mejorar código (1 minuto 30 segundos)

### **Para código que funciona pero quieres mejorarlo:**

```
"Tengo este código Python que funciona, pero quiero mejorarlo.

Mi código:
[PEGA TU CÓDIGO]

Contexto:
- Soy principiante en Python
- Conozco [LISTA LOS CONCEPTOS QUE MANEJAS]
- Quiero que sea más limpio/legible/eficiente

Por favor:
1. Revísalo y sugiere mejoras
2. Explica cada cambio que propones
3. Mantén la simplicidad para principiante
4. Dime si uso buenas prácticas"
```

## 🎯 Casos especiales de debugging (1 minuto 30 segundos)

### **1. Código que no hace lo que esperabas:**

```
"Mi código no da error, pero no hace lo que quiero.

Código:
[TU CÓDIGO]

Lo que espero que haga:
[EXPLICA QUE DEBERÍA PASAR]

Lo que realmente hace:
[EXPLICA QUE PASA EN REALIDAD]

¿Puedes ayudarme a entender por qué?"
```

### **2. Optimización simple:**

```
"Este código funciona pero se ve muy largo/repetitivo.
¿Hay una forma más simple de hacer lo mismo?
Recuerda que soy principiante.

Código:
[TU CÓDIGO]"
```

### **3. Errores lógicos:**

```
"Mi código corre sin errores pero los resultados están mal.
¿Puedes revisar mi lógica paso a paso?

Código:
[TU CÓDIGO]

Resultado esperado: [X]
Resultado que obtengo: [Y]"
```

## 🚀 Trucos profesionales (30 segundos)

### **1. Debug paso a paso:**

```
"¿Puedes agregar prints de debug a mi código para ver qué pasa en cada paso?"
```

### **2. Explicar errores comunes:**

```
"¿Cuáles son los 5 errores más comunes que cometen los principiantes con [TEMA]? Con ejemplos."
```

### **3. Código más legible:**

```
"¿Cómo puedo hacer este código más fácil de leer y entender?"
```

## 🎮 Ejercicio práctico

**¡Prueba con este código que tiene errores!**

```python
def calcular_promedio(notas)
    suma = 0
    for nota in notas:
    suma += nota
    promedio = suma / len(notas)
return promedio

notas_estudiante = [85, 90, 78, 92]
resultado = calcular_promedio(notas_estudiante)
print(f"El promedio es: {resultado}")
```

**Usa el template de debugging y pregúntale a ChatGPT qué está mal.**

## ✅ Lo que recordar

- **Copia SIEMPRE** el mensaje de error completo
- **Incluye TODO** tu código, no solo la línea problemática
- **Explica el contexto** de lo que intentas hacer
- **Pide explicación** en palabras simples
- **Solicita tips** para evitar errores futuros
- **¡No tengas vergüenza** de errores "tontos"!

## ➡️ Próximo paso

En la siguiente lección aprenderemos sobre **GitHub Copilot** - tu compañero de programación en tiempo real.

---

**💡 Tip**: ¡Los errores son normales y todos los programadores los tienen! La IA convierte la frustración en aprendizaje.
