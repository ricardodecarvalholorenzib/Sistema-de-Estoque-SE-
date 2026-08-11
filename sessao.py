# sessao.py

import json
import os

usuario_atual = None

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARQUIVO = os.path.join(BASE_DIR, "dados", "sessao.json")

def salvar_sessao(usuario):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(
            {"usuario": usuario},
            arquivo,
            indent=4
        )

def iniciar_sessao(usuario):
    global usuario_atual
    usuario_atual = usuario
    salvar_sessao(usuario)

def carregar_sessao():
    global usuario_atual

    if not os.path.exists(ARQUIVO):
        return None

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        usuario_atual = dados.get("usuario")

        return usuario_atual

    except (json.JSONDecodeError, OSError):
        return None

def encerrar_sessao():
    global usuario_atual

    usuario_atual = None

    if os.path.exists(ARQUIVO):
        os.remove(ARQUIVO)

def obter_usuario():
    return usuario_atual


def encerrar_sessao():
    global usuario_atual
    usuario_atual = None