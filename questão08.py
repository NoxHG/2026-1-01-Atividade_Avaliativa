#QUESTÃO8
print('insira 4 números')
n1 = int(input('insira um número: '))
n2 = int(input('insira um número: '))
n3 = int(input('insira um número: '))
n4 = int(input('insira um número: '))
print(f'a soma dos 4 números é: {(n1 + n2 + n3 + n4)}')

if (n1 + n2 + n3 + n4) > 100:
   print('a soma é maior que 100.')
else:
  print('a soma é igual ou menor que 100.')
