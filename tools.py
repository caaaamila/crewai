import requests
from crewai.tools import BaseTool
from typing import Optional
import os
from util import *

class GetMealTool(BaseTool):
    name: str = "Receitas Típicas"
    description: str = "Busca uma receita típica de um país usando a API TheMealDB."

    def _run(self, country: str) -> str:
        url = f"https://www.themealdb.com/api/json/v1/1/filter.php?a={country}"
        response = requests.get(url)
        data = response.json()
        meals = data.get("meals")

        if not meals:
            return f"Nenhuma receita encontrada para {country}."

        meal = meals[0]
        return f"Prato típico: {meal['strMeal']}\nLink da imagem: {meal['strMealThumb']}"

class GetMovieTool(BaseTool):
    name: str = "Filmes por País"
    description: str = "Busca um filme típico de um país usando a API do TMDB."

    def _run(self, country: str) -> str:
        api_key = os.getenv("TMDB_API_KEY")

        code = obter_codigo_pais(country)

        url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_origin_country={code}&sort_by=popularity.desc"
        response = requests.get(url)
        data = response.json()
        movies = data.get("results", [])

        if not movies:
            return f"Nenhum filme encontrado para {country}."

        movie = movies[0]
        return f"Filme: {movie['title']}\nResumo: {movie.get('overview', 'Sem resumo')}\nNota: {movie['vote_average']}"

class GetCountryFactsTool(BaseTool):
    name: str = "Fatos do País"
    description: str = "Busca curiosidades e dados sobre um país com a API RESTCountries."

    def _run(self, country: str) -> str:
        code = obter_codigo_pais(country)
        url = f"https://restcountries.com/v3.1/alpha/{code}"
        response = requests.get(url)
        data = response.json()

        if isinstance(data, dict) and data.get("status") == 404:
            return f"Não encontrei dados para {country}."

        info = data[0]
        capital = info.get("capital", ["Desconhecida"])[0]
        population = info.get("population", "Desconhecida")
        region = info.get("region", "Desconhecida")
        languages = ", ".join(info.get("languages", {}).values())

        return (
            f"País: {country}\n"
            f"Capital: {capital}\n"
            f"População: {population}\n"
            f"Região: {region}\n"
            f"Idiomas: {languages}"
        )
    
