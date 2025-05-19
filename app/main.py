from fastapi import FastAPI
from app.routes import usuarios, produtos, recomendacoes

app = FastAPI(
  title="API de Recomendação de Produtos",
  description="API para cadastro de usuários, produtos e recomendações baseadas no histórico e preferências.",
  version="1.0.0"
)

# Inclui as rotas de usuários, produtos e recomendações
app.include_router(usuarios.router, prefix="/usuarios", tags=["usuarios"])
app.include_router(produtos.router, prefix="/produtos", tags=["produtos"])
app.include_router(recomendacoes.router, prefix="/recomendacoes", tags=["recomendacoes"])

# Rota raiz da API
@app.get("/", summary=" Bem-vindo à API de Recomendação de Produtos")
def read_root():
    return {"message": "Bem-vindo à API de Recomendação de Produtos!"}