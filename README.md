# 🌍 HolaMundo Travel

> **Plataforma web de viajes y turismo** para descubrir destinos, explorar información de viajes y realizar reservas de forma sencilla.
> Esta plataforma web fue desarrollada como proyecto final integrador del curso Full Stack Python de Codo a Codo 4.0

## 📋 Descripción

**HolaMundo Travel** es una aplicación web ligera y responsiva diseñada para que los usuarios puedan:

- ✈️ **Descubrir destinos turísticos** con información detallada
- 📍 **Explorar información de viajes** sobre diferentes ubicaciones
- 🎫 **Realizar reservas** de manera intuitiva
- 🎨 **Navegar** por una interfaz moderna y amigable

Es un proyecto **frontend estático** construido con tecnologías web fundamentales, perfecto para aprender o como base para un sitio de viajes.

---

## 🚀 Características

### Funcionalidades

- 🎯 **Navegación fluida** entre secciones
- 📱 **Diseño responsivo** (adapta a móviles, tablets y desktop)
- 🎨 **Interfaz moderna y atractiva** con CSS3
- ⚡ **JavaScript interactivo** para validaciones y dinámicas
- 🖼️ **Galería de imágenes** de destinos

## 💻 Tecnologías Utilizadas

### Frontend Stack

```
┌─────────────────────────────────────┐
│      HolaMundo Travel               │
├─────────────────────────────────────┤
│  HTML5       │ Estructura y contenido│
│  CSS3        │ Estilos y diseño     │
│  JavaScript  │ Interactividad       │
└─────────────────────────────────────┘
```

### Detalles Técnicos

**HTML5:** Semántica moderna, formularios, multimedia
**CSS3:** Flexbox, Grid, Media Queries, Animaciones
**JavaScript:** Validación de formularios, interactividad DOM

---

## 🛠️ Instalación y Uso

### Opción 1️⃣: Clonar y abrir localmente

```bash
# Clona el repositorio
git clone https://github.com/HolaMundoTravel/HolaMundo.git

# Entra en la carpeta
cd HolaMundo

# Abre index.html en tu navegador
# Opción A: Double-click en index.html
# Opción B: Click derecho → "Abrir con" → Navegador
# Opción C: Desde terminal (si tienes Python instalado)
python -m http.server 8000
# Luego ve a http://localhost:8000
```

### Opción 2️⃣: Usar Live Server (Recomendado)

Si tienes **Visual Studio Code**:

1. Instala la extensión **"Live Server"** (Ritwick Dey)
2. Click derecho en `index.html`
3. Selecciona **"Open with Live Server"**
4. ¡Listo! Se abre automáticamente en tu navegador

```bash
# O desde terminal en VSC:
code .
# Luego ctrl+shift+p → "Live Server: Open with Live Server"
```

## ⚙️ Funcionalidades JavaScript

### En `scriptform.js`:
```javascript
// ✅ Validación de formularios en tiempo real
// ✅ Cálculo de precio total según duración
// ✅ Validación de fechas
// ✅ Feedback visual al usuario
```

### En `jsinfo.js`:
```javascript
// ✅ Carga dinámica de información
// ✅ Filtrado de destinos
// ✅ Interactividad en galerías
```

---

## 📱 Responsividad

La aplicación se adapta a todos los tamaños de pantalla:

```
📱 Móvil      (320px - 768px)   → Navegación compacta
💻 Tablet     (768px - 1024px)  → Menú expandido
🖥️ Desktop    (1024px+)         → Interfaz completa
```

**Media Queries:** Configuradas en cada archivo CSS
---

**Última actualización:** 2023

**Desarrollado con ❤️ por Franco Cancino, Luis Macek y Taiel Altamirano
