#Implemete um programa em python, em que o usuario informe uma letra. 
#Verificar se a letra informada é "F", escrever Feminino ou "M" escrever Masculino
letra=str(input("Digite a sigla do seu sexo: "))
if (letra == "F") or (letra == "f"):
    print(letra," de ","Feminino")
elif (letra == "M") or (letra == "m"):
    print(letra," de ","Masculino")
else:
    print("Letra invalida")
