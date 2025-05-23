# 🧠 Case Prático AutoU - Luan Rodrigues Carlos

Este projeto é uma API desenvolvida para o Case Prático AutoU, com o objetivo de criar uma aplicação que utiliza inteligência artificial para automação do processamento de emails.

[📚 Ver documentação da API](#-documentação-da-api)

Link do deploy da aplicação: [https://autou-front-77008956635.southamerica-east1.run.app](https://autou-api-77008956635.southamerica-east1.run.app)

Informações de Contato:

Email: rodrigues.luan20@gmail.com

Telefone: (21) 98152-8060

---

## 🚀 Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

---

### 2. Crie o ambiente virtual

```bash
python -m venv venv
```

---

### 3. Ative o ambiente virtual

No Linux/macOS ou WSL:

```bash
source venv/bin/activate
```

No Windows (CMD):

```bash
venv\Scripts\activate
```

No Windows (PowerShell):

```bash
.\venv\Scripts\Activate.ps1
```

---

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 5. Configure as variáveis de ambiente

1. Copie o arquivo `.env.example` para `.env`:

```bash
cp .env.example .env
```

2. Edite o arquivo `.env` e adicione sua chave da API da OpenAI:

```bash
OPENAI_API_KEY=sua_chave_aqui
```

> ⚠️ **Importante**: Você precisa ter uma chave de API válida da OpenAI para que a aplicação funcione corretamente.

---

### 6. Rode a aplicação

```bash
uvicorn app.main:app --reload
```

A API estará acessível em: http://localhost:8000

---

## 📚 Documentação da API

### Endpoint: `/email`

Este endpoint processa emails e retorna uma classificação e sugestão de resposta.

#### Método: POST

#### Corpo da Requisição (JSON):

```json
{
  "email_subject": "string",
  "email_content": "string"
}
```

#### Resposta:

```json
{
  "category": "PRODUTIVO | IMPRODUTIVO",
  "suggested_response": {
    "subject": "string",
    "content": "string"
  }
}
```

#### Descrição:

- **email_subject**: Assunto do email
- **email_content**: Conteúdo do email
- **category**: Classificação do email (PRODUTIVO ou IMPRODUTIVO)
- **suggested_response**: Sugestão de resposta contendo:
  - **subject**: Sugestão de assunto para a resposta
  - **content**: Sugestão de conteúdo para a resposta

#### Exemplo de Uso:

```bash
curl -X POST "http://localhost:8000/email" \
     -H "Content-Type: application/json" \
     -d '{
           "email_subject": "Problema com o sistema",
           "email_content": "Olá, estou tendo dificuldades para acessar o sistema. Poderia me ajudar?"
         }'
```

#### Resposta de Exemplo:

```json
{
  "category": "PRODUTIVO",
  "suggested_response": {
    "subject": "Re: Problema com o sistema",
    "content": "Prezado(a),\n\nAgradeço seu contato. Estou analisando sua solicitação e retornarei em breve com mais informações.\n\nAtenciosamente,\n[Seu Nome]"
  }
}
```
