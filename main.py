from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import ProdutoDB
from schemas import ProdutoCreate, ProdutoResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from models import EventoDB
from schemas import EventoCreate, EventoResponse



Base.metadata.create_all(bind=engine) # cria as tabelas, se ainda não existirem
app = FastAPI()

app.add_middleware(
 CORSMiddleware,
 allow_origins=['*'],
 # em produção, restringir para o domínio real do front-end
 allow_methods=['*'],
 allow_headers=['*'],
)


@app.get('/produtos', response_model=list[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(ProdutoDB).all()

@app.post('/produtos', response_model=ProdutoResponse, status_code=201)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    novo_produto = ProdutoDB(**produto.dict())
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

# GET /produtos/{id} -> retorna um único produto pelo id
@app.get('/produtos/{produto_id}', response_model=ProdutoResponse)
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    produto      =        db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    return produto

 # DELETE /produtos/{id} -> remove um produto do banco de dados
@app.delete('/produtos/{produto_id}', status_code=204)
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id ==
produto_id).first()
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    db.delete(produto)
    db.commit ()

    # GET /produtos/{id} -> consulta um produto pelo id no banco
@app.get('/produtos/{produto_id}', response_model=ProdutoResponse)
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id ==produto_id).first()
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    return produto


# DELETE /produtos/{id} -> remove um produto do banco
@app.delete('/produtos/{produto_id}', status_code=204)
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
    if produto is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    db.delete(produto)
    db.commit()

   # PUT /produtos/{id} -> atualiza um produto existente no banco
@app.put('/produtos/{produto_id}', response_model=ProdutoResponse)
def atualizar_produto(produto_id: int, dados: ProdutoCreate, db:
Session = Depends(get_db)):
 produto = db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
 if produto is None:
    raise HTTPException(status_code=404, detail='Produto não encontrado')
    produto.nome = dados.nome
    produto.preco = dados.preco
    produto.quantidade = dados.quantidade
    db.commit()
    db.refresh(produto)
    return produto










 @app.get('/evento', response_model=list[EventoResponse])
 def listar_evento(db: Session = Depends(get_db)):
    return db.query(EventoDB).all()

@app.post('/evento', response_model=EventoResponse, status_code=201)
def criar_evento(evento: EventoCreate, db: Session = Depends(get_db)):
    novo_evento = EventoDB(**evento.dict())
    db.add(novo_evento)
    db.commit()
    db.refresh(novo_evento)
    return novo_evento

# GET /produtos/{id} -> retorna um único produto pelo id
@app.get('/evento/{evento_id}', response_model=EventoResponse)
def obter_evento(evento_id: int, db: Session = Depends(get_db)):
    evento      =        db.query(EventoDB).filter(EventoDB.id == evento_id).first()
    if evento is None:
        raise HTTPException(status_code=404, detail='Evento não encontrado')
    return evento

 # DELETE /produtos/{id} -> remove um produto do banco de dados
@app.delete('/evento/{evento_id}', status_code=204)
def remover_evento(evento_id: int, db: Session = Depends(get_db)):
    evento = db.query(EventoDB).filter(EventoDB.id == evento_id).first()
    if evento is None:
        raise HTTPException(status_code=404, detail='Evento não encontrado')
    db.delete(evento)
    db.commit ()

    # GET /produtos/{id} -> consulta um produto pelo id no banco
@app.get('/evento/{evento_id}', response_model=EventoResponse)
def obter_evento(evento_id: int, db: Session = Depends(get_db)):
    evento = db.query(EventoDB).filter(EventoDB.id ==evento_id).first()
    if evento is None:
        raise HTTPException(status_code=404, detail='Evento não encontrado')
    return evento


# DELETE /produtos/{id} -> remove um produto do banco
@app.delete('/evento/{evento_id}', status_code=204)
def remover_evento(evento_id: int, db: Session = Depends(get_db)):
    evento = db.query(EventoDB).filter(EventoDB.id == evento_id).first()
    if evento is None:
        raise HTTPException(status_code=404, detail='Evento não encontrado')
    db.delete(evento)
    db.commit()

   # PUT /produtos/{id} -> atualiza um produto existente no banco
@app.put('/evento/{evento_id}', response_model=EventoResponse)
def atualizar_evento(evento_id: int, dados: EventoCreate, db:
Session = Depends(get_db)):
 evento = db.query(EventoDB).filter(EventoDB.id == evento_id).first()
 if evento is None:
        raise HTTPException(status_code=404, detail='Evento não encontrado')
 evento.nome = dados.nome
 evento.local = dados.local
 evento.data_evento = dados.data_evento
 evento.capacidade = evento.capacidade
 db.commit()
 db.refresh(evento)
 return evento

