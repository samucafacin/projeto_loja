from database import conectar
from datetime import datetime

def inserir_produtos(conexao, id_pedido, id_produto, quantidade, preco_unitario):
    cursor = conexao.cursor()
    sql = """
        INSERT INTO item_pedido (id_pedido, id_produto, quantidade, preco_unitario)
        VALUES (%s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (id_pedido, id_produto, quantidade, preco_unitario))
        conexao.commit()
        print("Produto inserido com sucesso! ✅")
    except Exception as e:
        print("Erro ao inserir Produto:", e)
        conexao.rollback()
    finally:
        cursor.close()