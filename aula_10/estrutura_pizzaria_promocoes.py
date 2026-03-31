# Variaveis da pizzaria 
FRETE = 2 #Constante Fake 
pizza_sabor = input("informe o sabor da pizza- [frango com requeijão], [calabresa], [mussarela], [banana com chocolate]: ")
pizza_tamanho = input("informe o tamanho da pizza- [pequena], [media], [grande]: ")
dia_semana = input("informe o dia da semana- [quarta], [quinta], [sexta], [sabado], [domingo]: ")

print(f" O sabor escolhido da pizza é {pizza_sabor}, o tamanho é {pizza_tamanho} e hoje é {dia_semana}")

# Promoções -> Estruturas condicionais 

# comprando qualquer pizza e tamanho no sabado ganha refri gratuito
if dia_semana == "sabado":
    print(f"🍕pedido aceito com sucesso")
    print(f"o refri hoje é por conta da casa!")
#comprando qualquer pizza de qualquer tamanho no domingo, o frete e o refri são gratuitos 
elif dia_semana == "domingo":
    print(f"🍕pedido aceito com sucesso")
    print(f"o frete e o refri hoje é por conta da casa!")
# comprando uma pizza de calabresa de tamanho medio , em qualquer dia, frete gratis
elif pizza_sabor == "calabresa" and pizza_tamanho == "media":
     print(f"🍕pedido aceito com sucesso")
     print(f"o frete é por conta da casa!")

