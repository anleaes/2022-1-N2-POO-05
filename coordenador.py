from funcionario import Funcionario

class Coordenador(Funcionario):
        
    def __init__(self, nome, cpf, endereco, telefone, formacao, salario, numero_de_cursos_coordenados):
        super().__init__(nome, cpf, endereco, telefone)
        self._formacao = formacao
        self._salario = salario
        self._numero_de_cursos_coordenados = numero_de_cursos_coordenados