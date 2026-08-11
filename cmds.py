import customtkinter as ctk
import os
from PIL import Image

def trocar_tela(janela, nova_tela):
    for widget in janela.winfo_children():
        widget.destroy()

    nova_tela(janela)


def botao_voltar_menu(frame, janela, nova_tela):
    botao = ctk.CTkButton(
        frame,
        text="Voltar ao Menu",
        font=("Helvetica", 12, "bold"),
        command=lambda: trocar_tela(janela, nova_tela)
    )

    botao.pack(pady=20)

# ----------------------- IMAGENS -----------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def carregar_imagem(nome_arquivo, tamanho):
    caminho = os.path.join(BASE_DIR, "imagens", nome_arquivo)

    return ctk.CTkImage(
        light_image=Image.open(caminho),
        size=tamanho
    )
# -------------------------------------------------------