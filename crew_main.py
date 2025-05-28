

from dotenv import load_dotenv
load_dotenv()

from crewai import Crew, Process, Agent, Task, TaskOutput, CrewOutput

from src.agents import personajes_research,gm_researcher,history_writer
from src.tasks import personalidad_task,research_task,writing_task





def run_crew_game_history(game_name,verbose=True):
  # Form the crew with a sequential process
  report_crew = Crew(
  agents=[gm_researcher,personajes_research, history_writer],
  tasks=[research_task, personalidad_task, writing_task],
  process=Process.sequential,
  verbose=verbose,
  )
  # Execute the crew
  result = report_crew.kickoff(inputs={'game_name':game_name})
  # Accessing the type-safe output
  crew_output = result.raw
  return crew_output

