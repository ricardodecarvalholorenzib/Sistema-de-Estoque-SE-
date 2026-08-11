# 📦 StockFlow — Beta

Sistema de gerenciamento de estoque desenvolvido em **Python** com **CustomTkinter**.

> ⚠️ Projeto em desenvolvimento — versão **Beta**.

## ✨ Funcionalidades

- 🔐 Sistema de login e criação de contas
- 🔒 Senhas armazenadas utilizando hash
- 👤 Produtos separados por usuário autenticado
- 📦 Cadastro de produtos
- 📋 Listagem de produtos cadastrados
- ✏️ Edição de produtos
- 🗑️ Exclusão de produtos
- 💰 Cadastro e edição de preço e quantidade
- 💾 Persistência dos dados em arquivos **JSON**
- 🖼️ Interface gráfica com CustomTkinter
- 👁️ Opção para mostrar/ocultar senha
- 🔄 Navegação entre telas
- 🛡️ Tratamento básico para arquivos JSON inexistentes ou inválidos

## 💾 Persistência de dados

Os dados locais da aplicação são armazenados na pasta `dados/`.

Os arquivos de dados são mantidos fora do controle de versão através do `.gitignore`, evitando que informações locais sejam publicadas no GitHub.

Cada produto é associado ao usuário que o cadastrou, permitindo que diferentes contas mantenham estoques separados.

> Atualmente o projeto utiliza **JSON** como armazenamento. Uma futura evolução prevista é a migração para **SQLite**.

## 🚧 Em desenvolvimento

- 🔐 Login automático / persistência da sessão entre execuções
- 🔎 Pesquisa e filtros de produtos
- ✅ Validações mais completas dos formulários
- 🛡️ Confirmação antes de excluir produtos
- ✨ Melhorias de interface e consistência visual
- 🧪 Testes automatizados
- 🛒 Sistema de vendas
- 📊 Relatórios
- 🗄️ Migração para SQLite
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
├── images/         # Imagens utilizadas pela interface
├── telas/          # Telas da aplicação
├── util/           # Funções auxiliares e persistência
├── main.py         # Ponto de entrada
├── .gitignore
└── README.md
```

## 📌 Status

**Versão: v0.3.0-beta**

O StockFlow está sendo desenvolvido como projeto de estudo e prática de programação em Python, organização de código, interfaces gráficas, autenticação e persistência de dados.

O projeto ainda está em evolução e novas funcionalidades estão sendo planejadas através das **GitHub Issues**.

---

Desenvolvido por **Ricardo de Carvalho Lorenzib**.
