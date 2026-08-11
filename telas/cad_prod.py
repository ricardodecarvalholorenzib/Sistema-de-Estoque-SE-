# cad_prod.py

import customtkinter as ctk
import random
from PIL import Image
import os

produtos = []

# ==========================================
# IMPORT JANELA
# ==========================================

from util.cmds import botao_voltar_menu
from telas.menu import abrir_menu

def abrir_produto(janela):
    janela.title("Cadastro de Produtos")
    
    frame = ctk.CTkScrollableFrame(
    janela,
    width=450,
    height=500,
    fg_color="transparent",
    )

    frame._scrollbar.grid_remove()

    traço = ctk.CTkLabel(
        frame,
        text="―――――――――――――――――――――――――――――――――――",
        text_color="grey"
    )

    erro_digito_numero = ctk.CTkLabel(
        frame,
        text="",
        font=("Helvetica", 15),
        text_color="red"
    )

    titulo = ctk.CTkLabel(
        frame,
        text="Cadastro de Produtos",
        font=("Segoe UI", 24, "bold")
    )
    titulo.pack(pady=20)

    janela_result = ctk.CTkLabel(frame,text="") 
    
    janela_result.pack(pady=10)

    nome_produto = ctk.CTkEntry(
        frame,
        placeholder_text="Nome do produto",
        font=("Helvetica", 12, "bold"),
        text_color="black"
    
    )

    preço_produto = ctk.CTkEntry(
        frame,
        placeholder_text="Preço do Produto",
        font=("Helvetica", 12, "bold"),
        text_color="black"
    )

    quantidade_produto = ctk.CTkEntry(
        frame,
        placeholder_text="Quantidade do Produto",
        font=("Helvetica", 12, "bold"),
        text_color="black"
    )    

    from util.prod_save import criar_produto

    def cadastro_produto_nome():

        from telas.menu import abrir_menu

        from util.cmds import trocar_tela
        
        nome = nome_produto.get().capitalize()
        if not nome.strip():
            erro_digito_numero.configure(text="Digite o nome do produto.")
            return
        
        try:
            preço = float(preço_produto.get().replace(",", "."))
            quantidade = int(quantidade_produto.get())
        except ValueError:
            erro_digito_numero.configure(text="Você não pode digitar letras ou caracteres especiais\nnas caixas de números!")
            return

        sucesso = criar_produto(nome, preço, quantidade)
        if not sucesso:
            erro_digito_numero.configure(text="Produto já cadastrado!")
            return

        nome_produto.delete(0, "end")
        preço_produto.delete(0, "end")
        quantidade_produto.delete(0, "end")
        
        trocar_tela(janela, abrir_menu)

    botao_cad_prod = ctk.CTkButton(
        frame,
        text="Cadastrar Produto",
        font=("Helvetica", 12, "bold"),
        command=cadastro_produto_nome                        
        )
    
    nome_produto.pack(pady=20)
    preço_produto.pack(pady=20)
    quantidade_produto.pack(pady=20)
    botao_cad_prod.pack(pady=20)
    traço.pack(pady=30)
    botao_voltar_menu(frame, janela, abrir_menu)
    erro_digito_numero.pack(pady=20)
    frame.pack(pady=20)