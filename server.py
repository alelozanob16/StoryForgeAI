from fastapi import FastAPI
from fastapi.responses import JSONResponse

from crew_main import run_crew_game_history


import requests

app = FastAPI()

@app.get("/history_by_game/{game_name}")
def history_by_game(game_name: str):
    gh = run_crew_game_history(game_name)
    return JSONResponse(content={"history": gh})