from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def hello():
    return {"message": "Olá, Luan! Sua API está funcionando!"}