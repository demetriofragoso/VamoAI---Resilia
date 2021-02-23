print('{::^80}'.format(' Vamos as Compras! '))
print("Olá! Por favor digita três produtos que você comprou no supermercado? ")
produto_1 = input("Digite o primeiro produto! ")
preco_1 = float(input("Digite o preço do primeiro produto! "))
produto_2 = input("Digite o segundo produto! ")
preco_2 = float(input("Digite o o preço do segundo produto! "))
produto_3 = input("Digite o terceiro produto! ")
preco_3 = float(input("Digite o preço do terceiro produto! "))

if preco_1 < preco_2 and preco_1 < preco_3:
    mais_barato = preco_1
    barato_nome = produto_1
elif preco_2 < preco_1 and preco_2 < preco_3:
    mais_barato = preco_2
    barato_nome = produto_2
else:
    mais_barato = preco_3
    barato_nome = produto_3
print(f"O produto mais barato das suas compras é {barato_nome} que custa apenas R$ {mais_barato:.2f}")
































































