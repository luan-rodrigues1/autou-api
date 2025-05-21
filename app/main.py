"""
Módulo principal da aplicação.
"""

from fastapi import FastAPI
from app.routes import base

app = FastAPI()

# Registrar as rotas
app.include_router(base.router)

@app.get("/")
def read_root():
    return {"message": "API rodando com FastAPI"}