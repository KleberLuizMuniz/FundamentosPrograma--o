idade = int(input("informe sua idade: "))
if idade < 18:
        print("idade insuficiente!🚫")
else:
        nota = float(input("sua nota é: "))
        if nota >= 9:
                print(f"sua idade é {idade}, sua nota é {nota}")
                print("Aprovado automaticamente")
        else:
                frequencia = float(input("Digite a porcentagem de frequência (0-100): "))
                frequencia_decimal = frequencia / 100
                if frequencia_decimal < 75/100:
                        print(f"sua idade é {idade}, sua nota é {nota} sua frequencia é {frequencia}% ")
                        print("Sua frequencia está baixa, matrícula negada!")
                else:
                        if idade >= 18 and nota >= 6 and frequencia_decimal >= 75/100:
                                print(f"sua idade é {idade}, sua nota é {nota} sua frequencia é {frequencia}% ")
                                print("sua matricula está aprovada")
                        else:
                                print("Matricula negada!")