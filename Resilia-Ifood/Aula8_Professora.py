def media_geral(nota_historia,nota_portugues,nota_geografia,nota_matematica,nota_ingles):
    media = (nota_geografia+nota_historia+nota_ingles+nota_matematica+nota_portugues)/5
    print(media)

def media_disciplina(prova1,prova2,prova3):
    media = (prova1 + prova2 +prova3)/3
    print(media)

def status_aluno(nota):
    if nota >= 7 and nota <= 10:
        print("Parabéns você foi aprovado, por média!")
    elif nota >= 5 and nota < 7:
        print("você está em recuperação, mas tem a oportunidade de estudar mais")
    else:
        print("Infelizmente você foi reprovado!")


print("NOTAS - ESCOLA RESILIA")
print("Escolha alguma das duas opções para calcular a média geral ou por disciplina!")
print("Digite 1 para calcular a média geral!")
print("Digite 2 para calcular a média por disciplina!")

escolha_do_aluno = input()
if escolha_do_aluno == 1:
    nota_geografia = float(input("Digite a sua nota de geografia: "))
    nota_historia = float(input("Digite a sua nota de historia: "))
    nota_portugues = float(input("Digfite a sua nota de português: "))
    nota_matematica = float(input("Digite a sua nota de matematica: "))
    nota_ingles = float(input("Digite a sua nota de inglês: "))
    media = media_geral(nota_geografia,nota_historia,nota_ingles,nota_matematica,nota_portugues)
    print(f"A sua média geral é {media} pontos.")
else:
    prova1 = float(input("Digite a nota da sua primeira prova: "))
    prova2 = float(input("Digite a nota da sua segunda prova: "))
    prova3 = float(input("Digite a nota da sua terceira prova:  "))
    media = media_disciplina(prova1,prova2,prova3)
    print(f"A sua média na disciplina é {media} pontos.")

print("Agora que você já inseriu as notas, vamos vê se você foi aprovado")
status_aluno(nota)




