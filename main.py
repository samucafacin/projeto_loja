from database import conectar
from clientes import Clientes




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
        print("Erro ao inserir o cliente:", e)
        conexao.rollback()
    finally:
        cursor.close()

def main():
    conexao = conectar()

    nome = input("Digite o seu nome: ")
    cpf = input("Digite o seu CPF: ")
    email = input("Digite o seu email: ")
    telefone = input("Digite o seu telefone: ")

    cliente = Clientes(nome, cpf, email, telefone)
    inserir_cliente(conexao, cliente)

    

if __name__ == "__main__":
    main()
