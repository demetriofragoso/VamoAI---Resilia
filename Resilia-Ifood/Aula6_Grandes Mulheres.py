print('{::^120}'.format('  Ada Lovelace  '))
print("")
print("Iremos realizar três perguntas sobre a vida e historia da grande mulher que faz parte da ciência atual!")

print("Pergunta 1 - Alem de ser a primeira mulher a criar uma linguagem de programação, o que ela mais gostava de fazer?")
print("1 - Recitar poemas")
print("2 - Costurar")
print("3 - Imaginar")
acertou = 0
pergunta_1 = int(input("Qual a alternativa correta? "))
if pergunta_1 == 1 or pergunta_1 == 3:
    print("Você acertou!")
    acertou += 1
else:
    print("Você errou!")


print("Pergunta 2 - Quem foi sua maior influência?")
print("1 - Seu pai (poeta).")
print("2 - Sua mãe (matemática).")
print("3 - Não teve influência.")

pergunta_2 = int(input("Qual a alternativa correta?"))
if pergunta_2 == 1 or pergunta_2 == 2:
    print("Você acertou!")
    acertou += 1
else:
    print("Você errou")


print("Pergunta 3 - A Ada Lovelace criava poesias e criou uma liguagem de programação, quais os adjetivos que ela teve para conseguir?")
print("1 - Curiosidade")
print("2 - Criatividade")
print("3 - Imparcial ")

pergunta_3 = int(input("Qual a alternativa correta?"))
if pergunta_3 == 1 or pergunta_3 == 2:
    print("Você acertou!")
    acertou += 1
else: 
    print("Você errou!")


if acertou == 3:
    print("Você é fera! Acertou todas as questões!")
elif acertou == 2 or acertou == 1:
    print("Você não acertou todas, mas mesmo assim está de parabéns!")
else:
    print("Que pena! Leia mais sobre a Ada Lovelace e outras mulheres da nossa ciência que fizerem história!")

