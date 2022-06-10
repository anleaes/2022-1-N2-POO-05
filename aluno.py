class Aluno:
    
    def __init__(self, nome, cpf, telefone, data_nascimento, endereco):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._data_nascimento = data_nascimento
        self._endereco = endereco

    @property
    def get_nome(self):
        return self._nome
    
    @get_nome.setter
    def set_nome(self, nome):
        self._nome = nome

    @property    
    def get_endereco(self):
        return self._endereco
    
    @get_endereco.setter
    def set_endereco(self, endereco):
        self._endereco = endereco
    