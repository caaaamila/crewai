# 🚀 CrewAI + APIs

Este projeto utiliza agentes inteligentes baseados na **CrewAI** integrados com APIs públicas para fornecer informações culturais sobre qualquer país do mundo. Com base no nome de um país, o sistema retorna:

- 🎬 Um **filme popular** típico do país
- 🍽️ Um **prato tradicional** da culinária local
- 🌍 Informações gerais do país, como nome oficial, idioma e população

---

## 📡 APIs Utilizadas

### 🍽️ [TheMealDB](https://www.themealdb.com/)
API gratuita com receitas e pratos tradicionais de diversos países.

- **Exemplo de requisição:**
  ```
  https://www.themealdb.com/api/json/v1/1/filter.php?a=Mexican
  ```

---

### 🎬 [The Movie Database (TMDb)](https://www.themoviedb.org/documentation/api)
API para descobrir filmes de acordo com o país de origem.

- **Exemplo de requisição:**
  ```
  https://api.themoviedb.org/3/discover/movie?api_key=SUA_CHAVE&with_origin_country=BR&sort_by=popularity.desc
  ```
- ⚠️ Requer chave de API (gratuita mediante cadastro).

---

### 🌍 [REST Countries](https://restcountries.com/)
API com informações oficiais sobre países do mundo.

- **Exemplo de requisição:**
  ```
  https://restcountries.com/v3.1/alpha/BR
  ```

---
## 🛠️ Pré-requisitos

- Python 3.12
- [Conta na Groq](https://console.groq.com/)

  # Verifique sua versão do Python

  python --version

## 📥 Instalação

### 1\. Clone o repositório

    git clone https://github.com/caaaamila/crewai

### 2\. Configure ambiente virtual

    py -3.12 -m venv venv

    # Windows:

    venv\Scripts\activate

    # Mac/Linux:

    source venv/bin/activate

### 3\. Instale dependências

    pip install -r requirements.txt

### 4\. Configure sua API key

    echo "GROQ_API_KEY=sua_chave_aqui" > .env
    echo "TMDB_API_KEY=sua_chave_aqui" > .env

## 🖥️ Como Usar

Execute o sistema:

    python main.py

