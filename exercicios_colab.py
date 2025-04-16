# -*- coding: utf-8 -*-
"""Exercícios de python

Original file is located at
    https://colab.research.google.com/drive/1BptVUd4B45teqxqBaJTe6GwDF-jRpPn0
"""

# Pede ao usuário para digitar dois números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Realiza os cálculos
potencia = num1 ** num2  # Exponenciação
modulo = num1 % num2  # Resto da divisão
divisao_inteira = num1 // num2  # Parte inteira da divisão

# Exibe os resultados formatados
print(f"\n{num1} elevado a {num2} = {potencia}")
print(f"O resto da divisão de {num1} por {num2} = {modulo}")
print(f"A parte inteira da divisão de {num1} por {num2} = {divisao_inteira}")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

potencia = num1**num2
modulo = num2%num3
divisao_inteira = num1//num3

print(f"\n{num1} elevado a {num2} = {potencia}")
print(f"O resto da divisão de {num2} por {num3} = {modulo}")
print(f"A parte inteira da divisão de {num1} por {num3} = {divisao_inteira}")

# Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print("Olá, %s, você tem %d e mede %.2f ." % (nome, idade, altura))



# Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print(f"Olá, {nome}, você tem {idade} e mede {altura} .")

# Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.
num1 =int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
print(f"A soma de {num1} e {num2} é {soma}.")

#Crie um código que solicita 3 notas de um estudante e imprima a média das notas.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1+nota2+nota3)/3
print(f"A média das notas é {media}")

#Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.
media_ponderada = (5*1+12*2+20*3+15*4)/10
print(f"A média ponderada é {media_ponderada}")

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.
frase = (input("Digite uma frase: "))
print(frase.upper())

#Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.
frase = "      Eu amo meu amor    "
print(frase.strip())

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.
frase = input("Digite uma frase sobre você: ")
print(frase.replace("a", "@"))

frase = input('Digite uma frase: ')
print(frase.lower().replace('s',chr(36)))

#Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 > num2:
  print(f"O número maior é {num1}")
else:
  print(f"O número maior é {num2}")

# Solicita o percentual de crescimento da produção
percentual = float(input("Digite o percentual de crescimento de produção: "))

# Verifica se houve crescimento ou decrescimento
if percentual > 0:
    print("Houve um crescimento")
else:
    print("Houve um decrescimento")

#Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.
vogal = input("Digite uma letra: ")
if vogal == "a" or "e" or "i" or "o" or "u":
  print("É uma vogal!")
else:
    print("É uma consoante")

#Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.
ano1 = float(input("Digite o preço do carro no primeiro ano: "))
ano2 = float(input("Digite o preço do carro no segundo ano:"))
ano3 = float(input("Digite o preço do carro no terceiro ano: "))
if ano1>ano2 and ano1>ano3:
  print(f"O preço mais alto é {ano1}")
elif ano2>ano1 and ano2>ano3:
  print(f"O preço mais alto é {ano2}")
elif ano3>ano1 and ano3>ano2:
  print(f"O preço mais alto é {ano}")

if ano1<ano2 and ano1<ano3:
  print(f"O preço mais baixo é {ano1}")
elif ano2<ano1 and ano2<ano3:
  print(f"O preço mais baixo é {ano2}")
elif ano3<ano1 and ano3<ano2:
  print(f"O preço mais baixo é {ano3}")

#Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.
produto1 = float(input("Digite o preço do primeiro produto: "))
produto2 = float(input("Digite o preço do segundo produto: "))
produto3 = float(input("Digite o preço do terceiro produto: "))
if produto1<produto2 and produto1<produto3:
  print(f"O produto mais barato é o primeiro produto que custa {produto1}")
elif produto2<produto1 and produto2<produto3:
    print(f"O produto mais barato é o segundo produto que custa {produto2}")
elif produto3<produto1 and produto3<produto2:
      print(f"O produto mais barato é o terceiro produto que custa {produto3}")

# Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.
num = int(input("Digite um número inteiro: "))
if num%2 == 0:
  print(f"O número é par")
else:
  print(f"O número é impar")

#Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.
num = float(input("Digite um número: "))
if num%1 == 0:
  print(f"O número é inteiro")
else:
  print(f"O número é decimal")

total_imoveis = 0

for ano in range(2017,2023):
  quantidade_imoveis = float(input(f'Digite a quantidade de imóveis no ano {ano}: '))
  total_imoveis += quantidade_imoveis

print(f'Total de imóveis construídos: {total_imoveis} imóveis')

#1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1<num2:
  for i in range(num1+1,num2):
    print(i)

#2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.
dias = 0
colônia_a = 4
colônia_b = 10
while colônia_a <= colônia_b:
  colônia_a += colônia_a*0.03
  colônia_b += colônia_b*0.015
  dias += 1
print(f"Serão necessários {dias} dias para que a colônia A ultrapasse a colônia B.")

# número inicial de bactérias
colonia_a = 4
colonia_b = 10

# taxas de crescimento das colônias
taxa_a = 0.03
taxa_b = 0.015

# contador de dias
dias = 0

# A condição que finaliza o laço é o caso em que
# a colônia A ultrapasse a colônia B
while colonia_a <= colonia_b:
  # usamos um operador de atribuição com multiplicação
  colonia_a *= 1 + taxa_a
  colonia_b *= 1 + taxa_b
  # contamos o dia para cada iteração
  dias += 1

# resultado final
print(f'Irá levar {dias} dias para a colônia A ultrapassar a colônia B.')

loja = {'nomes': ['televisão', 'celular', 'notebook', 'geladeira', 'fogão'],
        'precos': [2000, 1500, 3500, 4000, 1500]}
for chave, elementos in loja.items():
  print(f'Chave: {chave}\nElementos:')
  for dado in elementos:
    print(dado)

escolhas = ["Vou", "Não vou"]
from random import choice
escolha = choice(escolhas)
escolha

# 1. Escreva um código para instalar a versão 3.7.1 da biblioteca matplotlib.
!pip install matplotlib==3.7.1

# 2. Escreva um código para importar a biblioteca numpy com o alias np
import numpy as np

#3. Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
from random import choice
numero_aleatorio = choice(lista)
numero_aleatorio

#4. Crie um programa que sorteia, aleatoriamente, um número inteiro positivo menor que 100.
from random import randrange
numero_aleatorio = randrange(100)
numero_aleatorio

#5. Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.
from math import pow
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
potencia = pow(num1,num2)
print(f"{num1} elevado a {num2} é igual a {potencia}")

#6. Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes. Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para ela o número sorteado.
from random import randrange
participantes = int(input("Digite o número de participantes: "))
numero_sorteado = randrange(participantes)
print(f"O número sorteado é {numero_sorteado}")

#7. Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa. O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita à pessoa usuária o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.
from random import randrange

nome = input("Qual o seu nome? ")
# Gerando um token par de 1000 a 9998. O randrange tem o intervalo aberto em 10000, ou seja,
# não considera 10000 como opção de escolha (token >= 1000 e token < 10000)
token = randrange(1000, 10000, 2)

print(f"Olá, {nome}, o seu token de acesso é {token}! Seja bem-vindo(a)!")

#Para diversificar e atrair novos(as) clientes, uma lanchonete criou um item misterioso em seu cardápio chamado "salada de frutas surpresa". Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 para compor a salada de frutas da pessoa cliente. Crie o código que faça essa seleção aleatória de acordo com a lista abaixo:

frutas = ["maçã", "banana", "uva", "pêra",
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]
from random import choices
salada_de_frutas = choices(frutas, k=3)
print(f"A salada de frutas surpresa é {salada_de_frutas}")

cafe_manhã = ["Pão com queijo", "Ovo cozido", "Ovo mexido", "banana com iogurte", "maça com iogurte"]
from random import choice
comida = choice(cafe_manhã)
print(f"Amanhã você irá comer {comida} de café da manhã!")

peso = float(input("Digite o peso, em quilogramas: "))
altura = float(input("Digite a altura, em metros: "))

imc = round(peso / pow(altura, 2), 2)

print(f"O IMC da pessoa é: {imc}")

# Lista gerada
lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

# Lendo o tamanho, maior e menor número e soma, respectivamente, utilizando as built-in functions
tam = len(lista)
maior = max(lista)
menor = min(lista)
soma = sum(lista)

# Exibindo o texto
print(f"A lista possui {tam} números em que o maior número é {maior} e o menor número é {menor}. A soma dos valores  presentes nela é igual a {soma}.")

# Requisitando o número
num = int(input("Digite um número inteiro de 1 a 10:"))

# Gerando a função tabuada()
def tabuada(numero: int):
  print(f'Tabuada do {numero}:')
  for i in range(11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')

# lendo a tabuada do número escolhido
tabuada(num)

# Lista dos números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função lambda que eleva um número ao quadrado
quadrado = lambda x: x ** 2

# Utilizando a função map() para aplicar a função lambda em cada número da lista
resultado = list(map(quadrado, numeros))
resultado

# declarando a lista de notas
notas = []
# laço for para pedir as 5 notas e armazená-las na lista notas
for i in range(1,6):
  nota = float(input(f"Digite a {i}ª nota: "))
  notas.append(nota)

# Função para remover a maior e menor nota e retornar a média das notas restantes
def media(lista):
  lista.remove(max(lista))
  lista.remove(min(lista))
  return sum(lista) / len(lista)

# Chamando a função e imprimindo a nota da(o) skatista
media = media(notas)
print(f"Nota da manobra: {round(media, 1)}")

# declarando a lista de notas
notas = []
# laço for para pedir as 4 notas e armazená-las na lista notas
for i in range(1,5):
  nota = float(input(f"Digite a {i}ª nota: "))
  notas.append(nota)

def cadastro(lista):
  maior = max(lista)
  menor = min(lista)
  media = sum(lista) / len(lista)
  if media >= 6:
    situacao = "Aprovado(a)"
  else:
    situacao = "Reprovado(a)"

  return (media, maior, menor, situacao)

media, maior, menor, situacao = cadastro(notas)

print(f"O(a) estudante obteve uma media de {media}, com a sua maior nota de {maior} pontos e a menor nota de {menor} pontos e foi {situacao}")

# Nomes dos estudantes
nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

# Função lambda que recebe duas listas e itera em cada uma concatenando seu nome e sobrenome
# na forma desejada
nome_completo = map(lambda nome, sobrenome: f'{nome.title()} {sobrenome.title()}', nomes, sobrenomes)

# Leitura do objeto mapa(iterável)
for n in nome_completo:
  print(f'Nome completo: {n}')

dias = int(input("Quantas diárias? "))
cidade = input("Qual a cidade? [Salvador, Fortaleza, Natal ou Aracaju]: ")
distancias = [850, 800, 300, 550]
passeio = [200, 400, 250, 300]
km_l = 14
gasolina = 5

def gasto_hotel(dias):
    return 150 * dias

def gasto_gasolina(cidade):
    if cidade == "Salvador":
        return (2 * distancias[0] * gasolina) / km_l
    elif cidade == "Fortaleza":
        return (2 * distancias[1] * gasolina) / km_l
    elif cidade == "Natal":
        return (2 * distancias[2] * gasolina) / km_l
    elif cidade == "Aracaju":
        return (2 * distancias[3] * gasolina) / km_l

def gasto_passeio(cidade, dias):
    if cidade=="Salvador":
        return passeio[0] * dias
    elif cidade=="Fortaleza":
        return passeio[1] * dias
    elif cidade=="Natal":
        return passeio[2] * dias
    elif cidade=="Aracaju":
        return passeio[3] * dias

gastos = gasto_hotel(dias) + gasto_gasolina(cidade) + gasto_passeio(cidade, dias)
print(f"Com base nos gastos definidos, uma viagem de {dias} dias para {cidade} saindo de Recife custaria {round(gastos, 2)} reais")

# Requisitando uma frase e separando-a pelos espaços. Usando replace para trocar
# pontuações por espaço.
frase = input("Digite uma frase: ")
frase = frase.replace(',',' ').replace('.',' ').replace('!',' ').replace('?',' ').split()

# Filtrando a frase no formato de lista, passando para a lista tamanho
# apenas as palavras com 5 ou mais caracteres e imprimindo-a na tela
tamanho = list(filter(lambda x: len(x) >= 5, frase))
print(tamanho)

#1. Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:

lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

for lista in lista_de_listas:
    print(sum(lista))

# 2. Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
lista = []
for tupla in lista_de_tuplas:
    lista.append(tupla[2])
print(lista)

#3. A partir da lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento como a posição do nome na lista original e o segundo elemento sendo o próprio nome.
lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']  # redefinindo corretamente

lista_de_tuplas = []
for i in range(len(lista)):
    lista_de_tuplas.append((i, lista[i]))

print(lista_de_tuplas)

#4. Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada tupla caso o primeiro elemento seja 'Apartamento', a partir da seguinte lista de tuplas:

aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
lista = [tupla[1] for tupla in aluguel if tupla[0]== 'Apartamento']
print(lista)

#5. Crie um dicionário usando o dict comprehension em que as chaves estão na lista
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
#e os valores estão em
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]
dicionario = {meses[i]: despesa[i] for i in range(len(meses))}
print(dicionario)

vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]
filtro = [tupla[1] for tupla in vendas if tupla[0] == '2022' and tupla[1] > 6000]
print(filtro)

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
rotulos = [('Hipoglicemia', glicose) if glicose <= 70 else ('Normal', glicose) if glicose < 100 else ('Alterada', glicose) if glicose < 125 else ('Diabetes', glicose) for glicose in glicemia]
print(rotulos)

rotulos = [('Hipoglicemia', glicose) if glicose <= 70, elif ('Normal', glicose) if glicose > 70 and < 100, elif ('Alterada', glicose) if glicose > 100 and < 125, else ('Diabetes', glicose) for glicose in glicemia]
print(rotulos)

#Chegou a hora de você testar os conhecimentos desenvolvidos durante a aula. Continuando com o projeto das laranjas/toranjas agora você deve selecionar parte dos dados. As colunas que iremos avaliar são as de diâmetro e peso. Crie arrays específicos para guardar o diâmetro e peso da laranja e toranja. O diâmetro está na coluna zero e o peso na coluna 1. Os dados referentes a laranja vão até a linha 4999 e os referentes à toranja iniciam na linha 5000 do arquivo.

#Após fazer a seleção de dados, importe a biblioteca matplotlib e crie um gráfico para a laranja e para a toranja do peso pelo diâmetro.
diametro_laranja = dado[:5000,0]
diametro_toranja = dado[5000:,0]
peso_laranja = dado[:5000,1]
peso_toranja = dado[5000:,1]



