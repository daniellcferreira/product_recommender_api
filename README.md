# API de Recomendação de Produtos

[![Python](https://img.shields.io/badge/Python-Backend-blue?style=flat-square&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-teal?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-green?style=flat-square&logo=python)](https://www.uvicorn.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-Validation-orange?style=flat-square&logo=python)](https://docs.pydantic.dev/)

## Descrição

Esta API tem como objetivo fornecer um sistema básico de recomendação de produtos baseado em preferências e histórico de compras.  
Foi construída com FastAPI e organizada de forma modular, visando escalabilidade, leitura clara e manutenção simples.  
O foco do projeto é demonstrar como estruturar uma API RESTful moderna com endpoints bem definidos, documentação automática e uso de boas práticas.

Os dados são armazenados em memória (sem banco de dados) para simplificar testes e aprendizado.  
As respostas são validadas com modelos Pydantic e seguem padrões esperados em aplicações reais.

A interface interativa do Swagger é automaticamente gerada e permite testar todos os endpoints diretamente pelo navegador.

## Funcionalidades

- Registro de usuários com nome
- Listagem de todos os usuários cadastrados
- Registro de produtos com nome, descrição, categoria e lista de tags
- Listagem completa dos produtos disponíveis
- Registro do histórico de compras de um usuário por IDs de produtos
- Consulta de recomendações de produtos para um usuário com base no histórico e em filtros opcionais (categorias e tags)
- Documentação automática gerada via OpenAPI e Swagger
- Separação clara por módulos (`routes`, `models`, `storage`)
- Respostas e requisições fortemente tipadas com Pydantic
- Validações para garantir consistência de dados
- Tratamento de erros comuns com HTTPException

## Tecnologias abordadas

- **Python 3.11**  
  Linguagem de programação principal, com suporte a tipagem estática e orientada a objetos.

- **FastAPI**  
  Framework web moderno e rápido para criação de APIs com base em Python 3.6+ e tipo hints.  
  Utiliza Starlette como núcleo assíncrono e Pydantic para validação de dados.

- **Uvicorn**  
  Servidor ASGI leve e rápido usado para rodar a aplicação localmente.

- **Pydantic**  
  Biblioteca para criação de modelos de dados com validação e parsing automáticos.  
  Fundamental para garantir a integridade dos dados da API.

- **Swagger UI / OpenAPI**  
  Interface gráfica gerada automaticamente para testes e visualização da documentação da API.  
  Permite realizar requisições diretamente pelo navegador.

- **Tipagem com `BaseModel` e Annotations (`List`, `Optional`, etc.)**  
  Toda estrutura da API é fortemente tipada, facilitando o uso de ferramentas de validação estática e lint.

- **Boas práticas de modularização**  
  Estrutura separada por arquivos de rotas, modelos e camada de armazenamento, respeitando os princípios da organização RESTful.

O projeto é ideal para fins educacionais, prototipagem de sistemas de recomendação simples e aprendizado de FastAPI com código limpo.
