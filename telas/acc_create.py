# acc_create.py

import customtkinter as ctk
from telas.menu import abrir_menu
from util.seguranca import criptografar_senha
from PIL import Image
import os
from util.cmds import carregar_imagem

def criar_conta(janela):

    janela.title("Criar Conta | StockFlow")

    frame = ctk.CTkFrame(
        janela,
        width=600,
        height=600,
        corner_radius=10,
        fg_color="transparent"
    )
    frame.pack(expand=True)

    titulo = ctk.CTkLabel(
        frame,
        text="Criar Nova Conta",
        font=("Segoe UI", 45, "bold"),
        text_color="grey"
    )
    titulo.pack(pady=(0, 30))

    nome_create = ctk.CTkEntry(
        frame,
        placeholder_text="Usuário",
        width=300,
        height=40
    )
    nome_create.pack(pady=10)

    erro_label = ctk.CTkLabel(
        frame,
        text="",
        font=("Segoe UI", 15),
        text_color="red"
    )

    frame_senha = ctk.CTkFrame(frame, fg_color="transparent")
    frame_senha.pack(pady=10)

    senha_create = ctk.CTkEntry(
        frame_senha,
        placeholder_text="Senha",
        show="*",
        width=243,
        height=40
    )
    senha_create.pack(side="left", padx=(0, 10))
    
    eye = carregar_imagem("eyes_on.png", (30, 20))
    eye_off = carregar_imagem("eyes_off.png", (30, 24))

    mostrando = False
    
    def mostrar_senha():
        nonlocal mostrando
        mostrando = not mostrando
        if mostrando:
            senha_create.configure(show="") 
            botao_olho.configure(image=eye_off) 
        else: 
            senha_create.configure(show="*") 
            botao_olho.configure(image=eye) 
        
    botao_olho = ctk.CTkButton(
        frame_senha,
        image=eye,
        text="",
        width=40,
        height=40,
        fg_color="transparent",
        hover=False,
        command=mostrar_senha
    )
    botao_olho.pack(side="left")
    
    from util.banco_data import criar_usuario

    def cadastrar():
        from util.cmds import trocar_tela
        from telas.menu import abrir_menu

        usuario = nome_create.get().strip()
        senha = senha_create.get()

        if not usuario:
            erro_label.configure(text="Digite um usuário.")
            return

        if not senha:
            erro_label.configure(text="Digite uma senha.")
            return

        criar_usuario(usuario, senha)

        trocar_tela(janela, abrir_menu)
        
    botao_criar_nova_conta = ctk.CTkButton(
        frame,
        text="Criar Conta",
        font=("Segoe UI", 20),
        width=200,
        height=45,
        command=cadastrar
    )
    botao_criar_nova_conta.pack(pady=(20, 0))

    def abrir_login():
        from util.cmds import trocar_tela
        from telas.login import abrir_login

        trocar_tela(janela, abrir_login)

    botao_criar_conta = ctk.CTkButton(
    frame,
    text="Já possui uma Conta?\nEntrar conta",
    fg_color="transparent",
    hover=False,
    text_color="#1E90FF",
    font=("Segoe UI", 13, "underline"),
    command=abrir_login
    )
    botao_criar_conta.pack(pady=20)