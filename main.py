# main.py
import customtkinter as ctk

ctk.set_appearance_mode("light")

from telas.login import abrir_login

janela = ctk.CTk()

janela.title("SE | Login")
janela.geometry("600x600")

abrir_login(janela)

janela.mainloop()