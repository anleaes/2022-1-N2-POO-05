from funcionario import Funcionario

class Reitor(Funcionario):
        
    def __init__(self, nome, cpf, endereco, telefone, salario, numero_de_campus_administrados):
        super().__init__(nome, cpf, endereco, telefone)
        self._salario = salario
        self._numero_de_campus_administrados = numero_de_campus_administrados