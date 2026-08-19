from sqlalchemy import Column, Integer, String, Float
from database import Base
class ProdutoDB(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)


class EventoDB(Base):
    __tablename__ = 'eventos'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    local = Column(String(100), nullable=False)
    data_evento = Column(Float, nullable=False)
    capacidade = Column(Integer, nullable=False)
