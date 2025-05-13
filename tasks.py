from crewai import Task

def buscar_receita(agent, cozinha):
    return Task(
        description=f"Busque uma receita típica da cozinha: {cozinha}",
        agent=agent,
        expected_output="Nome da receita, ingredientes, modo de preparo, link com imagem",
        output_file="output/receita.txt",
        verbose=True
    )

def buscar_filme(agent, pais):
    return Task(
        description=f"Indique um filme famoso originado no país: {pais}",
        agent=agent,
        expected_output="Título, sinopse e por que representa bem o país",
        output_file="output/filme.txt",
        verbose=True
    )

def buscar_curiosidades(agent, pais):
    return Task(
        description=f"Liste curiosidades interessantes e culturais sobre o país: {pais}",
        agent=agent,
        expected_output="3 a 5 curiosidades culturais, históricas ou sociais",
        output_file="output/curiosidades.txt",
        verbose=True
    )

def criar_historia(agent, contexto):
    return Task(
        description="Utilize a receita, o filme e as curiosidades para criar uma história criativa que se passe nesse país.",
        agent=agent,
        expected_output="Uma narrativa envolvente que conecte os elementos culturais pesquisados",
        output_file="output/narrativa_final.txt",
        context=contexto,
        verbose=True
    )
