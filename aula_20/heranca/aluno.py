from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, cpf, nascimento, ano_ingresso: int, matricula: str):
        super().__init__(nome, cpf, nascimento)
        self.ano_ingresso = ano_ingresso
        self.matricula = matricula
        self.ativo = True
        self.notas = []

    

    def adicionar_notas(self, disciplina: str, nota: float):

        if not(0 <= nota <=10):
            raise ValueError("nota deve estar entre 0 e 10")
        if disciplina not in self.notas:
            self.notas[disciplina] = []

        self.notas[disciplina].append(nota)       