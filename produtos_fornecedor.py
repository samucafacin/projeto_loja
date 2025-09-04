from database import conectar
from datetime import datetime



# INSERIR CATEGORIA

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



# INSERIR CLIENTE

def inserir_cliente(conexao, nome, cpf, email, telefone):
    cursor = conexao.cursor()
    sql = """
        INSERT INTO cliente (nome, cpf, email, telefone, data_cadastro)
        VALUES (%s, %s, %s, %s, %s)
    """
    try:
        data_cadastro = datetime.now()
        cursor.execute(sql, (nome, cpf, email, telefone, data_cadastro))
        conexao.commit()
        print("Cliente inserido com sucesso! ✅")
    except Exception as e:
        print("Erro ao inserir cliente:", e)
        conexao.rollback()
    finally:
        cursor.close()



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



# INSERIR ITEM DE PEDIDO

def inserir_item_pedido(conexao, id_pedido, id_produto, quantidade, preco_unitario):
    cursor = conexao.cursor()
    sql = """
        INSERT INTO item_pedido (id_pedido, id_produto, quantidade, preco_unitario)
        VALUES (%s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (id_pedido, id_produto, quantidade, preco_unitario))
        conexao.commit()
        print("Item de pedido inserido com sucesso! ✅")
    except Exception as e:
        print("Erro ao inserir item de pedido:", e)
        conexao.rollback()
    finally:
        cursor.close()



# PROGRAMA PRINCIPAL

def main():
    conexao = conectar()

    # Exemplo de uso:
    inserir_categoria(conexao, "Informática", "Produtos de tecnologia")
    inserir_cliente(conexao, "João Silva", "12345678900", "joao@email.com", "99999-9999")
    inserir_fornecedor(conexao, "Tech Ltda", "12345678000100", "3333-4444", "contato@tech.com")
    inserir_item_pedido(conexao, 1, 10, 2, 150.0)

    


if __name__ == "__main__":
    main()
