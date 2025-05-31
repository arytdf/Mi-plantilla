def infer(query: str):
    """
    Aquí va tu algoritmo de razonamiento.
    Por ahora devolvemos un ejemplo muy simple.
    """
    if "hola" in query.lower():
        return "¡Hola! ¿En qué puedo ayudarte?"
    return "No tengo una respuesta para eso."
