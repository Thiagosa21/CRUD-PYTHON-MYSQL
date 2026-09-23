# 📋 Sistema de Cadastro CRUD em Python e MySQL

> Um sistema simples de linha de comando (CLI) desenvolvido em Python para gerenciar cadastros de clientes utilizando um banco de dados relacional MySQL.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.12.8**
* **MySQL**
* **Biblioteca `mysql-connector-python`**
* **Biblioteca `python-dotenv`** (para segurança de credenciais)

---

## ⚙️ Funcionalidades

O sistema implementa um **CRUD** completo:
1. **Cadastrar Cliente:** Insere um novo registro com validação de nome e proteção contra *SQL Injection*.
2. **Listar Clientes:** Exibe todos os clientes cadastrados em ordem alfabética e mostra a contagem total de registros.
3. **Deletar Cliente:** Remove um cliente do banco de dados com base no ID informado, validando a existência do registro.
4. **Atualizar Cliente:** Altera o nome de um cliente existente buscando pelo ID.
5. **Sair:** Encerra a aplicação de forma segura.

---

## 🛠️ Como Executar o Projeto Localmente

### Pré-requisitos
* Ter o **Python** instalado na sua máquina.
* Ter um servidor **MySQL** rodando localmente (ex: XAMPP, MySQL Workbench ou Docker).

### 1. Clonar o repositório
```bash
git clone [https://github.com/SEU_USUARIO/nome-do-repositorio.git](https://github.com/SEU_USUARIO/nome-do-repositorio.git)
cd nome-do-repositorio
