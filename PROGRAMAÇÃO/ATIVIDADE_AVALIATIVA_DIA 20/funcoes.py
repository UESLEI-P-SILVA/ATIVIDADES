import os
def limpar():
    os.system('cls')

def verificar_numero(valor):
    partes = valor.split('.')
    
    if len(partes) == 2:
        if not (partes[0].isdigit() or partes[0] == '') or not partes[1].isdigit():
            return "Erro: Por favor, insira um valor numérico decimal válido."
    
    elif len(partes) == 1:
        
        if not partes[0].isdigit():
            return "Erro: Por favor, insira um valor numérico inteiro válido."
    
    else:
        return "Erro: Valor inválido."
    
    return "Valor válido."

#O método isdigit() em Python é um método de string que verifica se todos os
#caracteres na string são dígitos. Ou seja:
#'12345'.isdigit() retorna True porque todos os caracteres são dígitos.
#'12.34'.isdigit() retorna False porque o ponto (.) não é um dígito.
#'123a'.isdigit() retorna False porque o caractere 'a' não é um dígito.

# Funções de conversão

def centimetro_metro():
    valor = input("Digite o valor em Centímetros: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) / 100
    

def centimetro_quilometro():
    valor = input("Digite o valor em Centímetros: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) / 100000

def metro_centimetro():
    valor = input("Digite o valor em Metros: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) * 100

def metro_quilometro():
    valor = input("Digite o valor em Metros: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) / 1000

def quilometro_centimetro():
    valor = input("Digite o valor em Quilômetros: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) * 100000

def quilometro_metro():
    valor = input("Digite o valor em Quilômetros: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) * 1000

def mililitro_litro():
    valor = input("Digite o valor em Mililitros: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) / 1000

def litro_mililitro():
    valor = input("Digite o valor em Litros: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) * 1000

def grama_quilograma():
    valor = input("Digite o valor em Gramas: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) / 1000

def grama_tonelada():
    valor = input("Digite o valor em Gramas: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) / 1000000

def quilograma_grama():
    valor = input("Digite o valor em Quilogramas: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) * 1000

def quilograma_tonelada():
    valor = input("Digite o valor em Quilogramas: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) / 1000

def tonelada_grama():
    valor = input("Digite o valor em Toneladas: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) * 1000000

def tonelada_quilograma():
    valor = input("Digite o valor em Toneladas: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) * 1000

def celsius_fahrenheit():
    valor = input("Digite o valor em Celsius: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return (float(valor) * 9/5) + 32

def celsius_kelvin():
    valor = input("Digite o valor em Celsius: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) + 273.15

def fahrenheit_celsius():
    valor = input("Digite o valor em Fahrenheit: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return (float(valor) - 32) * 5/9

def fahrenheit_kelvin():
    valor = input("Digite o valor em Fahrenheit: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return ((float(valor) - 32) * 5/9) + 273.15

def kelvin_celsius():
    valor = input("Digite o valor em Kelvin: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) - 273.15

def kelvin_fahrenheit():
    valor = input("Digite o valor em Kelvin: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return ((float(valor) - 273.15) * 9/5) + 32

def centimetros_quadrados_metros_quadrados():
    valor = input("Digite o valor em Centímetros Quadrados: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) / 10000

def centimetros_quadrados_hectare():
    valor = input("Digite o valor em Centímetros Quadrados: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) / 100000000

def metros_quadrados_centimetros_quadrados():
    valor = input("Digite o valor em Metros Quadrados: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) * 10000

def metros_quadrados_hectare():
    valor = input("Digite o valor em Metros Quadrados: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) / 10000

def hectare_centimetros_quadrados():
    valor = input("Digite o valor em Hectares: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) * 100000000

def hectare_metros_quadrados():
    valor = input("Digite o valor em Hectares: ")
    mensagem = verificar_numero(valor)
    if mensagem != "Valor válido.":
        return mensagem
    return float(valor) * 10000

