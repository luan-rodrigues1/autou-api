# 🧠 NLP API Project (FastAPI)

Este projeto é uma API básica desenvolvida com **FastAPI**, com estrutura preparada para ser expandida com funcionalidades de **Processamento de Linguagem Natural (NLP)** e integração com APIs de Inteligência Artificial (como OpenAI ou Hugging Face).

---

## 📁 Estrutura do Projeto

nlp_api_project/
├── app/
│ ├── main.py # Ponto de entrada da aplicação
│ └── routes/
│ └── base.py # Rotas definidas
├── requirements.txt # Lista de dependências
├── README.md # Este arquivo
├── .gitignore # Arquivos/pastas ignoradas pelo Git
└── venv/ # Ambiente virtual (não versionado)

---

## 🚀 Como rodar o projeto localmente

### 1. Clone o repositório

````bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo

---

### 2. Crie o ambiente virtual

```bash
python -m venv venv

---

### 3. Ative o ambiente virtual

No Linux/macOS ou WSL:
```bash
source venv/bin/activate

No Windows (CMD):
```bash
venv\Scripts\activate

No Windows (PowerShell):
```bash
.\venv\Scripts\Activate.ps1

---

### 4. Instale as dependências

```bash
pip install -r requirements.txt

---

### 5. Rode a aplicação

```bash
uvicorn app.main:app --reload

A API estará acessível em: http://localhost:8000

---

````
