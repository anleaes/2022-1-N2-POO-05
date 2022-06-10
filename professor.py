from funcionario import Funcionario

class Professor(Funcionario):
        
    def __init__(self, nome, cpf, endereco, telefone, graducao, salario, carga_horaria_semanal):
        super().__init__(nome, cpf, endereco, telefone)
        self._graducao = graducao
        self._salario = salario
        self._carga_horaria_semanal = carga_horaria_semanal

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
    