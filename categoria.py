
from datetime import datetime

class Categoria:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

def inserir_categoria(conexao, nome, descricao):
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