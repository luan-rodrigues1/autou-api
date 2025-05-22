from fastapi import APIRouter, Body
from app.services.text_processing import preprocess_text
from app.services.email_classifier import process_email

router = APIRouter()

@router.post("/email")
def process_email_route(
    email_subject: str = Body(...),
    email_content: str = Body(...)
):
    processed_subject = preprocess_text(email_subject)
    processed_content = preprocess_text(email_content)
    
    subject_for_classification = f"""
    Original: {processed_subject['original']}
    Sem stop words: {processed_subject['without_stop_words']}
    Stemmed: {processed_subject['stemmed']}
    Lemmatized: {processed_subject['lemmatized']}
    """
    
    content_for_classification = f"""
    Original: {processed_content['original']}
    Sem stop words: {processed_content['without_stop_words']}
    Stemmed: {processed_content['stemmed']}
    Lemmatized: {processed_content['lemmatized']}
    """
    
    classification_result = process_email(
        subject=subject_for_classification,
        content=content_for_classification
    )
    
    return {
        "category": classification_result["classification"],
        "suggested_response": classification_result["suggested_response"]
    }