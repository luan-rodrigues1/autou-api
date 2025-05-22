from fastapi import APIRouter, Body
from app.services.text_processing import preprocess_text
from app.services.email_classifier import process_email

router = APIRouter()

@router.get("/hello")
def hello():
    return {"message": "Olá, Luan! Sua API está funcionando!"}

@router.post("/email")
def process_email_route(
    email_subject: str = Body(...),
    email_content: str = Body(...)
):
    return {
	"category": "IMPRODUTIVO",
	"suggested_response": {
		"subject": "Agradecimento pelo feedback positivo",
		"content": "Prezado [Nome do Remetente],\nAgradecemos imensamente pelo seu feedback positivo e por reconhecer o excelente atendimento prestado pela nossa equipe. Ficamos felizes em saber que conseguimos resolver o seu problema de forma eficiente e profissional. Com certeza, continuaremos empenhados em oferecer um serviço de qualidade e atendimento excepcional.\nEstamos à disposição para qualquer outra necessidade que possa surgir. Mais uma vez, agradecemos pela confiança em nosso trabalho.\nAtenciosamente,\n[Sua Assinatura]\n[Sua Posição na Empresa]"
        }
    }
    # Processa o texto (NLP)
    # processed_subject = preprocess_text(email_subject)
    # processed_content = preprocess_text(email_content)
    
    # # Combina os diferentes processamentos para melhorar a classificação
    # subject_for_classification = f"""
    # Original: {processed_subject['original']}
    # Sem stop words: {processed_subject['without_stop_words']}
    # Stemmed: {processed_subject['stemmed']}
    # Lemmatized: {processed_subject['lemmatized']}
    # """
    
    # content_for_classification = f"""
    # Original: {processed_content['original']}
    # Sem stop words: {processed_content['without_stop_words']}
    # Stemmed: {processed_content['stemmed']}
    # Lemmatized: {processed_content['lemmatized']}
    # """
    
    # # Classifica o email e sugere resposta usando todos os processamentos
    # classification_result = process_email(
    #     subject=subject_for_classification,
    #     content=content_for_classification
    # )
    
    # return {
    #     "category": classification_result["classification"],
    #     "suggested_response": classification_result["suggested_response"]
    # }