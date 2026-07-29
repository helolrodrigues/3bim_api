from fastapi import FastAPI

app = FastAPI(title= "Minha Primeira API")

@app.get('/')
def principal():
     return {'mensagem': 'Minha primeira API em FastAPI'}


@app.get('/sobre')
def principal():
     return {'mensagem': 'Pagina sobre'}
 