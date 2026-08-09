# login.py

import customtkinter as ctk
from telas.menu import abrir_menu

def abrir_login(janela):

    frame = ctk.CTkFrame(
        janela,
        width=600,
        height=600,
        corner_radius=10
    )

    titulo = ctk.CTkLabel(
        frame,
        text="Entrar no SE",
        font=("Segpe UI", 50, "bold"),
        text_color="grey"
    )

    nome_login = ctk.CTkEntry(
        frame,
        placeholder_text="Usuário",
        font=("Arial", 20),
        text_color="black"
    )

    senha_login = ctk.CTkEntry(
        frame,
        placeholder_text="Senha",
        font=("Arial", 20),
        show="*",
        text_color="black"
    )

    erro_label = ctk.CTkLabel(
        frame,
        text="",
        font=("Helvetica", 15),
        text_color="red"
    )

    botao_login = ctk.CTkButton(
        frame,
        text="Entrar",
        font=("Arial", 20),
        text_color="white"
    )

    def cadastro():
        nome = nome_login.get()
        senha = senha_login.get()
        
        if nome == "admin" and senha == "1234":
            for widget in janela.winfo_children():
                widget.destroy()
            abrir_menu(janela)
        else:
            erro_label.configure(text="Usuário ou senha incorretos")

    botao_login.configure(command=cadastro)

    titulo.pack(pady=20)
    nome_login.pack(pady=10)
    senha_login.pack(pady=10)
    erro_label.pack(pady=5)
    botao_login.pack(pady=20)
    frame.pack(pady=20)
