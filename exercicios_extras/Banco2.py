nome = input("informe seu nome: ")
endereço = input("seu endereço: ")
idade = int(input("informe sua idade "))
if idade < 18:
        print("idade insuficiente! Pedido negado🚫")
else:
    salario = float(input("informe seu salário "))
    trinta_porcento = salario * 0.30
    if salario > 5000:
          print("Emprestimo garantido🤑🤑🤑💸💸")
    else:
            emprestimo = float(input("Quanto de emprestimo você deseja? "))
            parcela = emprestimo / 12
            while parcela > trinta_porcento:
                 print("A sua parcela é maior que trinta porcento do seu salario,por favor escolha um emprestimo menor") 
                 emprestimo = float(input("Quanto de emprestimo você deseja? "))
                 parcela = emprestimo / 12
            tempo_trabalho = int(input("informe quanto tempo você trabalha(em anos): "))
            if tempo_trabalho < 2:
                print("tempo de trabalho invalido! Pedido negado🚫")
            else:
                if idade >= 18 and salario >= 2000 and tempo_trabalho > 2:
                    print(f"seu nome é {nome}, seu endereço é {endereço}, sua idade é {idade}⌛, seu salário é {salario}💰 e seu tempo de trabalho atual é {tempo_trabalho} 💼 sua parcela é {parcela}➗")
                    print("Pedido enviado com sucesso e está em analise👍")
                else:
                    print("Pedido negado🚫")
                




           
