from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(base.router)

@app.get("/")
def read_root():
    return {"message": "API rodando com FastAPI"}