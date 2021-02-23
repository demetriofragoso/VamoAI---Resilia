print("Qual foi o preço do KG tomate a 1 ano atrás?")
tomate_anterior = float(input())
print("Qual é o preço do kg do tomate hoje?")
tomate_hoje = float (input())

diferenca =  tomate_hoje - tomate_anterior 
print("A diferença de preço do KG do tomate em um ano é de:",diferenca)

inflacao = (diferenca/tomate_anterior)*100

print ("inflação do KG do tomate em um ano é de:", inflacao)