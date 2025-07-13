# Instalación de Python

## 🐍 ¿Qué es Python?

**Python** es el lenguaje que vamos a usar. Es:

- **Súper fácil** de aprender
- **Gratuito** 100%
- Usado por **Google, Netflix, Instagram**

## 💻 Instalación en Windows

### Paso 1: Descargar

1. Ve a **python.org**
2. Haz clic en el botón grande **"Download Python"**
3. Se descarga un archivo (como `python-3.12.exe`)

### Paso 2: Instalar

1. Haz **doble clic** en el archivo descargado
2. ⚠️ **¡MUY IMPORTANTE!** ✅ Marca la casilla **"Add Python to PATH"**
3. Haz clic en **"Install Now"**
4. ¡Espera a que termine!

### Paso 3: Verificar que funciona

1. Presiona **Windows + R**
2. Escribe **cmd** y presiona Enter
3. Escribe: **python --version**
4. Debe aparecer algo como: `Python 3.12.1`

## 🍎 Instalación en Mac (2 minutos)

### Paso 1: Descargar

1. Ve a **python.org**
2. Haz clic en **"Download Python"**
3. Se descarga un archivo `.pkg`

### Paso 2: Instalar

1. Haz **doble clic** en el archivo `.pkg`
2. Sigue los pasos del instalador
3. ¡Listo!

### Paso 3: Verificar

1. Abre **Terminal** (búscalo en Spotlight)
2. Escribe: **python3 --version**
3. Debe aparecer la versión de Python

## ❓ ¿Problemas?

### No aparece la versión:

1. **Reinicia** tu computadora
2. **Intenta otra vez** el comando
3. Si sigue sin funcionar, **reinstala Python** marcando bien "Add to PATH"

## ✅ Lo que recordar

- **Python es gratis** y fácil de instalar
- **"Add Python to PATH"** es súper importante en Windows
- **Verifica siempre** que funcione con el comando de versión

## ➡️ Próximo paso

En la siguiente lección probaremos **la consola interactiva de Python**.

---

**💡 Tip**: Si tienes problemas, pregúntale a ChatGPT: "¿Cómo instalo Python en [tu sistema]?"
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Python

brew install python

### 🐧 Linux (Ubuntu/Debian)

Python normalmente ya está instalado, pero para asegurar la versión más reciente:

```bash
# Actualizar repositorios
sudo apt update

# Instalar Python 3 y pip
sudo apt install python3 python3-pip

# Verificar instalación
python3 --version
```

## ✅ Verificar que Python está funcionando

### 1. Comprobar versión

```bash
# Windows
python --version

# macOS/Linux (a veces necesitas usar python3)
python3 --version
```

**Deberías ver:**

```
Python 3.12.1
```

### 2. Probar el intérprete interactivo

```bash
# Escribir en terminal
python

# O en algunos sistemas
python3
```

**Deberías ver:**

```
Python 3.12.1 (main, Dec  8 2023, 15:04:12)
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## ✅ ¡Verificación final!

Ejecuta este código para confirmar que todo está listo:

1. Abre la consola/terminal
2. Escribe `python` para entrar al intérprete
3. Escribe: `print("¡Python funciona!")`
4. Deberías ver: `¡Python funciona!`
5. Escribe `exit()` para salir

## 🤖 Usando IA para ayuda con instalación

Si tienes problemas, pregunta a ChatGPT:

```
"Tengo problemas instalando Python en [tu sistema operativo].
El error que veo es: [copia el mensaje de error exacto].
¿Puedes ayudarme paso a paso?"
```

## 📚 Recursos adicionales

- **Documentación oficial**: https://docs.python.org/3/
- **Tutorial interactivo**: https://www.learnpython.org/
- **Cheatsheet**: https://www.pythoncheatsheet.org/

## ➡️ Próximo paso

En la siguiente lección exploraremos la **consola interactiva de Python** donde haremos nuestros primeros experimentos.

---

**💡 Consejo**: Si algo no funciona perfectamente, no te preocupes. La programación requiere paciencia, y solucionar problemas de instalación es parte del aprendizaje.
