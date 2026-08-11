import json

from util.seguranca import criptografar_senha

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ARQUIVO = os.path.join(BASE_DIR, "dados", "usuarios.json")


def carregar_usuarios():
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)


def usuario_existe(usuario):
    usuarios = carregar_usuarios()

    return any(
        u["usuario"].lower() == usuario.lower()
        for u in usuarios
    )


def criar_usuario(usuario, senha):

    if usuario_existe(usuario):
        return False

    usuarios = carregar_usuarios()

    usuarios.append({
        "usuario": usuario,
        "senha": criptografar_senha(senha)
    })

    salvar_usuarios(usuarios)

    return True


def autenticar_usuario(usuario, senha):

    senha = criptografar_senha(senha)

    usuarios = carregar_usuarios()

    return any(
        u["usuario"] == usuario and
        u["senha"] == senha
        for u in usuarios
    )