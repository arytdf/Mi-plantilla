from fastapi import FastAPI
from .expert_system import infer

app = FastAPI(title="{{ cookiecutter.project_name }}")

@app.get("/infer")
def run_inference(q: str):
    """
    Endpoint para consultar al sistema experto.
    Parámetro:
    - q: pregunta o dato de entrada
    """
    result = infer(q)
    return {"input": q, "output": result}

