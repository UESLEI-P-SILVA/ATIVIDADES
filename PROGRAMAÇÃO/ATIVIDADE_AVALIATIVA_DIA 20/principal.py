from funcoes import *


nome = input("\nDigite o seu nome: ")
limpar()
print(f"{'-'*5} Seja bem-vindo ao sistema de conversão, {nome}! {'-'*5}\n")

while True:
    input("\nContinue...")
    print("Selecione qual conversão deseja fazer:")
    print("1 - Comprimento")
    print("2 - Volume")
    print("3 - Massa")
    print("4 - Temperatura")
    print("5 - Área")
    print("0 - Sair")

    opcao = input("\nOpção: ")
    limpar()
    if opcao == "0":
        print("Obrigado por usar o sistema de conversão. Até mais!")
        input()
        break
    
    elif opcao == "1":
        print("Qual medida você quer converter:")
        print("1.0 - Centímetro para Metro")
        print("1.1 - Centímetro para Quilômetro")
        print("1.2 - Metro para Centímetro")
        print("1.3 - Metro para Quilômetro")
        print("1.4 - Quilômetro para Centímetro")
        print("1.5 - Quilômetro para Metro")
        print("0 - Sair")
        
        medida = input("\nOpção: ")
        limpar()
        if medida == "1.0":
            recebe = "1"
            print(f"O valor de entrada em Centímetros convertido para Metro é: {centimetro_metro()}")
        elif medida == "1.1":
            print(f"O valor de entrada em Centímetros convertido para Quilograma é: {centimetro_quilometro()}")
        elif medida == "1.2":
            print(f"O valor de entrada em Metros convertido para Centímetros é: {metro_centimetro()}")
        elif medida == "1.3":
            print(f"O valor de entrada em Metros convertido para Quilometro é: {metro_quilometro()}")
        elif medida == "1.4":
            print(f"O valor de entrada em Quilometro convertido para Centímetros é: {quilometro_centimetro()}")
        elif medida == "1.5":
            print(f"O valor de entrada em Quilometro convertido para metro é: {quilometro_metro()}")
        elif medida == "0":
            print("Obrigado por usar o sistema de conversão. Até mais!")
            input()
            break
        else:
            print("Opção inválida!")
    
    elif opcao == "2":
        print("Qual medida você quer converter:")
        print("2.0 - Mililitro para Litro")
        print("2.1 - Litro para Mililitro")
        print("0 - Sair")
        
        medida = input("\nOpção: ")
        limpar()
        if medida == "2.0":
            print(f"O valor de entrada em Mililitro convertido para litro é: {mililitro_litro()}")
        elif medida == "2.1":
            print(f"O valor de entrada em Litro convertido para Mililitro é: {litro_mililitro()}")
        elif medida == "0":
            print("Obrigado por usar o sistema de conversão. Até mais!")
            input()
            break
        else:
            print("Opção inválida!")
    
    elif opcao == "3":
        print("Qual medida você quer converter:")
        print("3.0 - Grama para Quilograma")
        print("3.1 - Grama para Tonelada")
        print("3.2 - Quilograma para Grama")
        print("3.3 - Quilograma para Tonelada")
        print("3.4 - Tonelada para Grama")
        print("3.5 - Tonelada para Quilograma")
        print("0 - Sair")
        
        medida = input("\nOpção: ")
        limpar()
        if medida == "3.0":
            print(f"O valor de entrada em Grama convertido para Quilograma é: {grama_quilograma()}")
        elif medida == "3.1":
            print(f"O valor de entrada em Grama convertido para Tonelada é: {grama_tonelada()}")
        elif medida == "3.2":
            print(f"O valor de entrada em Quilograma convertido para Grama é: {quilograma_grama()}")
        elif medida == "3.3":
            print(f"O valor de entrada em Quilograma convertido para Tonelada é: {quilograma_tonelada()}")
        elif medida == "3.4":
            print(f"O valor de entrada em Tonelada convertido para Grama é: {tonelada_grama()}")
        elif medida == "3.5":
            print(f"O valor de entrada em Tonelada convertido para Quilograma é: {tonelada_quilograma()}")
        elif medida == "0":
            print("Obrigado por usar o sistema de conversão. Até mais!")
            input()
            break
        else:
            print("Opção inválida!")
    
    elif opcao == "4":
        print("Qual medida você quer converter:")
        print("4.0 - Celsius para Fahrenheit")
        print("4.1 - Celsius para Kelvin")
        print("4.2 - Fahrenheit para Celsius")
        print("4.3 - Fahrenheit para Kelvin")
        print("4.4 - Kelvin para Celsius")
        print("4.5 - Kelvin para Fahrenheit")
        print("0 - Sair")
        
        medida = input("\nOpção: ")
        limpar()
        if medida == "4.0":
            print(f"O valor de entrada em Celsius convertido para Fahrenheit é: {celsius_fahrenheit()}")
        elif medida == "4.1":
            print(f"O valor de entrada em Celsius convertido para Kelvin é: {celsius_kelvin()}")
        elif medida == "4.2":
            print(f"O valor de entrada em Fahrenheit convertido para Celsius é: {fahrenheit_celsius()}")
        elif medida == "4.3":
            print(f"O valor de entrada em Fahrenheit convertido para Kelvin é: {fahrenheit_kelvin()}")
        elif medida == "4.4":
            print(f"O valor de entrada em Kelvin convertido para Celsius é: {kelvin_celsius()}")
        elif medida == "4.5":
            print(f"O valor de entrada em Kelvin convertido para Fahrenheit é: {kelvin_fahrenheit()}")
        elif medida == "0":
            print("Obrigado por usar o sistema de conversão. Até mais!")
            input()
            break
        else:
            print("Opção inválida!")
    
    elif opcao == "5":
        print("Qual medida você quer converter:")
        print("5.0 - Centímetro Quadrado para Metro Quadrado")
        print("5.1 - Centímetro Quadrado para Hectare")
        print("5.2 - Metro Quadrado para Centímetro Quadrado")
        print("5.3 - Metro Quadrado para Hectare")
        print("5.4 - Hectare para Centímetro Quadrado")
        print("5.5 - Hectare para Metro Quadrado")
        print("0 - Sair")
        
        medida = input("\nOpção: ")
        limpar()
        if medida == "5.0":
            print(f"O valor de entrada em Centimetros Quadrados convertido para Metros Quadrados é: {centimetros_quadrados_metros_quadrados()}")
        elif medida == "5.1":
            print(f"O valor de entrada em Centimetros Quadrados convertido para Hectare é: {centimetros_quadrados_hectare()}")
        elif medida == "5.2":
            print(f"O valor de entrada em Metros Quadrados convertido para Centimetros Quadrados é: {metros_quadrados_centimetros_quadrados()}")
        elif medida == "5.3":
            print(f"O valor de entrada em Metro Quadrados convertido para Hectare é: {metros_quadrados_hectare()}")
        elif medida == "5.4":
            print(f"O valor de entrada em Hectare convertido para Centimetros Quadrados é: {hectare_centimetros_quadrados()}")
        elif medida == "5.5":
            print(f"O valor de entrada em Hectare convertido para Metros Quadrados é: {hectare_metros_quadrados()}")
        elif medida == "0":
            print("Obrigado por usar o sistema de conversão. Até mais!")
            input()
            break
        else:
            print("Opção inválida!")
    
    else:
        print("Opção inválida!")
