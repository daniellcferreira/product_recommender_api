from pydantic import BaseModel
from typing import Optional, List

# Modelos de dados para o sistema de recomendação de produtos
# BaseModel é uma classe do Pydantic que fornece validação de dados e serialização

class ProdutoBase(BaseModel):
  nome: str
  categoria: str
  tags: List[str]

class CriarProduto(ProdutoBase):
  pass

class Produto(ProdutoBase):
  id: int

class HistoricoCompras(BaseModel):
  Produto_ids: List[int]

class Preferencias(BaseModel):
  categorias: Optional[List[str]] = None
  tags: Optional[List[str]] = None

class Usuario(BaseModel):
  id: int
  nome: str