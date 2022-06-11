from funcionario import Funcionario

class Professor(Funcionario):
        
    def __init__(self, nome, cpf, endereco, telefone, graducao, salario, carga_horaria_semanal,numero_de_disciplinas_lecionadas ):
        super().__init__(nome, cpf, endereco, telefone)
        self._graducao = graducao
        self._salario = salario
        self._carga_horaria_semanal = carga_horaria_semanal
        self._numero_de_disciplinas_lecionadas = numero_de_disciplinas_lecionadas
    