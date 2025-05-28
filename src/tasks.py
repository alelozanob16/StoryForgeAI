
from crewai import Task
from src.agents import gm_researcher, personajes_research, history_writer, serper_tool

# Define your tasks
research_task = Task(
  description="""
    Tienes que buscar información sobre el videojuego {game_name}. Debes de extraer toda la información
    posible para que el resto de agentes puedan desarrollar mejor su tarea. 
    Centrate en información relevante. Evita críticas.
    Obten datos de:
    - La sinopsis
    - Los personajes
    - La ambientación
    - La historia del videojuego
    - La jugabilidad
    - La música
    Además debes captar todos los detalles de todos los personajes posibles, incluyendo sus nombres, descripciones, relaciones entre ellos y cualquier otro detalle relevante que pueda ayudar a desarrollar una historia interesante.
    Usa la herramienta de búsqueda para obtener información relevante y completa sobre el videojuego.
    """, 
  agent=gm_researcher, 
  expected_output='Un informe detallado en markdown',
  output_file='output/research_report.md',
  tools=[serper_tool],
)
personalidad_task = Task(
  description="""
  Tienes que crear personalidades para personajes de una historia. Los  personajes te vienen dados de la tarea anterior.

  Tienes que desarrollar un texto en el que explicas como es un personaje:
  - Su caracter
  - Su forma de hablar
  - Su forma de gestionar
  - Su forma de expresarse
  - Su mentalidad
  - Su ideología
  - Sus valores
  
  Este texto lo usará después otro agente para crear una historia, con lo que debe de ser completo.
  """, 
  context=[research_task],
  agent=personajes_research, 
  expected_output='Una lista con el nombre del personaje y su personalidad, en formato JSON',
  output_file='output/characters_personalities.json',
)
writing_task = Task(
  description="""
  Tienes que crear una historia a partir de la información del videojuego y las personalidades de los personajes.
  Tienes que desarrollar un texto en el que explicas la historia de los personajes, como se relacionan entre ellos,
  y como se desarrolla la trama. Debes de tener en cuenta las personalidades de los personajes y la información del videojuego.
  El texto debe de ser lo más detallado posible, y debe de tener en cuenta los giros de guión y las decisiones difíciles que
  los personajes deben de tomar. También debes de tener en cuenta el tono de la historia, que debe de ser acorde a las personalidades de los personajes y la información del videojuego.
  No tienes que ceírte a un final feliz, puedes tomar decisiones difíciles sobre la vida de los personajes. Y es muy importante que no es necesario hacer una historia parecida a la del
  videojuego, puedes tomar decisiones creativas y arriesgadas para crear una historia única y emocionante. Quiero que la historia sea lo más completa posible, incluyendo todos los detalles relevantes de los personajes y la trama.
  
  """, 
  agent=history_writer, 
  expected_output='Un texto en formato txt que describe la historia de los personajes, sus relaciones y la trama, incluyendo giros de guión y decisiones difíciles. El texto tiene que explicar la historia entera de manera ordenada',
  output_file='output/final_report.txt',
)
