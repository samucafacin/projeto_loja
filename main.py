from database import conectar
from clientes import Clientes
from database import conectar
import tkinter as tk
from tkinter import messagebox
from clientes import Clientes
from categorias import inserir_categorias
from produtos import produto
from pedidos import Pedido
from itens_pedido import itens_pedido
from fornecedores import Fornecedor
from produto_fornecedor import produto_fornecedor
from datetime import datetime
 
## aqui é a parte estrutural do nosso código -- Funções de inserção.
def inserir_cliente(conexao, cliente):
    cursor = conexao.cursor()
    sql = """
        INSERT INTO cliente(nome, cpf, email, telefone, data_cadastro)
        VALUES (%s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (
            cliente.nome,
            cliente.cpf,
            cliente.email,
            cliente.telefone,
            cliente.data_cadastro
        ))
        conexao.commit()
        print("Cliente inserido com sucesso! ✅")
    except Exception as e:
        print("Erro ao inserir cliente:", e)
        conexao.rollback()
    finally:
        cursor.close()
 
 
def inserir_categoria(conexao, categoria):
    cursor = conexao.cursor()
    sql = "INSERT INTO categoria(nome, descricao) VALUES (%s, %s)"
    try:
        cursor.execute(sql, (categoria.nome, categoria.descricao))
        conexao.commit()
        print("Categoria inserida com sucesso! ✅")
    except Exception as e:
        print("Erro ao inserir categoria:", e)
        conexao.rollback()
    finally:
        cursor.close()
 
 
def inserir_produto(conexao, produto):
    cursor = conexao.cursor()
    sql = """
        INSERT INTO produto(nome, descricao, preco, estoque, id_categoria)
        VALUES (%s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (
            produto.nome,
            produto.descricao,
            produto.preco,
            produto.estoque,
            produto.id_categoria
        ))
        conexao.commit()
        print("Produto inserido com sucesso! ✅")
    except Exception as e:
        print("Erro ao inserir produto:", e)
        conexao.rollback()
    finally:
        cursor.close()
 
 
def inserir_pedido(conexao, pedido):
    cursor = conexao.cursor()
    sql = """
        INSERT INTO pedido(id_cliente, data_pedido, valor_total, status)
        VALUES (%s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (
            pedido.id_cliente,
            pedido.data_pedido,
            pedido.valor_total,
            pedido.status
        ))
        conexao.commit()
        print("Pedido inserido com sucesso! ✅")
    except Exception as e:
        print("Erro ao inserir pedido:", e)
        conexao.rollback()
    finally:
        cursor.close()
 
 
def inserir_item_pedido(conexao, item):
    cursor = conexao.cursor()
    sql = """
        INSERT INTO item_pedido(id_pedido, id_produto, quantidade, preco_unitario)
        VALUES (%s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (
            item.id_pedido,
            item.id_produto,
            item.quantidade,
            item.preco_unitario
        ))
        conexao.commit()
        print("Item de pedido inserido com sucesso! ✅")
    except Exception as e:
        print("Erro ao inserir item de pedido:", e)
        conexao.rollback()
    finally:
        cursor.close()
 
 
def inserir_fornecedor(conexao, fornecedor):
    cursor = conexao.cursor()
    sql = """
        INSERT INTO fornecedor(nome, cnpj, telefone, email)
        VALUES (%s, %s, %s, %s)
    """
    try:
        cursor.execute(sql, (
            fornecedor.nome,
            fornecedor.cnpj,
            fornecedor.telefone,
            fornecedor.email
        ))
        conexao.commit()
        print("Fornecedor inserido com sucesso! ✅")
    except Exception as e:
        print("Erro ao inserir fornecedor:", e)
        conexao.rollback()
    finally:
        cursor.close()
 
 
def inserir_produto_fornecedor(conexao, pf):
    cursor = conexao.cursor()
    sql = """
        INSERT INTO produto_fornecedor(id_produto, id_fornecedor, preco_compra)
        VALUES (%s, %s, %s)
    """
    try:
        cursor.execute(sql, (
            pf.id_produto,
            pf.id_fornecedor,
            pf.preco_compra
        ))
        conexao.commit()
        print("Produto_Fornecedor inserido com sucesso! ✅")
    except Exception as e:
        print("Erro ao inserir produto_fornecedor:", e)
        conexao.rollback()
    finally:
        cursor.close()
 
 
# Tela de Cadastro
def tela_cliente(conexao):
    win = tk.Toplevel()
    win.title("Cadastrar Cliente")
 
    tk.Label(win, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
    nome = tk.Entry(win)
    nome.grid(row=0, column=1)
 
    tk.Label(win, text="CPF:").grid(row=1, column=0, padx=5, pady=5)
    cpf=tk.Entry(win)
    cpf.grid(row=1, column=1)
 
    tk.Label(win, text="Email").grid(row=2, column=0, padx=5, pady=5)
    email=tk.Entry(win)
    email.grid(row=2, column=1)
 
    tk.Label(win, text="Telefone:").grid(row=3, column=0, padx=5, pady=5)
    telefone=tk.Entry(win)
    telefone.grid(row=3, column=1)
 
    def salvar():
        Cliente = Clientes(
            nome.get(),
            cpf.get(),
            email.get(),
            telefone.get()
        )
        inserir_cliente(conexao, Cliente)
        win.destroy()
 
    tk.Button(win, text="Salvar", command=salvar).grid(row=4, columnspan=2, pady=10)
 
## menu principal
def main():
    conexao = conectar()
 
    root = tk.Tk()
    root.title("Sistema de Cadastro")
 
    tk.Label(root, text="Painel Principal", font=("Arial", 16, "bold")).pack(pady=10)
 
    tk.Button(root, text="inserir Cliente", width=25, command=lambda: tela_cliente(conexao)).pack(pady=5)
   
    tk.Button(root, text="Inserir Categoria", width=25).pack(pady=5)
 
    tk.Button(root, text="Inserir Produto", width=25).pack(pady=5)
 
    tk.Button(root, text="Inserir Inserir Pedido", width=25).pack(pady=5)
 
    tk.Button(root, text="Inserir Inserir Item do Pedido", width=25).pack(pady=5)
 
    tk.Button(root, text="Inserir Fornecedor", width=25).pack(pady=5)
 
    tk.Button(root, text="Inserir Produto do Fornecedor", width=25).pack(pady=5)
 
    tk.Button(root, text="Sair", width=25, command=lambda: (conexao.close (), root.destroy())).pack(pady=20)
 
    root.mainloop()
 
 
if __name__ == "__main__":
    main()
    


