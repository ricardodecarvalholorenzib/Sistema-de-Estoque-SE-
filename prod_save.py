# prod_save.py

import json
import os

from util.sessao import obter_usuario

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_DADOS = os.path.join(BASE_DIR, "dados")
ARQUIVO = os.path.join(PASTA_DADOS, "produtos.json")

def carregar_produtos():
    # Cria a pasta 'dados' se ela não existir
    if not os.path.exists(PASTA_DADOS):
        os.makedirs(PASTA_DADOS)

    # Se o arquivo não existir, retorna lista vazia
    if not os.path.exists(ARQUIVO):
        return []

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, Exception):
        return []

def carregar_meus_produtos():

    usuario = obter_usuario()

    produtos = carregar_produtos()

    return [
        produto
        for produto in produtos
        if produto.get("usuario") == usuario
    ]

def salvar_produtos(produtos):
    if not os.path.exists(PASTA_DADOS):
        os.makedirs(PASTA_DADOS)

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)

def produto_existe(nome_produto):
    usuario_atual = obter_usuario()

    produtos = carregar_produtos()
    return any(
        p["usuario"] == usuario_atual and
        p.get("nome_produto", "").lower() == nome_produto.lower()
        for p in produtos
    )

def criar_produto(nome_produto, preco, quantidade):
    if produto_existe(nome_produto):
        return False

    usuario_atual = obter_usuario()

    produtos = carregar_produtos()
    produtos.append({
        "nome_produto": nome_produto,
        "usuario": usuario_atual,
        "preco": preco,
        "quantidade": quantidade
    })

    salvar_produtos(produtos)
    return True