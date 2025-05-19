from fastapi import APIRouter
from typing import List
from pydantic import BaseModel
from app.models import Usuario
from app.storage import adicionar_usuario, listar_usuarios_storage

router = APIRouter()  # Cria um roteador FastAPI

# Classe de entrada para criação do usuário
class UsuarioInput(BaseModel):
  nome: str

# Função para criar um usuário com o nome fornecido
@router.post("/", response_model=Usuario, summary="Cria um novo usuário")  # Define a rota para criar um usuário
def criar_usuario(usuario: UsuarioInput):
  novo_usuario = adicionar_usuario(usuario.nome)
  return novo_usuario

# Função para listar todos os usuários cadastrados
@router.get("/", response_model=List[Usuario], summary="Lista todos os usuários")  # Define a rota para listar usuários
def obter_usuarios():
  return listar_usuarios_storage()
