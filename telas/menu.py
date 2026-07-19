# menu.py

import customtkinter as ctk
from PIL import Image
import os
from util.cmds import carregar_imagem

def abrir_menu(janela):
    janela.title("Menu Principal | Sistema de Estoque")
    ctk.set_appearance_mode("light")
    janela.geometry("500x350")

    frame = ctk.CTkScrollableFrame(
        janela,
        width=450,
        height=280,
        corner_radius=10
    )

    caixa_image = carregar_imagem("caixa.png", (50, 50))
    
    titulo = ctk.CTkLabel(
        frame,
        text="Menu Principal",
        font=("Segoe UI", 24, "bold"),
        text_color="black",
        image=caixa_image,
        compound="top",
        pady=20
    )
    titulo.pack(pady=25)

    button_cadastro_produto = ctk.CTkButton(
        frame,
        text="Cadastrar Produto",
        font=("Arial", 18),
        text_color="white",
        width=220,
        height=45
    )

    button_listar_produto = ctk.CTkButton(
        frame,
        text="Listar Produto",
        font=("Arial", 18),
        text_color="white",
        width=220,
        height=45
    )

    def cadastro_item():
        from util.cmds import trocar_tela
        from telas.cad_prod import abrir_produto

        trocar_tela(janela, abrir_produto)

    button_cadastro_produto.configure(command=cadastro_item)

    def ver_items():
        from util.cmds import trocar_tela
        from telas.listar_prod import abrir_listar

        trocar_tela(janela, abrir_listar)
    
    button_listar_produto.configure(command=ver_items)

    button_cadastro_produto.pack(pady=20)
    button_listar_produto.pack(pady=20)
    frame.pack(pady=20)