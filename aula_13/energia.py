valor_ate_100kw = 0.40
valor_ate_200kw = 0.60
valor_acima_200kw = 0.90

print(f"------ Seja Bem vindo ao programa de energia eletrica ------")
while True:
    consumo_energia = input(f"seu consumo de energia em kwa é: ")
    if consumo_energia.lower() == 'sair':
        print("encerrando o programa. obrigado por usar!\n")
        break
    elif not consumo_energia.isdigit():
        print("invalido\n")
        continue
    else:
        kwh = float(consumo_energia)
        if kwh <= 100:
            valor_total = kwh * valor_ate_100kw
            print(f'a faixa de consumo é 0 - 100 kwh. o custo do seu consumo é R${valor_total:.2f}')
        elif kwh <= 200:
            valor_total = ((kwh - 100) * valor_ate_200kw) + 40
            print(f'a faixa de consumo é 0 - 200 kwh. o custo do seu consumo é R${valor_total:.2f}')
        else:
            valor_total = ((kwh - 200) * valor_acima_200kw) + 100
            print(f'a faixa de consumo é maior que 200 kwh. o custo do seu consumo é R${valor_total:.2f}')