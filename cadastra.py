import mysql.connector

# =========================
# CONEXÃO COM O BANCO
# =========================
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='SUA_SENHA_AQUI',
    database='cadastra',
)

cursor = conexao.cursor()

# =========================
# CRIAÇÃO DA TABELA
# =========================
tabela_cadastro = 'cliente_cadastrado'

comando = f"""
CREATE TABLE IF NOT EXISTS {tabela_cadastro} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
)
"""
cursor.execute(comando)
conexao.commit()

# =========================
# LOOP PRINCIPAL
# =========================
resposta = -1

while resposta != 0:
    print("""
    1 - Cadastrar Cliente
    2 - Listar Clientes
    3 - Deletar Cliente
    4 - Atualizar Cliente
    0 - Sair
    """)

    try:
        resposta = int(input("Escolha: "))
    except:
        print("Entrada inválida! Digite um número.")
        continue

    # =========================
    # 1 - CADASTRAR
    # =========================
    if resposta == 1:
        nome = input("Digite o nome: ").strip()

        # validação
        if nome == "":
            print("Nome inválido!")
        else:
            # proteção contra SQL Injection usando %s
            comando = f"INSERT INTO {tabela_cadastro} (nome) VALUES (%s)"
            cursor.execute(comando, (nome,))
            conexao.commit()
            print("Cliente cadastrado com sucesso!")

    # =========================
    # 2 - LISTAR
    # =========================
    elif resposta == 2:
        comando = f"SELECT * FROM {tabela_cadastro} ORDER BY nome"
        cursor.execute(comando)
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            for id_cliente, nome in resultado:
                print(f"ID: {id_cliente} | Nome: {nome}")

            # COUNT com fetchone (mais eficiente)
            comando = f"SELECT COUNT(*) FROM {tabela_cadastro}"
            cursor.execute(comando)
            total = cursor.fetchone()[0]

            print(f"Total de clientes: {total}")

    # =========================
    # 3 - DELETAR
    # =========================
    elif resposta == 3:
        try:
            id_cliente = int(input("Digite o ID do cliente que deseja excluir: "))
        except:
            print("ID inválido!")
            continue

        comando = f"DELETE FROM {tabela_cadastro} WHERE id = %s"
        cursor.execute(comando, (id_cliente,))
        conexao.commit()

        # verifica se deletou
        if cursor.rowcount == 0:
            print("Cliente não encontrado!")
        else:
            print("Cliente deletado com sucesso!")

    # =========================
    # 4 - ATUALIZAR
    # =========================
    elif resposta == 4:
        try:
            id_cliente = int(input("Digite o ID do cliente: "))
        except:
            print("ID inválido!")
            continue

        nome = input("Digite o novo nome: ").strip()

        if nome == "":
            print("Nome inválido!")
            continue

        comando = f"UPDATE {tabela_cadastro} SET nome = %s WHERE id = %s"
        cursor.execute(comando, (nome, id_cliente))
        conexao.commit()

        if cursor.rowcount == 0:
            print("Cliente não encontrado!")
        else:
            print("Cliente atualizado com sucesso!")

    # =========================
    # 0 - SAIR
    # =========================
    elif resposta == 0:
        print("Programa encerrado!")

    else:
        print("Opção inválida!")