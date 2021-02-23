nota_mat = float(input("Qual a nota de matematica?"))
nota_port = float(input("Qual a nota de português?"))
nota_qui = float(input("Qual a nota de quimica?"))

media =round(((nota_mat + nota_port + nota_qui) / 3))
print("Sua média é,",media)

if media >= 6:
    print("Que bom você foi aprovado!")
else:
    print("Opa! você precisa de estudar mais...")
