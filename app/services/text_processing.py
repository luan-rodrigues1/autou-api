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
    words = text.lower().split()
    
    filtered_words = [word for word in words if word not in STOP_WORDS]
    
    return ' '.join(filtered_words)

def stem_word(word: str) -> str:
    sufixos = ['ar', 'er', 'ir', 'or', 'al', 'el', 'il', 'ol', 'ul', 'ão', 'ões',
               'mente', 'ção', 'ções', 'dor', 'dora', 'dores', 'doras', 'ista',
               'istas', 'oso', 'osa', 'osos', 'osas', 'ível', 'ível', 'íveis',
               'ável', 'ável', 'áveis']
    
    for sufixo in sufixos:
        if word.endswith(sufixo):
            return word[:-len(sufixo)]
    
    return word

def stem_text(text: str) -> str:
    words = text.split()
    stemmed_words = [stem_word(word) for word in words]
    return ' '.join(stemmed_words)

def lemmatize_word(word: str) -> str:
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
    
    if word in exceptions:
        return exceptions[word]
    
    return stem_word(word)

def lemmatize_text(text: str) -> str:
    words = text.split()
    lemmatized_words = [lemmatize_word(word) for word in words]
    return ' '.join(lemmatized_words)

def preprocess_text(text: str) -> dict:
    text_without_stop_words = remove_stop_words(text)
    
    stemmed_text = stem_text(text_without_stop_words)
    
    lemmatized_text = lemmatize_text(text_without_stop_words)
    
    return {
        'original': text,
        'without_stop_words': text_without_stop_words,
        'stemmed': stemmed_text,
        'lemmatized': lemmatized_text
    } 