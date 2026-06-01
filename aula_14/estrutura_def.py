def calcular_preco_pizza(tamanho, borda_recheada=False):
    "Calcular o preço final de uma pizza com opções."
    tabela = {"P": 25.0, "M": 35.0, "G": 45.0}
    preco = tabela[tamanho]
    if borda_recheada: # borda_recheada == True Por padrão toda variável é True
        preco += 8.0 # preco = preco + 8.0
    return preco  

print(calcular_preco_pizza("P")) # 25
print(calcular_preco_pizza("P",True)) # 33
print(calcular_preco_pizza("M", False)) # 35