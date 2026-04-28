CONTADOR = 1
Historico_alunos = []
Alunos_cadastrados = int(input("quantos alunos serão cadastrados?: "))
if Alunos_cadastrados >= 2:
    while Alunos_cadastrados + 1 != CONTADOR :
        nome_aluno = input("qual o nome dos alunos? ")
        nota_p = float(input("informe a primeira nota do aluno: "))
        nota_s = float(input("informe a segunda nota do aluno: "))
        nota_t = float(input("informe a terceira nota do aluno: "))
        media_nota = (nota_p + nota_s + nota_t)/3
        print(f"A média de suas notas é: {media_nota} ")
        if media_nota >= 7:
            registro = f"---Aluno {CONTADOR}: {nome_aluno}, Primeira nota é:{nota_p} Segunda nota é:{nota_s} Terceira nota é:{nota_t} Aluno Aprovado!--- "
            Historico_alunos.append(registro)
            print(f"Aluno {CONTADOR} registrado!")
            CONTADOR += 1
        elif media_nota >= 5:
            registro = f"---Aluno {CONTADOR}: {nome_aluno}, Primeira nota é:{nota_p} Segunda nota é:{nota_s} Terceira nota é:{nota_t} Aluno precisará de recuperação!--- "
            Historico_alunos.append(registro)
            print(f"Aluno{CONTADOR} registrado!")
            CONTADOR += 1
        else:
            registro = f"---Aluno {CONTADOR}: {nome_aluno}, Primeira nota é:{nota_p} Segunda nota é:{nota_s} Terceira nota é:{nota_t} Aluno reprovado!--- "
            Historico_alunos.append(registro)
            print(f"Aluno {CONTADOR} registrado!")
            CONTADOR += 1
    for nome_notas in Historico_alunos:
        print(nome_notas)

else:
    nome = input("nome do aluno: ")
    nota_p = float(input("informe a primeira nota do aluno: "))
    nota_s = float(input("informe a segunda nota do aluno: "))
    nota_t = float(input("informe a terceira nota do aluno: "))
    media_nota = (nota_p + nota_s + nota_t)/3
    print(f"A média de suas notas é: {media_nota} ")
    if media_nota >= 7:
        print("Aluno aprovado!")
    elif media_nota >= 5:
        print("Aluno precisará de recuperação!")
    else:
        print("Aluno reprovado!")
        