# 📦 StockFlow — Beta

Sistema de gerenciamento de estoque desenvolvido em **Python** com **CustomTkinter**.

> ⚠️ Projeto em desenvolvimento — versão **Beta**.

## ✨ Funcionalidades

- 🔐 Sistema de login e criação de contas
- 🔒 Senhas armazenadas utilizando hash
- 📦 Cadastro de produtos
- 📋 Listagem de produtos cadastrados
- 🆔 Identificação dos produtos
- 💰 Cadastro de preço e quantidade
- 💾 Persistência dos produtos em arquivos **JSON**
- 👤 Persistência dos usuários em arquivo **JSON**
- 🖼️ Interface gráfica com CustomTkinter
- 👁️ Opção para mostrar/ocultar senha
- 🔄 Navegação entre telas
- 🛡️ Tratamento básico para arquivos JSON inexistentes ou inválidos

## 💾 Persistência de dados

Os dados locais da aplicação são armazenados na pasta `dados/`.

Os arquivos de dados são mantidos fora do controle de versão através do `.gitignore`, evitando que informações locais sejam publicadas no GitHub.

> Atualmente o projeto utiliza **JSON** como armazenamento. Uma futura evolução prevista é a migração para **SQLite**.

## 🚧 Em desenvolvimento

- 🛒 Sistema de vendas
- 🔎 Pesquisa de produtos
- ✏️ Edição de produtos
- 🗑️ Exclusão de produtos
- 📊 Relatórios
- 🗄️ Migração para SQLite
- ✨ Melhorias na interface
- 📦 Geração de executável (`.exe`)

## 🛠️ Tecnologias

- Python 3
- CustomTkinter
- Pillow (PIL)
- JSON

## ▶️ Como executar

Instale as dependências:

```bash
pip install customtkinter pillow
```

Depois execute:

```bash
python main.py
```

## 📁 Estrutura do projeto

```text
StockFlow/
├── dados/          # Dados locais da aplicação (não versionados)
├── imagens/        # Imagens utilizadas pela interface
├── telas/          # Telas da aplicação
├── util/           # Funções auxiliares e persistência
├── main.py         # Ponto de entrada
├── .gitignore
└── README.md
```

## 📌 Status

**Versão: v0.2.0-beta**

O StockFlow está sendo desenvolvido como projeto de estudo e prática de programação em Python, organização de código, interfaces gráficas e persistência de dados.

---

Desenvolvido por **Ricardo de Carvalho Lorenzib**.
