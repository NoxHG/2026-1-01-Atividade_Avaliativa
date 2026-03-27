#QUESTÃO7
print('Insira 4 notas suas.')
[n1, n2, n3, n4] = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
# n1 = float(input(n1))
# n2 = float(input(n2))
# n3 = float(input(n3))
# n4 = float(input(n4))
média = (n1 + n2 + n3 + n4) / 4
print(f'A média aritimética é: {média}', f'A diferença do primeiro para o ulitmo é: {n1/n4}', sep='\n')
