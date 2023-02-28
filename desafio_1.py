#Escreva um programa que receba um valor e verifique o dia da semana correspondente
#OBS: Verificar se o valor é um dia invalido
dia = int(input("Digite o dia da semana: "))
if (dia >= 0) and (dia <= 7):
    if dia == 1:
        print("Segunda-Feira")
    elif dia == 2:
        print("Terça-Feira")
    elif dia == 3:
        print("Quarta-Feira")
    elif dia == 4:
        print("Quinta-Feira")
    elif dia == 5:
        print("Sexta-Feira")
    elif dia == 6:
        print("Sabado")
    elif dia == 7:
        print("Domingo")
else:
    print("Data invalida")

