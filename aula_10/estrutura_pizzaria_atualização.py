#essa é a atualização do codigo da pizzaria para que se o usuario erre, o codigo já finalize em vez de pegar outros dados para avisar

#Constante Fake

SABORES_VALIDOS = ["frango com requeijão", "calabresa", "mussarela", "banana com chocolate"]
TAMANHOS_VALIDOS = ["pequena", "media", "grande"]
DIAS_VALIDOS = ["quarta", "quinta", "sexta", "sabado", "domingo"]
FRETE = 2 

#-> Estruturas condicionais 

#verificação do sabor
pizza_sabor = input("informe o sabor da pizza- [frango com requeijão], [calabresa], [mussarela], [banana com chocolate]: ").lower().strip()
if pizza_sabor not in SABORES_VALIDOS:
    print(f"❌ Pedido não concluído: sabor escolhido invalido!!!") 
else:
    pizza_tamanho = input("informe o tamanho da pizza- [pequena], [media], [grande]: ").lower().strip()
#verificação tamanho
    if pizza_tamanho not in TAMANHOS_VALIDOS:
        print(f"❌ Pedido não concluído: tamanho escolhido invalido!!!")
    else:
        dia_semana = input("informe o dia da semana- [quarta], [quinta], [sexta], [sabado], [domingo]: ").lower().strip()
#verificação dia
        if dia_semana not in DIAS_VALIDOS:
            print(f"❌ Pedido não concluído: dia da semana escolhido invalido!!!")
        else:
            print(f" O sabor escolhido da pizza é {pizza_sabor}, o tamanho é {pizza_tamanho} e hoje é {dia_semana}")

#promoções 

            # comprando qualquer pizza e tamanho no sabado ganha refri gratuito
            if dia_semana == "sabado":
                print(f"🍕pedido aceito com sucesso")
                print(f"já que é sabado, o refri hoje é por conta da casa!")
            #comprando qualquer pizza de qualquer tamanho no domingo, o frete e o refri são gratuitos 
            elif dia_semana == "domingo":
                print(f"🍕pedido aceito com sucesso")
                print(f"já que é domingo, o frete e o refri hoje é por conta da casa!")
            # comprando uma pizza de calabresa de tamanho medio , em qualquer dia, frete gratis
            elif pizza_sabor == "calabresa" and pizza_tamanho == "media":
                print(f"🍕pedido aceito com sucesso")
                print(f"já que a pizza é de calabresa e o tamanho é média, o frete é por conta da casa!")
            else:
                print(f"pedido realizado com sucesso")