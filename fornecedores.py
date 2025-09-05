
from datetime import datetime


class fornecedores:
    def inserir_fornecedor(self, nome, cnpj, email, telefone, data_cadastro=None):
        self.nome = nome
        self.cnpj= cnpj
        self.email = email
        self.telefone = telefone
        # Se não passar data, usamos a data atual
        self.data_cadastro = data_cadastro if data_cadastro else datetime.now()
