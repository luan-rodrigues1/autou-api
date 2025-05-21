"""
Pacote de serviços para processamento e classificação de emails.
"""

from .text_processing import preprocess_text
from .email_classifier import process_email, classify_email, suggest_response

__all__ = [
    'preprocess_text',
    'process_email',
    'classify_email',
    'suggest_response'
] 