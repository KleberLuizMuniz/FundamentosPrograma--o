class Pessoa:
    def __init__(self, nome: str, cpf: str, nascimento: str):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
    def apresentar(self) -> str:
        return f"Seja Bem vindo {self.nome} de cpf:{self.cpf}"
    
pessoa1 = Pessoa("Lídia" , "123")
print(pessoa1.apresentar())