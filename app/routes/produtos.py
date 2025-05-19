from fastapi import APIRouter
from typing import List
from app.models import Produto, CriarProduto
from app.storage import adicionar_produto, listar_produtos

router = APIRouter()  # Cria um roteador FastAPI

# Função para criar um produto e retorna o objeto criado com id
@router.post("/", response_model=Produto, summary="Cria um novo produto")  # Define a rota para criar um produto
def criar_produto(produto: CriarProduto):
  novo_produto = adicionar_produto(produto.model_dump()) 
  return novo_produto

# Função para listar todos os produtos cadastrados
@router.get("/", response_model=List[Produto], summary="Lista todos os produtos")  # Define a rota para listar produtos
def listar_produtos_route():
  return listar_produtos()