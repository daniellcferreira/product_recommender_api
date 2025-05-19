from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from app.models import HistoricoCompras, Preferencias, Produto
from app.storage import (
  usuario_existe,
  salvar_historico_compras,
  obter_historico_compras,
  obter_produtos_por_ids,
)

router = APIRouter()  # Cria um roteador FastAPI

# Modelo de resposta para mensagens simples
class MensagemResposta(BaseModel):
  mensagem: str

# Função para registrar os ids dos produtos comprados pelo usuário
@router.post(
  "/usuarios/{usuario_id}/historico/",
  response_model=MensagemResposta,
  summary="Registra o histórico de compras do usuário",
)
def adicionar_historico_compras(usuario_id: int, compras: HistoricoCompras):
  if usuario_existe(usuario_id):  # Verifica se o usuário existe
    salvar_historico_compras(usuario_id, compras.Produto_ids)  # Salva o histórico de compras do usuário
    return {"mensagem": "Histórico de compras registrado com sucesso"}  # Retorna uma mensagem de sucesso
  else:
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# Função retorna lista de produtos recomendados baseada no histórico e nas preferências informadas
@router.post(
  "/usuarios/{usuario_id}/recomendacoes/",
  response_model=List[Produto],
  summary="Obtém recomendações de produtos para o usuário",
)
def recomndar_produtos(usuario_id: int, preferencias: Preferencias):
  if not usuario_existe(usuario_id):  # Verifica se o usuário existe
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

  historico_ids = obter_historico_compras(usuario_id)  # Obtém o histórico de compras do usuário
  if not historico_ids:  # Verifica se o histórico de compras está vazio
    return []  # Retorna uma lista vazia se o histórico de compras estiver vazio

  produtos_recomendados = obter_produtos_por_ids(historico_ids)  # Filtra os produtos do histórico

  # Aplicar filtros com base nas preferências
  if preferencias.categorias:
    produtos_recomendados = [
      p for p in produtos_recomendados if p.categoria in preferencias.categorias
    ]

  if preferencias.tags:
    produtos_recomendados = [
      p for p in produtos_recomendados if any(tag in preferencias.tags for tag in p.tags)
    ]

  return produtos_recomendados  # Retorna a lista final de produtos recomendados
