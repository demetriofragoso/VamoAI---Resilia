def multiplicador(num1,num2):
    if (num1 >=1) and (num1 <=50) and (num2 >=1) and (num2<=50):
        resultado = num1*num2
        print("O resultado é", resultado)
    else:
        print("Não podemos seguir com o calculo!")

print("Vamos multiplicar dois valores a sua escolha, entre 1 ao 50!")
numero1 = int(input("Digite o primeiro! "))
numero2 = int(input("Digite o segundo!"))

multiplicador(numero1,numero2)
