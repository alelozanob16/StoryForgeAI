
from crewai import Agent

from crewai import LLM

import os
from crewai_tools import SerperDevTool



llm = LLM(
    model="openrouter/deepseek/deepseek-r1:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

serper_tool = SerperDevTool(
    api_key = os.getenv("SERPER_API_KEY"),
    search_engine="google",
    search_type="search",
)


# Define your agents
gm_researcher = Agent(
  role='Game Researcher',
  goal='Buscar información sobre videojuegos en internet',
  backstory='Eres especialista en buscar contenido relacionado con videojuegos, centrandote en evitar confusiones con otros medios de entretenimiento.',
  llm=llm,
  tools=[serper_tool]
)

personajes_research = Agent(
  role='Character Screenwriter',
  goal='Desarrollar personalidades de diferentes personajes para ser usados en una historia ',
  backstory='Eres un especialista en desarrollar personalidades complejas e iconicas',
  llm=llm
)

history_writer = Agent(
  role='History Writer',
  goal='Desarrollar una historia a partir de las personalidades de los personajes y la información del videojuego',
  backstory='Eres un escritor experto en crear historias complejas y emocionantes basadas en personajes bien desarrollados abierto a los giros de guión y sin miedo a tomar decisiones dificiles sobre la vida de los personajes.',
  llm=llm
)