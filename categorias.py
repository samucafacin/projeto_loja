from database import conectar
from datetime import datetime


def inserir_categorias(conexao, nome, descricao):
    cursor = conexao.cursor()
    sql = """
        INSERT INTO categoria (nome, descricao)
        VALUES (%s, %s)
    """
    try:
        cursor.execute(sql, (nome, descricao))
        conexao.commit()
        print("Categoria inserida com sucesso! ✅")
    except Exception as e:
        print("Erro ao inserir categoria:", e)
        conexao.rollback()
    finally:
        cursor.close()