from crewai import Crew
from agents import *
from tasks import *
from dotenv import load_dotenv
from util import *

load_dotenv()

# Parâmetro de entrada
pais = "spain"
cozinha  = obter_cozinha_pais(pais)

# Criação dos agentes
chef = create_chef_agent()
cinefilo = create_cinefilo_agent()
historiador = create_historiador_agent()
narrador = create_narrador_agent()

# Criação das tarefas
task_receita = buscar_receita(chef, cozinha)
task_filme = buscar_filme(cinefilo, pais)
task_curiosidade = buscar_curiosidades(historiador, pais)

# O narrador recebe os resultados das 3 tarefas anteriores
task_narrativa = criar_historia(narrador, [task_receita, task_filme, task_curiosidade])

# Configuração da tripulação
crew = Crew(
    agents=[chef, cinefilo, historiador, narrador],
    tasks=[task_receita, task_filme, task_curiosidade, task_narrativa],
    verbose=True
)

# Execução
print("🌍 Luz, Câmera... Sabor! Explorando Culinárias do Mundo")
resultado = crew.kickoff()

# Exibir resultado final
print("\n📘 HISTÓRIA FINAL:")
print(resultado)

