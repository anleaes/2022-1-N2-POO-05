class Disciplina:
    
    def __init__(self,nome,codigo_disciplina,carga_horaria,turno,modalidade_disciplina,descricao,professor,curso):
        self._nome = nome
        self._codigo_disciplina = codigo_disciplina
        self.carga_horaria = carga_horaria
        self._turno = turno
        self._modalidade_disciplina = modalidade_disciplina
        self._descricao = descricao
        self._professor = professor
        self._curso = curso
