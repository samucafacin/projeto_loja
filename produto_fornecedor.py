
from datetime import datetime
class produto_fornecedor:

    def __init__(self, nome, cnpj, email, telefone, data_cadastro=None):
        self.id = None
        self.nome = nome
        self.cnpj = cnpj
        self.email = email
        self.telefone = telefone
        
        self.data_cadastro = data_cadastro if data_cadastro else datetime.now()

    