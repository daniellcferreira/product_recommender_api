# API de Recomendação de Produtos

[![Python](https://img.shields.io/badge/Python-Backend-blue?style=flat-square&logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-teal?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-green?style=flat-square&logo=python)](https://www.uvicorn.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-Validation-orange?style=flat-square&logo=python)](https://docs.pydantic.dev/)

## Descrição

Esta API REST permite o cadastro de usuários e produtos, o registro do histórico de compras e o fornecimento de recomendações personalizadas com base em preferências e comportamento do usuário. Foi desenvolvida com FastAPI, utilizando armazenamento em memória para fins didáticos e prototipagem.

## Funcionalidades

- Cadastro e listagem de usuários
- Cadastro e listagem de produtos
- Registro do histórico de compras de cada usuário
- Geração de recomendações personalizadas por categorias e tags
- Interface de testes via Swagger UI

## Tecnologias abordadas

- **Python 3.11** como linguagem principal
- **FastAPI** para criação da API com tipagem robusta e documentação automática
- **Uvicorn** como servidor ASGI de alto desempenho
- **Pydantic** para definição e validação de modelos de dados
