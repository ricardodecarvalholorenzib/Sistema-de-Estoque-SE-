# listar_prod.py

import customtkinter as ctk
from PIL import Image
from util.prod_save import carregar_produtos
from util.cmds import botao_voltar_menu
from telas.menu import abrir_menu
import os
from util.cmds import carregar_imagem

def abrir_listar(janela):
    janela.title("Listar Produtos")
    
    frame = ctk.CTkScrollableFrame(
    janela,
    width=450,
    height=500,
    fg_color="transparent"
    )

    frame._scrollbar.grid_remove()

    titulo = ctk.CTkLabel(
    frame,
    text="Listar Produtos",
    font=("Segoe UI", 24, "bold")
    )
    titulo.pack(pady=20)

    erro_label = ctk.CTkLabel(
        frame,
        text="",
        font=("Helvetica", 20, "bold"),
        text_color="red"
    )

    produtos = carregar_produtos()

    if produtos:
        for produto in produtos:
            caixa_image = carregar_imagem("caixa.png", (50, 50))

            card = ctk.CTkFrame(
                frame,
                corner_radius=10
            )

            titulo = ctk.CTkLabel(
                card,
                image=caixa_image,
                compound="left",
                text=f"{produto['nome_produto']}",
                font=("Segoe UI", 18, "bold")
            )

            preco = ctk.CTkLabel(
                card,
                text=f"Preço: R${produto['preco']:.2f}"
            )

            quantidade = ctk.CTkLabel(
                card,
                text=f"Quantidade: {produto['quantidade']}"
            )

            titulo.pack(anchor="w", padx=15, pady=(10,5))
            preco.pack(anchor="w", padx=15)
            quantidade.pack(anchor="w", padx=15, pady=(0,10))

            card.pack(fill="x", padx=10, pady=8)
    
    if not produtos:
        erro_label.configure(text="Você não tem produtos registrados!")


    erro_label.pack(pady=20)
    botao_voltar_menu(frame, janela, abrir_menu)

    frame.pack(pady=20)
