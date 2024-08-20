from modulo import *


print("Digite a opção desejada: \n")
opcao = input("1 - somar\n2 - subtrair\n\nOpcao: ")

a = int(input("Digite um número: "))
b = int(input("Digite um segundo número: "))


if opcao == "1":
    print(somar(a,b))

elif opcao == "2":
    print(sub(a,b))