from database import conectar
from clientes import Clientes
from categoria import Categoria
from produtos import produtos   
from pedido import pedido
from fornecedores import fornecedores
from produto_fornecedor import produto_fornecedor
import tkinter as tk


# -------- Funções de Inserção --------
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


def inserir_produtos(conexao, produto):
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


# --------- Tela de Cadastro de Cliente ---------
import tkinter as tk
from tkinter import messagebox

# === CLIENTE ===


def tela_cliente(conexao):
    janela = tk.Toplevel()
    janela.title("Inserir Cliente")

    tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
    entry_nome = tk.Entry(janela)
    entry_nome.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(janela, text="CPF:").grid(row=1, column=0, padx=5, pady=5)
    entry_cpf = tk.Entry(janela)
    entry_cpf.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(janela, text="Email:").grid(row=2, column=0, padx=5, pady=5)
    entry_email = tk.Entry(janela)
    entry_email.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(janela, text="Telefone:").grid(row=3, column=0, padx=5, pady=5)
    entry_telefone = tk.Entry(janela)
    entry_telefone.grid(row=3, column=1, padx=5, pady=5)

    def salvar():
        cliente = Clientes(entry_nome.get(), entry_cpf.get(), entry_email.get(), entry_telefone.get())
        inserir_cliente(conexao, cliente)
        messagebox.showinfo("Sucesso", "Cliente inserido com sucesso!")
        janela.destroy()

    tk.Button(janela, text="Salvar", command=salvar).grid(row=4, column=0, columnspan=2, pady=10)


# === CATEGORIA ===


def tela_categoria(conexao):
    janela = tk.Toplevel()
    janela.title("Inserir Categoria")

    tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
    entry_nome = tk.Entry(janela)
    entry_nome.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(janela, text="Descrição:").grid(row=1, column=0, padx=5, pady=5)
    entry_descricao = tk.Entry(janela)
    entry_descricao.grid(row=1, column=1, padx=5, pady=5)

    def salvar():
        categoria = Categoria(entry_nome.get(), entry_descricao.get())
        inserir_categoria(conexao, categoria)
        messagebox.showinfo("Sucesso", "Categoria inserida com sucesso!")
        janela.destroy()

    tk.Button(janela, text="Salvar", command=salvar).grid(row=2, column=0, columnspan=2, pady=10)


# === PRODUTO ===


def tela_produto(conexao):
    janela = tk.Toplevel()
    janela.title("Inserir Produto")

    tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
    entry_nome = tk.Entry(janela)
    entry_nome.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(janela, text="Descrição:").grid(row=1, column=0, padx=5, pady=5)
    entry_descricao = tk.Entry(janela)
    entry_descricao.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(janela, text="Preço:").grid(row=2, column=0, padx=5, pady=5)
    entry_preco = tk.Entry(janela)
    entry_preco.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(janela, text="Estoque:").grid(row=3, column=0, padx=5, pady=5)
    entry_estoque = tk.Entry(janela)
    entry_estoque.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(janela, text="ID Categoria:").grid(row=4, column=0, padx=5, pady=5)
    entry_categoria = tk.Entry(janela)
    entry_categoria.grid(row=4, column=1, padx=5, pady=5)

    def salvar():
        produto = produtos(entry_nome.get(), entry_descricao.get(), float(entry_preco.get()), int(entry_estoque.get()), int(entry_categoria.get()))
        inserir_produtos(conexao, produto)
        messagebox.showinfo("Sucesso", "Produto inserido com sucesso!")
        janela.destroy()

    tk.Button(janela, text="Salvar", command=salvar).grid(row=5, column=0, columnspan=2, pady=10)


# === PEDIDO ===


def tela_pedido(conexao):
    janela = tk.Toplevel()
    janela.title("Inserir Pedido")

    tk.Label(janela, text="ID Cliente:").grid(row=0, column=0, padx=5, pady=5)
    entry_cliente = tk.Entry(janela)
    entry_cliente.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(janela, text="Data Pedido (AAAA-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
    entry_data = tk.Entry(janela)
    entry_data.grid(row=1, column=1, padx=5, pady=5)

    def salvar():
        pedido = pedido(int(entry_cliente.get()), entry_data.get())
        inserir_pedido(conexao, pedido)
        messagebox.showinfo("Sucesso", "Pedido inserido com sucesso!")
        janela.destroy()

    tk.Button(janela, text="Salvar", command=salvar).grid(row=2, column=0, columnspan=2, pady=10)


# === ITEM PEDIDO ===


def tela_item_pedido(conexao):
    janela = tk.Toplevel()
    janela.title("Inserir Item do Pedido")

    tk.Label(janela, text="ID Pedido:").grid(row=0, column=0, padx=5, pady=5)
    entry_pedido = tk.Entry(janela)
    entry_pedido.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(janela, text="ID Produto:").grid(row=1, column=0, padx=5, pady=5)
    entry_produto = tk.Entry(janela)
    entry_produto.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(janela, text="Quantidade:").grid(row=2, column=0, padx=5, pady=5)
    entry_quantidade = tk.Entry(janela)
    entry_quantidade.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(janela, text="Preço Unitário:").grid(row=3, column=0, padx=5, pady=5)
    entry_preco = tk.Entry(janela)
    entry_preco.grid(row=3, column=1, padx=5, pady=5)

    def salvar():
        item = itens_pedido(int(entry_pedido.get()), int(entry_produto.get()), int(entry_quantidade.get()), float(entry_preco.get()))
        inserir_item_pedido(conexao, item)
        messagebox.showinfo("Sucesso", "Item inserido com sucesso!")
        janela.destroy()

    tk.Button(janela, text="Salvar", command=salvar).grid(row=4, column=0, columnspan=2, pady=10)


# === FORNECEDOR ===


def tela_fornecedor(conexao):
    janela = tk.Toplevel()
    janela.title("Inserir Fornecedor")

    tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
    entry_nome = tk.Entry(janela)
    entry_nome.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(janela, text="CNPJ:").grid(row=1, column=0, padx=5, pady=5)
    entry_cnpj = tk.Entry(janela)
    entry_cnpj.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(janela, text="Telefone:").grid(row=2, column=0, padx=5, pady=5)
    entry_telefone = tk.Entry(janela)
    entry_telefone.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(janela, text="Email:").grid(row=3, column=0, padx=5, pady=5)
    entry_email = tk.Entry(janela)
    entry_email.grid(row=3, column=1, padx=5, pady=5)

    def salvar():
        fornecedor = fornecedores(entry_nome.get(), entry_cnpj.get(), entry_telefone.get(), entry_email.get())
        inserir_fornecedor(conexao, fornecedor)
        messagebox.showinfo("Sucesso", "Fornecedor inserido com sucesso!")
        janela.destroy()

    tk.Button(janela, text="Salvar", command=salvar).grid(row=4, column=0, columnspan=2, pady=10)


# === PRODUTO FORNECEDOR ===


def tela_produto_fornecedor(conexao):
    janela = tk.Toplevel()
    janela.title("Inserir Produto do Fornecedor")

    tk.Label(janela, text="ID Produto:").grid(row=0, column=0, padx=5, pady=5)
    entry_produto = tk.Entry(janela)
    entry_produto.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(janela, text="ID Fornecedor:").grid(row=1, column=0, padx=5, pady=5)
    entry_fornecedor = tk.Entry(janela)
    entry_fornecedor.grid(row=1, column=1, padx=5, pady=5)

    def salvar():
        produto_fornecedor = produto_fornecedor (int(entry_produto.get()), int(entry_fornecedor.get()))
        inserir_produto_fornecedor(conexao, produto_fornecedor)
        messagebox.showinfo("Sucesso", "Produto do Fornecedor inserido com sucesso!")
        janela.destroy()

    tk.Button(janela, text="Salvar", command=salvar).grid(row=2, column=0, columnspan=2, pady=10)

    


# --------- Menu Principal ---------
def main():
    conexao = conectar()

    root = tk.Tk()
    root.title("Sistema de Cadastro")
    root.geometry("400x450")  # tamanho fixo
    root.configure(bg="#f0f4f7")  # fundo suave

    tk.Label(root, text="Painel Principal", font=("Arial", 18, "bold"), bg="#f0f4f7", fg="#333").pack(pady=15)

    estilo_botao = {
        "bg": "#cde7f0",
        "fg": "black",
        "activebackground": "#b5d8e6",
        "relief": "flat",
        "width": 25,
        "height": 2
    }

    tk.Button(root, text="Inserir Cliente", command=lambda: tela_cliente(conexao), **estilo_botao).pack(pady=6)
    tk.Button(root, text="Inserir Categoria", command=lambda: tela_categoria(conexao), **estilo_botao).pack(pady=6)
    tk.Button(root, text="Inserir Produto", command=lambda: tela_produto(conexao), **estilo_botao).pack(pady=6)
    tk.Button(root, text="Inserir Pedido", command=lambda: tela_pedido(conexao), **estilo_botao).pack(pady=6)
    tk.Button(root, text="Inserir Item do Pedido", command=lambda: tela_item_pedido(conexao), **estilo_botao).pack(pady=6)
    tk.Button(root, text="Inserir Fornecedor", command=lambda: tela_fornecedor(conexao), **estilo_botao).pack(pady=6)
    tk.Button(root, text="Inserir Produto do Fornecedor", command=lambda: tela_produto_fornecedor(conexao), **estilo_botao).pack(pady=6)



    def sair():
        if conexao is not None:
            conexao.close()
        root.destroy()

    tk.Button(root, text="Sair", command=sair, bg="#f5b7b1", fg="black", activebackground="#f1948a",
              relief="flat", width=25, height=2).pack(pady=15)

    root.mainloop()


if __name__ == "__main__":
    main()
