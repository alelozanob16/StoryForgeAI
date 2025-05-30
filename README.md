# 🎮 StoryForgeAI

**StoryForgeAI** es una API que genera historias alternativas basadas en videojuegos existentes, utilizando agentes LLM colaborativos. A través de una arquitectura modular, el sistema recopila información sobre un videojuego y crea una narrativa completamente nueva, manteniendo coherencia con la ambientación y los personajes originales.

## 🚀 Tecnologías utilizadas

- **FastAPI**: Para construir y desplegar la API RESTful.
- **CrewAI**: Para la orquestación de múltiples agentes con roles definidos.
- **OpenRouter**: Para acceder a modelos de lenguaje avanzados.
- **Serper**: Para realizar búsquedas contextuales y obtener información relevante sobre videojuegos.
* Para ver los resultados de los trabajos de cada uno de los agentes, ir a la carpeta output.

## 🧠 Arquitectura del sistema

1. **Recopilación de información**: Utiliza Serper para obtener datos sobre el videojuego proporcionado.
2. **Definición de personajes**: Un agente crea perfiles detallados de los personajes principales.
3. **Generación de la historia**: Un guionista virtual elabora la narrativa basada en los elementos anteriores.

## 📦 Instalación y ejecución

1. Clona el repositorio:
   (dentro del directorio que quieras)
   git clone https://github.com/alelozanob16/StoryForgeAI.git
   cd StoryForgeAI

3. Para lanzar la api:
   (dentro del directorio donde este el archivo de la API)
   uvicorn history_API:app --reload
