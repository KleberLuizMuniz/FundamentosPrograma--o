# preisamos criar um molde de uma pessoa. => class
# caracteristicas -> atributos -> variáveis
# ações - métodos - funções

class MoldePessoa:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf
    
    def apresentar(self) -> str:
        return f"Seja Bem vindo {self.nome} de cpf:{self.cpf}"
    
pessoa1 = MoldePessoa("Lídia" , "123")
print(pessoa1.apresentar())
        
