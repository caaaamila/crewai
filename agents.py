from crewai import Agent
from tools import GetMealTool, GetMovieTool, GetCountryFactsTool
from config import get_llm

def create_chef_agent():
    return Agent(
        role="Chef Internacional",
        goal="Escolher uma receita típica do país",
        backstory="Você é um renomado chef global com conhecimento de culinárias regionais.",
        tools=[GetMealTool()],
        verbose=True,
        llm=get_llm()
    )

def create_cinefilo_agent():
    return Agent(
        role="Cinéfilo",
        goal="Selecionar um filme representativo do país",
        backstory="Você é um crítico de cinema especializado em cinema internacional.",
        tools=[GetMovieTool()],
        verbose=True,
        llm=get_llm()
    )

def create_historiador_agent():
    return Agent(
        role="Historiador",
        goal="Fornecer curiosidades e fatos históricos sobre o país",
        backstory="Você é um historiador apaixonado por cultura geral e fatos curiosos sobre países.",
        tools=[GetCountryFactsTool()],
        verbose=True,
        llm=get_llm()
    )

def create_narrador_agent():
    return Agent(
        role="Narrador",
        goal="Unir todas as informações em uma história interessante e envolvente",
        backstory="Você é um contador de histórias que transforma cultura, gastronomia e arte em experiências inesquecíveis.",
        tools=[],
        verbose=True,
        llm=get_llm()
    )
