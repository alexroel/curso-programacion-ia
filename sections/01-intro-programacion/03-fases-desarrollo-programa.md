# Fases de desarrollo de un programa

## 🎯 Los pasos básicos (2 minutos)

Cuando quieres hacer un programa, sigues **4 pasos simples**:

### 1. **¿Qué quiero hacer?** 🤔

Primero piensa exactamente qué problema quieres resolver.

**Ejemplo:**

- "Quiero una calculadora que sume y reste"

### 2. **¿Cómo lo voy a hacer?** 📝

Haces un plan simple, como una receta.

**Plan para calculadora:**

1. Pedir primer número
2. Pedir qué operación (+, -)
3. Pedir segundo número
4. Hacer la operación
5. Mostrar resultado

### 3. **Escribir el código** ⌨️

Aquí escribes las instrucciones en Python.

```python
# Esto es código (¡lo verás pronto!)
numero1 = input("Primer número: ")
operacion = input("+ o -: ")
numero2 = input("Segundo número: ")
# ... más código
```

### 4. **Probarlo y arreglarlo** 🔧

- ¿Funciona bien?
- ¿Hay errores?
- ¿Se puede mejorar?

## 🎮 Ejemplo súper fácil (3 minutos)

**Quiero hacer un programa que me salude:**

### Paso 1: ¿Qué quiero?

- Que me pregunte mi nombre
- Que me salude con mi nombre

### Paso 2: ¿Cómo?

1. Preguntar el nombre
2. Mostrar saludo personalizado

### Paso 3: Código

```python
nombre = input("¿Cómo te llamas? ")
print("¡Hola " + nombre + "! ¡Que tengas buen día!")
```

### Paso 4: Probar

- ¿Funciona? ✅
- ¿Se ve bien? ✅
- ¡Listo!

## 🧠 ¿Por qué seguir estos pasos? (1 minuto)

- **Sin plan = código confuso** 😵
- **Con plan = código ordenado** 😊
- **Ahorras tiempo** al final
- **Evitas errores** grandes

## 🔄 En la vida real (1 minuto)

Los programadores profesionales también siguen estos mismos pasos, ¡solo que con problemas más complejos!

- **Facebook** planea cada nueva función
- **YouTube** diseña antes de programar
- **WhatsApp** prueba todo antes de lanzar

## ✅ Lo que recordar

1. **Planear ANTES de programar**
2. **Dividir el problema** en pasos pequeños
3. **Probar siempre** tu código
4. **No tener miedo** a corregir errores

## ➡️ Próximo paso

En la siguiente lección veremos **cómo la IA puede ayudarte** en cada uno de estos pasos.

---

**💡 Tip**: ¡Los mejores programadores planean más tiempo del que programan!
INICIO

1. Mostrar menú de opciones
2. Pedir al usuario el primer número
3. Pedir la operación (+, -, \*, /)
4. Pedir el segundo número
5. Calcular el resultado
6. Mostrar el resultado
7. Preguntar si desea continuar
   FIN

````

### 3. **Codificación** ⌨️

**¡Escribimos el código!**

- Traducir el diseño a un lenguaje de programación
- Seguir buenas prácticas
- Escribir código limpio y comentado

**Ejemplo en Python:**

```python
# Calculadora simple
def calculadora():
    print("=== CALCULADORA ===")

    while True:
        # Pedir números al usuario
        num1 = float(input("Primer número: "))
        operacion = input("Operación (+, -, *, /): ")
        num2 = float(input("Segundo número: "))

        # Realizar cálculo
        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            resultado = num1 / num2

        # Mostrar resultado
        print(f"Resultado: {resultado}")

        # Preguntar si continuar
        continuar = input("¿Continuar? (s/n): ")
        if continuar.lower() != 's':
            break

# Ejecutar programa
calculadora()
````

### 4. **Pruebas** 🔧

**¿Funciona correctamente?**

- Probar diferentes casos
- Buscar errores (bugs)
- Verificar que cumple los requisitos

**Tipos de pruebas:**

| Tipo               | Descripción             | Ejemplo                             |
| ------------------ | ----------------------- | ----------------------------------- |
| **Casos normales** | Uso típico del programa | 5 + 3 = 8                           |
| **Casos límite**   | Situaciones extremas    | Dividir por cero                    |
| **Casos de error** | Entradas incorrectas    | Ingresar letras en lugar de números |

### 5. **Documentación** 📚

**¿Cómo se usa el programa?**

- Escribir instrucciones de uso
- Documentar el código
- Crear manuales para usuarios

**Ejemplo de documentación:**

```markdown
## Calculadora Simple v1.0

### Cómo usar:

1. Ejecuta el programa
2. Ingresa el primer número
3. Selecciona la operación (+, -, \*, /)
4. Ingresa el segundo número
5. Ve el resultado
6. Decide si continuar o salir

### Requisitos:

- Python 3.6 o superior
```

### 6. **Mantenimiento** 🔄

**Mejoras y correcciones continuas**

- Corregir errores encontrados
- Agregar nuevas funciones
- Optimizar el rendimiento
- Actualizar según necesidades

## 🚀 Ciclo de vida en la práctica

### Proyecto ejemplo: "Lista de Tareas"

#### Fase 1 - Análisis:

- **Problema**: Necesito organizar mis tareas diarias
- **Requisitos**: Agregar, eliminar, marcar como completada

#### Fase 2 - Diseño:

```
MENÚ:
1. Ver tareas
2. Agregar tarea
3. Completar tarea
4. Eliminar tarea
5. Salir
```

#### Fase 3 - Codificación:

```python
tareas = []

def mostrar_menu():
    print("1. Ver tareas")
    print("2. Agregar tarea")
    # ... resto del código
```

#### Fase 4 - Pruebas:

- ✅ ¿Puedo agregar tareas?
- ✅ ¿Puedo marcarlas como completadas?
- ✅ ¿El menú funciona correctamente?

#### Fase 5 - Documentación:

- Instrucciones de uso
- Comentarios en el código

#### Fase 6 - Mantenimiento:

- Agregar categorías de tareas
- Guardar tareas en archivo
- Mejorar la interfaz

## 🤖 Cómo la IA puede ayudar en cada fase

| Fase              | Ayuda de IA                                                      |
| ----------------- | ---------------------------------------------------------------- |
| **Análisis**      | "Ayúdame a definir los requisitos para una app de [descripción]" |
| **Diseño**        | "Crea un pseudocódigo para [problema específico]"                |
| **Codificación**  | "Convierte este pseudocódigo a Python"                           |
| **Pruebas**       | "¿Qué casos de prueba debería considerar?"                       |
| **Documentación** | "Ayúdame a escribir la documentación de este código"             |
| **Mantenimiento** | "¿Cómo puedo mejorar este código?"                               |

## 💡 Consejos para principiantes

### ✅ Haz esto:

- **Planifica antes de codificar**: 10 minutos de diseño ahorran 1 hora de correcciones
- **Divide y vencerás**: Problemas grandes = muchos problemas pequeños
- **Prueba frecuentemente**: No esperes hasta el final
- **Documenta mientras codificas**: Es más fácil que recordar después

### ❌ Evita esto:

- Empezar a codificar sin plan
- Querer crear todo perfecto desde el inicio
- Saltarse las pruebas
- No documentar tu código

## 🎯 Ejercicio práctico

**Aplica las fases a este problema:**

> "Quiero un programa que me ayude a decidir qué película ver. Debe mostrarme películas aleatorias de diferentes géneros y permitirme marcar cuáles ya vi."

1. **Análisis**: ¿Qué requisitos específicos tiene?
2. **Diseño**: Crea un pseudocódigo
3. **Planifica**: ¿Qué funciones necesitarás?

---

## 🤖 Pregunta a la IA

**Prompt para practicar:**

```
"Ayúdame a aplicar las 6 fases de desarrollo para crear un programa que [describe tu idea]. Enfócate especialmente en el análisis y diseño."
```

## ➡️ Próximo paso

En la siguiente lección aprenderemos **cómo aprovechar la inteligencia artificial para aprender programación** de manera más efectiva.

---

**💡 Recuerda**: Un buen programa empieza con un buen plan. Las fases de desarrollo son tu mapa de ruta hacia el éxito.
