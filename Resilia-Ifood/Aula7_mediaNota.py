def nota(aluno1, aluno2, aluno3, aluno4, aluno5):
    media= (aluno1 + aluno2 + aluno3 + aluno4 + aluno5) / 5
    print("A média das notas de 5 alunos foi ",media)

print("Olá, alunos! insira as suas notas para avaliar a média de vocês!")
aluno1 = int(input("Aluno 1 - "))
aluno2 = int(input("Aluno 2 - "))
aluno3 = int(input("Aluno 3 - "))
aluno4 = int(input("Aluno 4 - "))
aluno5 = int(input("Aluno 5 - "))
nota(aluno1, aluno2, aluno3, aluno4, aluno5)