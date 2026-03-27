#QUESTÃO11
alunos = []

for i in range(15):
    n1, n2, n3, n4, nome = input('Insira as 4 notas, e Nome do aluno. "1 2 3 4 Fulano"\n').split()
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    n4 = int(n4)
    nome = str(nome)

    media = (n1 + n2 + n3 + n4) / 4

if media >= 6:
    sa = 'Aprovado'
elif media == 4 <= 4 <= 6:
    sa = 'Recuperação'
elif media <= 4:
    sa = 'Reprovado'

for aluno in alunos:
    print(f'1n - {n1}, 2n - {n2}, 3n - {n3}, 4n - {n4}, Média: {media}, Situação: {sa}, {nome}', end=';')
    # ESSA MERDA N FUNCIONA 
    # :D
