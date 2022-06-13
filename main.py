from aluno import Aluno
from area import Area
from campus import Campus
from coordenador import Coordenador
from curso import Curso
from disciplina import Disciplina
from funcionario import Funcionario
from matricula import Matricula
from professor import Professor
from reitor import Reitor
from turma import Turma

print("Sistema de Matricula de faculdade")

aluno1 = Aluno("Fulano de Tal", 12345678910, "(51) 99999-8888", "12/06/2000", "Rua tal, número 1")

coordenador1 = Coordenador("Vanderlei Luxemburgo",  90909090909, "rua avenida, numero 10", "(51) 90909-0909", "Doutorado", "10,000", 3)

area1 = Area("Tecnologia", "Area dos cursos de Tecnologia da Informação", 1, coordenador1)

funcionario1 = Funcionario("Fulaninho de tal", 90909090908, "(51) 50505-5050", "funcionario1@uniritter.com")

professor1 = Professor("Professor fulano", 12544512346, "Rua tal, 123", "(51) 90909-9090", "Mestrado", 5000, 40, 10 )

reitor1 = Reitor("Reitor Ciclano", 88884444222, "Rua do canto, 123", "(51) 70707-7070", 15000, 1)

campus1 = Campus("Campus FAPA","Manoel Elias, 2000", 1, reitor1)

curso1 = Curso("Analise de Sistemas", 12, "Superior tecnologico", "Presencial", "2,5 anos", area1)

disciplina1 = Disciplina("Programação Orientada a Objetos", "2022/1", 5, 94.6, "Noite", "Presencial", "Disciplina de POO", curso1, professor1)

matricula1 = Matricula(1, "graduação", "12/02/2022", aluno1, disciplina1)

turma1 = Turma("TI-1", "Segunda-Feira", "19:10", "505A", professor1, aluno1, disciplina1)

def mostrar_aluno(self):
    print("O aluno de nome ", {self._aluno._nome}, "tem o seguinte cpf ", {self._aluno._cpf}, "seu telefone é ", {self._aluno._telefone}, "nascido em ", {self._aluno._data_nascimento}, "e reside no endereço:", {self._aluno._endereco})

def mostrar_curso(self):
    print("O Curso de ", {self._curso._nome}, "de código ", {self._curso._código_curso}, "e tipo de formação é", {self._curso._formacao}, ".Esse curso é na modalidade", {self._curso._modalidade}, "com duração de", {self._curso._duracao},"faz parte da área",{self._curso._area})

def mostrar_matricula(self):
     print("A matricula de código", {self._matricula._codigo_matricula}, "de tipo ", {self._matricula._tipo}, "feita na data", {self._matricula._data}, "é do aluno", {self._matricula._aluno._nome}, "na disciplina", {self._matricula._disciplina._nome})