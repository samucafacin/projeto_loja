from database import conectar
from datetime import datetime


# INSERIR FORNECEDOR

def inserir_fornecedor(conexao, nome, cnpj, telefone, email):
    cursor = conexao.cursor()
    sql = """
        INSERT INTO fornecedor (nome, cnpj, telefone, email)
        VALUES (%s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (nome, cnpj, telefone, email))
        conexao.commit()
        print("Fornecedor inserido com sucesso! ✅")
    except Exception as e:
        print("Erro ao inserir fornecedor:", e)
        conexao.rollback()
    finally:
        cursor.close()

