from typing import List
from app.models import Produto, Usuario

# Armazenamento em memória (substituir por um DB funturamente)
_produtos: List[Produto] = []
_usuarios: List[Usuario] = []
_historico_compras: dict[int, List[int]] = {}  # Mapeia usuário_id para lista de produto_ids

# Contadores para gerar IDs únicos
_contador_produto = 1
_contador_usuario = 1

# Função cria um produto com id e adiciona na lista de produtos
def adicionar_produto(produto_data: dict) -> Produto:       
  global _contador_produto                                  
  produto = Produto(id=_contador_produto, **produto_data)   
  _produtos.append(produto)                                 
  _contador_produto += 1                                                       
  return produto                                            

# Função retorna todos os produtos cadastrados
def listar_produtos() -> List[Produto]: 
  return _produtos.copy()  # Retorna uma cópia da lista de produtos

# Função cria um usuário com id e adiciona na lista de usuários
def adicionar_usuario(nome: str) -> Usuario:          
  global _contador_usuario                            
  usuario = Usuario(id=_contador_usuario, nome=nome)
  _usuarios.append(usuario)
  _contador_usuario += 1
  return usuario

# Função retorna todos os usuários cadastrados
def listar_usuarios_storage() -> List[Usuario]: 
  return _usuarios.copy()  # Retorna uma cópia da lista de usuários

# Função verifica se o usuário existe
def usuario_existe(usuario_id: int) -> bool:
  return any(usuario.id == usuario_id for usuario in _usuarios)  # Verifica se o usuário existe na lista de usuários

# Função salva/atualiza o histórico de compras do usuário
def salvar_historico_compras(usuario_id: int, produto_ids: List[int]) -> None:
  if usuario_existe(usuario_id):  # Verifica se o usuário existe
    _historico_compras[usuario_id] = produto_ids  # Atualiza o histórico de compras do usuário
  else:
    raise ValueError("Usuário não encontrado")  # Lança um erro se o usuário não for encontrado
  
# Função retorna lista de ids de produtos comprados pelo usuário
def obter_historico_compras(usuario_id: int) -> List[int]:
  if usuario_existe(usuario_id):  # Verifica se o usuário existe
    return _historico_compras.get(usuario_id, [])  # Retorna o histórico de compras do usuário ou uma lista vazia se não houver histórico
  else:
    raise ValueError("Usuário não encontrado")  # Lança um erro se o usuário não for encontrado
  
# Função retorna a lista de produtos correspondentes aos ids fornecidos
def obter_produtos_por_ids(ids: List[int]) -> List[Produto]:
  return [produto for produto in _produtos if produto.id in ids]  # Retorna a lista de produtos correspondentes aos ids fornecidos

