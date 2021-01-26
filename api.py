from fastapi import FastAPI
from pydantic import BaseModel

# iniciar a aplicação
app = FastAPI()

@app.get('/')
def root():
    return {'Olá':'Mundo'}

class Juros(BaseModel):
    id : int
    valor_inicial : float
    valor_5_juros : float

base_dados =  [
    Juros(id=1, valor_inicial=100, valor_5_juros=100 + (100 * 5 / 100)),
    Juros(id=2, valor_inicial=150, valor_5_juros=150 + (150 * 5 / 100)),
    Juros(id=3, valor_inicial=200, valor_5_juros=200 + (200 * 5 / 100))
]

@app.get('/juros')
def get_all():
    return base_dados


@app.get('/teste')
def juros(x=100):
    y = x + (x * 5 / 100)
    return (f'O valor {x} com 5% de juros é {y}')



