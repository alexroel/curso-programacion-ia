# Proyecto: Asistente conversacional con IA

## 🤖 ¿Qué vamos a crear? (1 minuto)

Un **chatbot inteligente** que simula conversaciones usando técnicas básicas de IA. ¡Como un mini ChatGPT creado por ti!

### 🎯 Funciones del asistente:

- ✅ **Responde preguntas** básicas
- ✅ **Reconoce palabras clave** en tu mensaje
- ✅ **Mantiene conversaciones** simples
- ✅ **Aprende respuestas** nuevas
- ✅ **Personaliza** sus respuestas

## 🗂️ Planificación del proyecto (1 minuto)

### Estructura del programa:

```python
# 1. Base de conocimiento (diccionario)
respuestas = {
    "saludo": ["¡Hola!", "¿Cómo estás?", "¡Qué tal!"],
    "despedida": ["¡Adiós!", "¡Hasta luego!", "¡Que tengas buen día!"],
    "programacion": ["Python es genial", "Me encanta programar", "¿Quieres aprender a programar?"]
}

# 2. Función para analizar mensaje
# 3. Función para generar respuesta
# 4. Bucle principal de conversación
```

## 💻 Código paso a paso (4 minutos)

### Paso 1: Base de conocimiento

```python
# asistente_ia.py
import random

# Base de conocimiento del asistente
conocimiento = {
    # Saludos
    "hola": ["¡Hola! ¿Cómo estás?", "¡Qué tal! ¿En qué puedo ayudarte?", "¡Hola! Me alegra verte."],
    "buenos dias": ["¡Buenos días! ¿Cómo amaneciste?", "¡Buen día! ¿Qué planes tienes?"],

    # Despedidas
    "adios": ["¡Adiós! Que tengas buen día.", "¡Hasta luego! Fue un placer hablar contigo."],
    "chao": ["¡Chao! ¡Nos vemos pronto!", "¡Hasta la vista!"],

    # Programación
    "python": ["¡Python es increíble! ¿Estás aprendiendo?", "Python es mi lenguaje favorito.", "¿Quieres que te ayude con Python?"],
    "programar": ["Programar es súper divertido.", "¿En qué proyecto estás trabajando?", "¡Me encanta ayudar con programación!"],

    # Preguntas sobre el asistente
    "quien eres": ["Soy tu asistente virtual.", "Soy un chatbot creado en Python.", "¡Soy tu amigo digital!"],
    "como estas": ["¡Estoy genial! ¿Y tú?", "¡De maravilla! Listo para ayudarte.", "¡Excelente! ¿Cómo te sientes tú?"]
}

# Respuestas por defecto
respuestas_default = [
    "Interesante... cuéntame más.",
    "No estoy seguro de entender. ¿Puedes explicar mejor?",
    "¡Qué curioso! ¿Qué opinas de eso?",
    "Hmm... ¿y qué más?",
    "¡Genial! ¿Algo más que quieras contarme?"
]

print("🤖 ¡Hola! Soy tu asistente virtual.")
print("💬 Escribe 'salir' para terminar la conversación.\n")
```

### Paso 2: Función para analizar mensajes

```python
def analizar_mensaje(mensaje):
    """
    Analiza el mensaje del usuario y encuentra palabras clave
    """
    mensaje = mensaje.lower().strip()

    # Buscar palabras clave en el mensaje
    for palabra_clave in conocimiento:
        if palabra_clave in mensaje:
            return palabra_clave

    # Si no encuentra palabras clave
    return None

def generar_respuesta(palabra_clave):
    """
    Genera una respuesta basada en la palabra clave encontrada
    """
    if palabra_clave and palabra_clave in conocimiento:
        # Elegir respuesta aleatoria de la categoría
        respuestas = conocimiento[palabra_clave]
        return random.choice(respuestas)
    else:
        # Respuesta por defecto si no entiende
        return random.choice(respuestas_default)
```

### Paso 3: Bucle principal de conversación

```python
def main():
    """
    Función principal que maneja la conversación
    """
    nombre_usuario = input("¿Cómo te llamas? ")
    print(f"¡Mucho gusto, {nombre_usuario}! ¿En qué puedo ayudarte?\n")

    while True:
        # Obtener mensaje del usuario
        mensaje_usuario = input(f"{nombre_usuario}: ")

        # Verificar si quiere salir
        if mensaje_usuario.lower() in ['salir', 'exit', 'quit', 'bye']:
            print("🤖 ¡Fue un placer hablar contigo! ¡Hasta luego!")
            break

        # Analizar mensaje y generar respuesta
        palabra_clave = analizar_mensaje(mensaje_usuario)
        respuesta = generar_respuesta(palabra_clave)

        # Mostrar respuesta del asistente
        print(f"🤖: {respuesta}\n")

# Ejecutar el programa
if __name__ == "__main__":
    main()
```

## 🎮 Versión mejorada (1 minuto)

### ¡Agreguemos funciones más inteligentes!

```python
def agregar_conocimiento():
    """
    Permite al usuario enseñar nuevas respuestas al asistente
    """
    print("🧠 ¡Enséñame algo nuevo!")
    palabra = input("¿Qué palabra clave quieres que aprenda? ").lower()
    respuesta = input("¿Qué debería responder cuando digan esa palabra? ")

    if palabra in conocimiento:
        conocimiento[palabra].append(respuesta)
    else:
        conocimiento[palabra] = [respuesta]

    print(f"✅ ¡Perfecto! Ya sé responder sobre '{palabra}'")

def mostrar_estadisticas(contador_mensajes):
    """
    Muestra estadísticas de la conversación
    """
    print(f"📊 Estadísticas de nuestra conversación:")
    print(f"💬 Mensajes intercambiados: {contador_mensajes}")
    print(f"🧠 Conceptos que conozco: {len(conocimiento)}")
```

## 🚀 Programa completo avanzado (30 segundos)

### ¡Con todas las funciones integradas!

```python
# Agregar al final del programa principal:

# Comandos especiales
if mensaje_usuario.lower() == "enseñar":
    agregar_conocimiento()
    continue
elif mensaje_usuario.lower() == "estadisticas":
    mostrar_estadisticas(contador_mensajes)
    continue

# Contador de mensajes (agregar al inicio del bucle)
contador_mensajes = 0
# ... (después de cada mensaje)
contador_mensajes += 1
```

## 🎯 Cómo probar tu asistente

**¡Conversa con tu creación!**

```
¿Cómo te llamas? Ana

🤖: ¡Mucho gusto, Ana! ¿En qué puedo ayudarte?

Ana: Hola, ¿cómo estás?
🤖: ¡Hola! ¿Cómo estás?

Ana: Estoy aprendiendo Python
🤖: ¡Python es increíble! ¿Estás aprendiendo?

Ana: enseñar
🧠 ¡Enséñame algo nuevo!
¿Qué palabra clave quieres que aprenda? musica
¿Qué debería responder cuando digan esa palabra? ¡Me encanta la música! ¿Cuál es tu género favorito?
✅ ¡Perfecto! Ya sé responder sobre 'musica'

Ana: Me gusta la música
🤖: ¡Me encanta la música! ¿Cuál es tu género favorito?
```

## 🌟 Mejoras que puedes hacer

### Ideas para expandir tu asistente:

1. **Guardar conversaciones** en un archivo
2. **Reconocimiento de emociones** (feliz, triste, enojado)
3. **Respuestas más largas** y contextuales
4. **Integración con APIs** externas
5. **Interfaz gráfica** con tkinter

## ✅ Lo que lograste

🎉 **¡Felicidades! Creaste tu propio asistente IA usando:**

- ✅ **Diccionarios** para almacenar conocimiento
- ✅ **Funciones** para organizar el código
- ✅ **Bucles** para mantener conversaciones
- ✅ **Análisis de texto** básico
- ✅ **Respuestas aleatorias** para variedad
- ✅ **Aprendizaje dinámico** de nuevos conceptos

## ➡️ Próximo paso

En la siguiente lección haremos el **resumen** de toda la sección sobre IA.

---

**💡 ¡Increíble!**: ¡Acabas de crear tu propia IA conversacional! Esto es la base de cómo funcionan los chatbots reales.
