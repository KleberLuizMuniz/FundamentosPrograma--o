idade = int(input("informe sua idade "))
salario = float(input("informe seu salário "))
tempo_trabalho = int(input("informe quanto tempo você trabalha(em anos): "))
emprestimo = float(input("Quanto de emprestimo você deseja? resposta: "))
trinta_porcento = salario * 0.30
parcela = emprestimo / 12

print(f"sua idade é {idade}⌛, seu salário é {salario}💰 e seu tempo de trabalho atual é {tempo_trabalho} 💼 sua parcela é {parcela}➗")

if idade < 18:
    print("pedido negado por ser muito novo👎")
elif trinta_porcento < emprestimo:
    print("Pedido negado🚫")
elif salario >= 5000 and idade >= 18:
    print("Emprestimo garantido🤑🤑🤑💸💸")
elif idade >= 18 and salario >= 2000 and salario < 5000 and tempo_trabalho >= 2:
    print("Pedido enviado com sucesso e está em analise👍")
else:
    print("Pedido negado🚫")

