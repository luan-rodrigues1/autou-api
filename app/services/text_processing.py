"""
Módulo para processamento de texto usando técnicas de NLP.
Implementa funções para remoção de stop words, stemming e lemmatização.
"""

# Lista de stop words em português
STOP_WORDS = {
    'a', 'o', 'as', 'os', 'um', 'uma', 'uns', 'umas', 'e', 'é', 'é', 'está', 'estou',
    'estamos', 'estão', 'estive', 'esteve', 'estivemos', 'estiveram', 'estava',
    'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja', 'estejamos',
    'estejam', 'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos',
    'estiverem', 'hei', 'há', 'havemos', 'hão', 'houve', 'houvemos', 'houveram',
    'houvera', 'houvéramos', 'haja', 'hajamos', 'hajam', 'houvesse', 'houvéssemos',
    'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 'houverá', 'houveremos',
    'houverão', 'houveria', 'houveríamos', 'houveriam', 'sou', 'somos', 'são', 'era',
    'éramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja',
    'sejamos', 'sejam', 'fosse', 'fôssemos', 'fossem', 'for', 'formos', 'forem',
    'serei', 'será', 'seremos', 'serão', 'seria', 'seríamos', 'seriam', 'tenho',
    'tem', 'temos', 'têm', 'tinha', 'tínhamos', 'tinham', 'tive', 'teve', 'tivemos',
    'tiveram', 'tivera', 'tivéramos', 'tenha', 'tenhamos', 'tenham', 'tivesse',
    'tivéssemos', 'tivessem', 'tiver', 'tivermos', 'tiverem', 'terei', 'terá',
    'teremos', 'terão', 'teria', 'teríamos', 'teriam'
}

def remove_stop_words(text: str) -> str:
    """
    Remove stop words do texto.
    """
    # Converte o texto para minúsculas e divide em palavras
    words = text.lower().split()
    
    # Filtra as palavras que não são stop words
    filtered_words = [word for word in words if word not in STOP_WORDS]
    
    # Junta as palavras novamente em um texto
    return ' '.join(filtered_words)

def stem_word(word: str) -> str:
    """
    Implementa um algoritmo simples de stemming para português.
    Remove sufixos comuns das palavras.
    """
    # Lista de sufixos comuns em português
    sufixos = ['ar', 'er', 'ir', 'or', 'al', 'el', 'il', 'ol', 'ul', 'ão', 'ões',
               'mente', 'ção', 'ções', 'dor', 'dora', 'dores', 'doras', 'ista',
               'istas', 'oso', 'osa', 'osos', 'osas', 'ível', 'ível', 'íveis',
               'ável', 'ável', 'áveis']
    
    # Tenta remover cada sufixo
    for sufixo in sufixos:
        if word.endswith(sufixo):
            return word[:-len(sufixo)]
    
    return word

def stem_text(text: str) -> str:
    """
    Aplica stemming em todas as palavras do texto.
    """
    words = text.split()
    stemmed_words = [stem_word(word) for word in words]
    return ' '.join(stemmed_words)

def lemmatize_word(word: str) -> str:
    """
    Implementa um algoritmo simples de lemmatização para português.
    Tenta converter a palavra para sua forma base.
    """
    # Dicionário de exceções para lemmatização
    exceptions = {
        'estou': 'estar',
        'está': 'estar',
        'estamos': 'estar',
        'estão': 'estar',
        'sou': 'ser',
        'somos': 'ser',
        'são': 'ser',
        'tenho': 'ter',
        'tem': 'ter',
        'temos': 'ter',
        'têm': 'ter',
        'fui': 'ir',
        'foi': 'ir',
        'fomos': 'ir',
        'foram': 'ir'
    }
    
    # Verifica se a palavra está no dicionário de exceções
    if word in exceptions:
        return exceptions[word]
    
    # Se não estiver nas exceções, aplica stemming
    return stem_word(word)

def lemmatize_text(text: str) -> str:
    """
    Aplica lemmatização em todas as palavras do texto.
    """
    words = text.split()
    lemmatized_words = [lemmatize_word(word) for word in words]
    return ' '.join(lemmatized_words)

def preprocess_text(text: str) -> dict:
    """
    Aplica todas as técnicas de pré-processamento no texto.
    """
    # Remove stop words
    text_without_stop_words = remove_stop_words(text)
    
    # Aplica stemming
    stemmed_text = stem_text(text_without_stop_words)
    
    # Aplica lemmatização
    lemmatized_text = lemmatize_text(text_without_stop_words)
    
    return {
        'original': text,
        'without_stop_words': text_without_stop_words,
        'stemmed': stemmed_text,
        'lemmatized': lemmatized_text
    } 