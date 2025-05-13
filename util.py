import pycountry

def obter_cozinha_pais(pais: str) -> str:
    pais = pais.strip().lower()

    cozinhas = {
        "brazil": "brazilian",
        "mexico": "mexican",
        "japan": "japanese",
        "china": "chinese",
        "france": "french",
        "italy": "italian",
        "india": "indian",
        "spain": "spanish",
        "thailand": "thai",
        "germany": "german",
        "vietnam": "vietnamese",
        "south korea": "korean",
        "greece": "greek",
        "turkey": "turkish",
        "morocco": "moroccan",
        "argentina": "argentine",
        "russia": "russian",
        "united states": "american",
        "england": "british",
        "uk": "british",
        "united kingdom": "british",
        "usa": "american"
    }

    return cozinhas.get(pais, "international")

def obter_codigo_pais(nome_pais: str) -> str:
    try:
        pais = pycountry.countries.lookup(nome_pais)
        return pais.alpha_2
    except LookupError:
        return "US"