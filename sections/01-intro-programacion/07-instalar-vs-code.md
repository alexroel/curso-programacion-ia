# Instalar VS Code

## 💻 ¿Qué es VS Code?

**Visual Studio Code** es el **editor de código más usado del mundo**. Es como un Word, pero para programadores.

### ¿Por qué es genial?

- **Gratuito** 100%
- **Fácil** de usar
- **Ayuda mientras escribes** código
- **Muestra errores** antes de que ejecutes

## 📥 Instalación

### En Windows:

#### Paso 1: Descargar

1. Ve a **code.visualstudio.com**
2. Haz clic en **"Download for Windows"**
3. Se descarga un archivo `.exe`

#### Paso 2: Instalar

1. Haz **doble clic** en el archivo descargado
2. **Acepta** los términos
3. ⚠️ **¡IMPORTANTE!** Marca **TODAS** estas opciones:
   - ☑️ "Abrir con Code" en archivos
   - ☑️ "Abrir con Code" en carpetas
   - ☑️ Agregar a PATH
4. Haz clic en **"Instalar"**
5. ¡Espera a que termine!

### En Mac:

#### Paso 1: Descargar

1. Ve a **code.visualstudio.com**
2. Haz clic en **"Download for Mac"**

#### Paso 2: Instalar

1. Abre el archivo **.zip** descargado
2. **Arrastra** VS Code a la carpeta **"Aplicaciones"**
3. ¡Listo!

## 🎯 Primera vez abriendo VS Code

### Al abrir VS Code verás:

- **Pantalla de bienvenida**
- **Menú lateral** con iconos
- **Área central** donde escribirás código

### ¡No te preocupes si se ve complicado!

- Solo necesitas saber que aquí **escribirás tu código**
- En la siguiente lección haremos nuestro **primer programa**

## ✅ Lo que recordar

- **VS Code es el mejor editor** para empezar
- **Es completamente gratis**
- **Marca todas las opciones** en la instalación (Windows)
- **No necesitas configurar nada** por ahora

## ➡️ Próximo paso

En la siguiente lección crearemos nuestro **primer programa: ¡Hola Mundo!**

---

**💡 Tip**: Si tienes dudas, pregunta a ChatGPT: "¿Cómo instalo VS Code paso a paso?"

- Abre VS Code
- Presiona `Cmd + Shift + P`
- Escribe "shell command"
- Selecciona "Install 'code' command in PATH"

### 🐧 Linux (Ubuntu/Debian)

#### Método 1: .deb package

```bash
# Descargar el paquete .deb
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'

# Instalar
sudo apt update
sudo apt install code
```

#### Método 2: Snap

```bash
sudo snap install --classic code
```

## 🔧 Configuración inicial

### 1. Primera ejecución

Al abrir VS Code por primera vez verás:

- Pantalla de bienvenida
- Sugerencias de temas
- Opciones de configuración

### 2. Cambiar idioma (opcional)

1. Presiona `Ctrl + Shift + P` (Windows/Linux) o `Cmd + Shift + P` (Mac)
2. Escribe "Configure Display Language"
3. Selecciona "Install additional languages"
4. Busca e instala "Spanish Language Pack"
5. Reinicia VS Code

### 3. Configurar tema

- `Ctrl/Cmd + K, Ctrl/Cmd + T` para cambiar tema
- Temas populares: Dark+ (default), Light+, Monokai

## 🐍 Extensiones esenciales para Python

### 1. Python (Microsoft) - OBLIGATORIA

```
Extensión: ms-python.python
Funciones:
- Resaltado de sintaxis
- Depuración
- Intellisense
- Linting
- Formateo de código
```

### 2. Pylance (Microsoft) - ALTAMENTE RECOMENDADA

```
Extensión: ms-python.vscode-pylance
Funciones:
- Análisis de código avanzado
- Autocompletado inteligente
- Detección de errores
- Sugerencias de tipos
```

### 3. Extensiones adicionales útiles

#### Para principiantes:

```
- Python Indent: Indentación automática
- Bracket Pair Colorizer: Colorea paréntesis coincidentes
- Error Lens: Muestra errores directamente en el código
- Code Runner: Ejecuta código con un clic
```

#### Para IA y productividad:

```
- GitHub Copilot: Sugerencias de código con IA
- GitLens: Mejores funciones de Git
- Live Share: Colaboración en tiempo real
```

## 📦 Instalación de extensiones

### Método 1: Interfaz gráfica

1. Haz clic en el ícono de extensiones (cuadrados) en la barra lateral
2. Busca "Python"
3. Haz clic en "Install" en la extensión de Microsoft

### Método 2: Comando

1. Presiona `Ctrl + Shift + P`
2. Escribe "Extensions: Install Extensions"
3. Busca e instala las extensiones

### Método 3: Terminal integrado

```bash
# Abrir terminal en VS Code: Ctrl + `
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
```

## 🎯 Tu primer proyecto Python en VS Code

### 1. Crear una carpeta de proyecto

```bash
# En terminal
mkdir mi_primer_proyecto
cd mi_primer_proyecto
```

### 2. Abrir en VS Code

```bash
# Desde terminal
code .

# O desde VS Code: File > Open Folder
```

## ✅ ¡VS Code está listo!

¡Perfecto! Ahora tienes VS Code instalado y configurado para programar en Python. En las siguientes lecciones aprenderemos a usarlo para crear nuestros primeros programas.

## 🚨 Solución de problemas comunes

### ❌ Python no se reconoce

**Solución:**

1. `Ctrl + Shift + P`
2. "Python: Select Interpreter"
3. Selecciona la versión de Python que instalaste

### ❌ Extensión Python no funciona

**Solución:**

1. Reinstalar extensión Python
2. Reiniciar VS Code
3. Verificar que Python esté en PATH

## ➡️ Próximo paso

En la siguiente lección escribiremos nuestro primer programa completo: **"Hola Mundo"** usando VS Code.

---

**💡 Consejo**: Dedica tiempo a aprender los atajos de teclado de VS Code. Te harán muchísimo más productivo a largo plazo.
