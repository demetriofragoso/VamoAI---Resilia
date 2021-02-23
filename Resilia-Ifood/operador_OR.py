print("Você já tomou a vacina?")
print("1. Já sim!")
print("2. Ainda não, mais irei tomar")
print("3. Não irei tomar!")
vacina = int(input("Qual a sua posição atual?"))

if vacina == 1 or vacina == 2:
    print("Parabéns, você vai virar um jacaré!")
else:
    print("Que pena, você é muito egoista essa causa é coletiva!")
