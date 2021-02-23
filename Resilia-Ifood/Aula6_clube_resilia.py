print('{::^80}'.format(' C L U B E  R E S I L I A '))
print("")
nome = input("olá! Qual o seu nome?  ")
idade = int(input("Qual a sua idade?  "))
estudante_python = input("Você é estudante de Python? sim ou não  ")

entrada_padrao = int(35) 
entrada_VIP = int(60)

if idade >= 18:
    print("Que ótimo! você poderá entrar no clube")

if idade < 18:
    print(f"Que pena você não poderá entrar, falta {18-idade} anos para entrar no clube!")

elif idade >= 18 and estudante_python == "sim": 
    print("Que maravilha! Você acaba de ganhar 50% desconto no valor da entrada!")
    print("Qual a entrada você vai querer? normal",entrada_padrao,"reais ou VIP",entrada_VIP,"reais")
    ingresso = int(input(""))
    if entrada_padrao == ingresso:
        print(f"{entrada_padrao/2} reais é o valor da sua entrada!")
    elif entrada_VIP == ingresso:
        print(f"{entrada_VIP/2} reais é o valor da sua entrada!")

else: 
    idade >= 18 and estudante_python == "nao"
    print("Que pena, você não ganhou o desconto!")
    print("Qual a entrada você vai querer?",entrada_padrao,"reais ou",entrada_VIP,"reais")
    ingresso = int(input(""))    
    if entrada_padrao == ingresso:
        print(f"{entrada_padrao} reais é o valor da sua entrada!")
    elif entrada_VIP == ingresso:
        print(f"{entrada_VIP} reais é o valor da sua entrada!")

