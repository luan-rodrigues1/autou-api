"""
Módulo para classificação de emails e sugestão de respostas usando OpenAI.
Implementa funções para categorizar emails e gerar respostas automáticas.
"""

import os
from openai import OpenAI
from typing import Dict, Tuple
from .text_processing import preprocess_text
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa o cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Templates para o prompt de classificação
CLASSIFICATION_PROMPT = """
Analise o seguinte email e classifique-o em uma das categorias abaixo.
O texto foi processado usando diferentes técnicas de NLP:

1. Original: Texto exatamente como foi recebido
2. Sem stop words: Removidas palavras comuns que não agregam significado
3. Stemmed: Palavras reduzidas à sua raiz
4. Lemmatized: Palavras convertidas à sua forma base

Use estas diferentes versões para fazer uma classificação mais precisa, considerando:
- O contexto completo do texto original
- As palavras-chave sem stop words
- Os padrões de palavras nas versões stemmed e lemmatized

Categorias:
- PRODUTIVO: Emails que requerem uma ação ou resposta específica (ex.: solicitações de suporte técnico, atualização sobre casos em aberto, dúvidas sobre o sistema)
- IMPRODUTIVO: Emails que não necessitam de uma ação imediata (ex.: mensagens de felicitações, agradecimentos)

Email:
Assunto: {subject}
Conteúdo: {content}

Responda APENAS com a categoria (PRODUTIVO ou IMPRODUTIVO).
"""

# Templates para o prompt de sugestão de resposta
RESPONSE_PROMPT = """
Com base na classificação e no conteúdo do email, sugira uma resposta profissional e adequada.
Forneça o assunto e o conteúdo separadamente.

Classificação: {classification}

Email Original:
Assunto: {subject}
Conteúdo: {content}

Forneça a resposta no seguinte formato:
ASSUNTO: [sugestão do assunto]
CONTEÚDO: [sugestão do conteúdo]

O conteúdo deve ser uma resposta profissional e adequada ao contexto.
"""

def classify_email(subject: str, content: str) -> str:
    """
    Classifica o email usando a API da OpenAI.
    
    Args:
        subject (str): Assunto do email (incluindo diferentes processamentos)
        content (str): Conteúdo do email (incluindo diferentes processamentos)
        
    Returns:
        str: Classificação do email (PRODUTIVO ou IMPRODUTIVO)
    """
    # Prepara o prompt com o assunto e conteúdo do email
    prompt = CLASSIFICATION_PROMPT.format(
        subject=subject,
        content=content
    )
    
    # Faz a chamada para a API da OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Modelo mais econômico e compatível
        messages=[
            {"role": "system", "content": "Você é um assistente especializado em classificação de emails."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,  # Temperatura muito baixa para respostas mais consistentes
        max_tokens=10  # Reduzido pois só precisamos da categoria
    )
    
    return response.choices[0].message.content.strip()

def suggest_response(subject: str, content: str, classification: str) -> Dict[str, str]:
    """
    Sugere uma resposta automática baseada na classificação do email.
    
    Args:
        subject (str): Assunto do email
        content (str): Conteúdo do email
        classification (str): Classificação do email
        
    Returns:
        Dict[str, str]: Dicionário com sugestão de assunto e conteúdo
    """
    # Prepara o prompt com todas as informações necessárias
    prompt = RESPONSE_PROMPT.format(
        classification=classification,
        subject=subject,
        content=content
    )
    
    # Faz a chamada para a API da OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Modelo mais econômico e compatível
        messages=[
            {"role": "system", "content": "Você é um assistente especializado em redação de emails profissionais."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500  # Aumentado para garantir espaço suficiente para o conteúdo
    )
    
    # Processa a resposta para separar assunto e conteúdo
    response_text = response.choices[0].message.content.strip()
    
    # Extrai assunto e conteúdo
    suggested_subject = ""
    suggested_content = ""
    
    # Divide o texto em linhas e processa
    lines = response_text.split('\n')
    content_started = False
    content_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if line.startswith('ASSUNTO:'):
            suggested_subject = line.replace('ASSUNTO:', '').strip()
        elif line.startswith('CONTEÚDO:'):
            content_started = True
            content_lines.append(line.replace('CONTEÚDO:', '').strip())
        elif content_started:
            content_lines.append(line)
    
    # Junta todas as linhas do conteúdo
    suggested_content = '\n'.join(content_lines).strip()
    
    # Verifica se o conteúdo está vazio e gera uma resposta padrão se necessário
    if not suggested_content:
        suggested_content = "Prezado(a),\n\nAgradeço seu contato. Estou analisando sua solicitação e retornarei em breve com mais informações.\n\nAtenciosamente,\n[Seu Nome]"
    
    return {
        "subject": suggested_subject or f"Re: {subject}",
        "content": suggested_content
    }

def process_email(subject: str, content: str) -> Dict:
    """
    Processa o email completo: classifica e sugere uma resposta.
    
    Args:
        subject (str): Assunto do email
        content (str): Conteúdo do email
        
    Returns:
        Dict: Dicionário com os resultados do processamento
    """
    # Classifica o email
    classification = classify_email(subject, content)
    
    # Sugere uma resposta
    suggested_response = suggest_response(
        subject=subject,
        content=content,
        classification=classification
    )
    
    return {
        "classification": classification,
        "suggested_response": suggested_response
    } 