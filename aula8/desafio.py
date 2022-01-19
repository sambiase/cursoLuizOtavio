'''
    criar variaveis para nome (str) e idade (int)
    altura (float) e peso (float) de uma pessoa
    criar variavel com ano atual (int)
    Obter o ano de nasc da pessoa (baseado na idade e no ano atual)
    Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
    Exibir um texto com todos os valores na tela usando F-string
'''

nome = str(input('Digite o seu nome: '))
idade = int(input('Digite a sua idade: '))
altura = float(input('Digite a sua altura: '))
peso = float(input('Digite s seu peso: '))
ano_atual = 2021
ano_nasc = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}Kg.')
print(f'O IMC de {nome} eh {imc:.2f}')
print(f'{nome} nasceu em {ano_nasc}')
