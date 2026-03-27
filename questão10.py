#QUESTÃO10
#Escreva um programa Python que leia 4 números inteiros e use o if else para verificar se a média deles é maior ou igual a 6. 
#Exiba dois prints usando f-string: um com o valor da média e outro indicando se o aluno foi aprovado (média ≥ 6) ou reprovado (média < 6).]

n1 = int(input('insira uma nota: '))
n2 = int(input('insira uma nota: '))
n3 = int(input('insira uma nota: '))
n4 = int(input('insira uma nota: '))
m = (n1 + n2 + n3 + n4) / 4

print(f'A média é: {m}')

if m >= 6:
    sa = 'Aprovado'
else:
    sa = 'Reprovado'

print(f'Situação: {sa}!')
