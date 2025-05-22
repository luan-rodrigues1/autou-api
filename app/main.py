"""
Módulo principal da aplicação.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import base

app = FastAPI()

# Configuração do CORS para aceitar qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos
    allow_headers=["*"],  # Permite todos os headers
)

# Registrar as rotas
app.include_router(base.router)

@app.get("/")
def read_root():
    return {"message": "API rodando com FastAPI"}