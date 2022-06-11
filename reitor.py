from funcionario import Funcionario

class Reitor(Funcionario):
        
    def __init__(self, nome, cpf, endereco, telefone, salario, numerodecampusadministrados):
        super().__init__(nome, cpf, endereco, telefone)
        self._salario = salario
        self._numerodecampusadministrados = numerodecampusadministrados