# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.
# Gabarito da Prova:
# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A
# Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
import os

print('Bem-vindo ao controle de notas')
print('******************************')
print()

gabarito = []
notas_alunos = []

def professor():
    global gabarito
    questoes = int(input('Professor, quantas questões tem na prova? '))
    print()
    print('Gabarito da Prova:')

    for cont in range(questoes):
        resposta = input(f'{cont + 1}: ').upper()  # Converter para maiúsculo para facilitar a comparação
        gabarito.append(resposta)
    os.system('clear')
    aluno()

def aluno():
    global notas_alunos
    questoes = len(gabarito)  # Usar o tamanho do gabarito definido pelo professor
    respostas_aluno = []
    acertos = 0
    print('Responda as questões:')
    for cont in range(questoes):
        resposta = input(f'{cont + 1}: ').upper()  # Converter para maiúsculo para facilitar a comparação
        respostas_aluno.append(resposta)

    for i in range(questoes):
        if respostas_aluno[i] == gabarito[i]:
            acertos += 1

    notas_alunos.append(acertos)
    print(f'\nVocê acertou {acertos} questões e sua nota é {acertos}!')

    inserir = input('Tem mais alunos para inserir as respostas (s/n)? ')

    if inserir.lower() == 's':
        aluno()
    else:
        print('\nAgora vamos aos resultados...')
        mostrarResultados()

def mostrarResultados():
    if not notas_alunos:
        print('Nenhum aluno respondeu a prova.')
        return

    maior_acerto = max(notas_alunos)
    menor_acerto = min(notas_alunos)
    total_alunos = len(notas_alunos)
    media_notas = sum(notas_alunos) / total_alunos

    print('\n----- Resultados da Turma -----')
    print(f'Maior Acerto: {maior_acerto}')
    print(f'Menor Acerto: {menor_acerto}')
    print(f'Total de Alunos: {total_alunos}')
    print(f'Média das Notas da Turma: {media_notas:.2f}')
    print('------------------------------')

professor()