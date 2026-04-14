# SABORES_VALIDOS = ["frango com requeijão", "calabresa", "mussarela", "banana com chocolate"]

# contador = int(input("informe numero:"))

# while contador <= 5:
#     print(f"Número {contador}")
#     contador = contador + 1  

# if contador < 6:
#     print("falhou!")
# else:
#     print("agora podemos continuar")
#     pizza_sabor = input("informe o sabor da pizza- [frango com requeijão], [calabresa], [mussarela], [banana com chocolate]: ").lower().strip()    
#     while pizza_sabor not in SABORES_VALIDOS:
#         print("sabor invalido!")
#         pizza_sabor = input("informe o sabor da pizza- [frango com requeijão], [calabresa], [mussarela], [banana com chocolate]: ")
#     print("podemos continuar")

valor_inicial = 1000
while valor_inicial > 0:
    valor_sacado = float(input("Quanto voce quer sacar? "))
    valor_inicial -= valor_sacado
    print(f' saldo restante: {valor_inicial} ')