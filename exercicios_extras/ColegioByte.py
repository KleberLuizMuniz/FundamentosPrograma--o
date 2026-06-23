CONTADOR = 1
Historico_alunos = []
Alunos_cadastrados = int(input("quantos alunos serão cadastrados?: "))
while Alunos_cadastrados + 1 != CONTADOR :
    nome_aluno = input("qual o nome dos alunos? ")
    nota_p = float(input("informe a primeira nota do aluno: "))
    nota_s = float(input("informe a segunda nota do aluno: "))
    nota_t = float(input("informe a terceira nota do aluno: "))
    media_nota = float(((nota_p * 2) + (nota_s*3) + (nota_t*5))/10)
    print(f"A média de suas notas é: {media_nota} ")
    if media_nota >= 9:
        registro = f"---Aluno {CONTADOR}: {nome_aluno}, Primeira nota é:{nota_p} Segunda nota é:{nota_s} Terceira nota é:{nota_t}, sua média é: {media_nota}, Aluno Aprovado com direito a menção honrosa!--- "
        Historico_alunos.append(registro)
        print(f"Aluno {CONTADOR} registrado!")
        CONTADOR += 1
    elif media_nota >= 7:
        registro = f"---Aluno {CONTADOR}: {nome_aluno}, Primeira nota é:{nota_p} Segunda nota é:{nota_s} Terceira nota é:{nota_t}, sua média é: {media_nota}, Aluno Aprovado!--- "
        Historico_alunos.append(registro)
        print(f"Aluno {CONTADOR} registrado!")
        CONTADOR += 1
    elif media_nota >= 5:
        registro = f"---Aluno {CONTADOR}: {nome_aluno}, Primeira nota é:{nota_p} Segunda nota é:{nota_s} Terceira nota é:{nota_t}, sua média é: {media_nota}, Aluno precisará de recuperação!--- "
        Historico_alunos.append(registro)
        print(f"Aluno{CONTADOR} registrado!")
        CONTADOR += 1
    else:
        registro = f"---Aluno {CONTADOR}: {nome_aluno}, Primeira nota é:{nota_p} Segunda nota é:{nota_s} Terceira nota é:{nota_t}, sua média é: {media_nota}, Aluno reprovado!--- "
        Historico_alunos.append(registro)
        print(f"Aluno {CONTADOR} registrado!")
        CONTADOR += 1
for nome_notas in Historico_alunos:
        print(nome_notas)


