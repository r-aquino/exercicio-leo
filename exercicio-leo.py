# 1) Faça um Programa que solicite a temperatura em graus Celsius e a transforme em graus Fahrenheit exibindo na tela.
# #°F = (°C x 1,8) + 32
# grausC = float(input("Insira a temperatura em ºC: "))
# while :
#     grausC = float(input("Insira a temperatura em ºC: "))
# farenheit = (grausC * 1.8) + 32
# print(farenheit)

# 2) Sabendo que o dólar comercial está a ( R$ 5,49 ) na cotação do dia
# Faça um programa que leia o dinheiro que possui na carteira em ( R$ Real ) e converta para ( $ Dólar )
# while True:
#     try:       
#         carteira = float(input("Insira suas moedas: "))
            
#     except: 
#         print("Insira um número em reais.")
#         continue
#     cotacaodolar = 5.49
#     print(f"Você possui $ {carteira/cotacaodolar:.2f} ")
#     break

# 3) Desenvolve um programa que leia um número com até 4 casas decimais
# e que retorne informando qual é o número de cada casa decimal.
# Exemplo: 1258
# Milhar: 1
# Centena: 2
# Dezena: 5
# Unidade: 8

# numero = input("Insira um numero: ")
# b = len(numero)
# c = 0 
# while c != b:
#     print(numero[c])
#     c += 1

# 4) Faça um programa que permita ler vários números:
# Para sair do programa, será necessário digitar o número 0.
# Após sair, mostre quantos números foram digitados e qual foi a soma entre eles


# lista = []
# while True:
#     try:
#         num = float(input("Insira um número: "))
#     except:
#         continue    
#     lista.append(num)
#     if num == 0:
#         break
# print(lista) 
# print(len(lista))
# print(sum(lista))

# 6) Desenvolva um programa que solicite a quantidade de dias que o veículo foi alugado
# e a quantidade kilometros percorridos.
# Sabendo que o veículo custa R$58 a diária e R$0,21 por km rodado, calcule o total gasto

# qdias, km = int(input("Insira o número de dias: ")), int(input("Insira a qtd de km: "))
# print(f"O total gasto foi {qdias * 58 + km * 0.21}")

# 8) Faça um programa que permite ler um número e escolhar uma das seguintes conversões:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

# numero = int(input("Insira um número: "))
# conversao = input("Insira \n1 para binário\n2 para octal\n3 para hexadecimal ")
# if conversao == "1":
#     numero = format(numero, "b")
# elif conversao == "2":
#     numero = oct(numero)[2:]
# elif conversao == "3":
#     numero = hex(numero)[2:]
# print(numero)

# 5)  Escreva um programa que leia um número e mostre o seu fatorial.
#  Exemplo: Número 5 = 5 x 4 x 3 x 2 x 1 = 120

# numero = int(input("Fatorial de: ") )
# resultado=1
# count=1
# while count <= numero:
#     resultado *= count
#     count += 1
# print(resultado)

# ou ---------------------

# n1 = int(input('Digite um numero : '))
# fat = 1
# for c in range(n1, 0, -1):
#     print(c, end='')
#     print(' x 'if c > 1 else ' = ',end='')
#     fat = fat * c
# print(fat)


# 7 Faça um programa que leia a velocidade de vários veículos.
# Se ultrapassar 80 Km/h, reporte a mensagem informando que foi multado.
# O valor da multa é R$ 45,00 por cada Km acima do limite.
# Para sair do programa, será necessário digitar sair


# while True:
#     try: 
#         veloc = float(input("Insira uma velocidade: "))
#     except:
#         continue    
#     if veloc > 80:   
#         excesso = veloc - 80
#         print("Multa do veículo é", excesso * 45)
#     else:        
#         print("Veículo dentro da velocidade")
#     pergunta = input("Deseja continuar? [Cont] ou [Sair] ").upper()
#     if pergunta == "CONT":
#         continue
#     elif pergunta == "SAIR":
#         break
#     else:
#         print("Resposta inválida")
    
# print("Fim")
