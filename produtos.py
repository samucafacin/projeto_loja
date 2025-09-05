from datetime import datetime   

class produtos:
    def __init__(self, nome, descricao, preco, estoque, id_categoria):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.id_categoria = id_categoria

    def inserir_produtos(self, conexao, id_pedido, id_produto, quantidade, preco_unitario):
        cursor = conexao.cursor()
        sql = """
        INSERT INTO item_produto (id_pedido, id_produto, quantidade, preco_unitario)
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