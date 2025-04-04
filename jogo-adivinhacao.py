# Jogo de adivinhação de animais... 
# Aplicando variáveis, listas e estruturas condicionais

perguntas = [ ['Seu animal gosta de bananas', 'macaco'] ]

print('Bem-vindo ao jogo de adivinhação!')
print('************************************')
print()

while True:
    print('Pense em um animal...')

    acertou = False
    for pergunta in perguntas:
        resposta = input(f'{pergunta[0]} (s/n): ')
        if resposta.lower() == 's':
            print(f'Você pensou em {pergunta[1]}!')
            acertou = True
            break

    if acertou == False: 
        animal = input('Desisto! Em qual animal pensou? ')
        print()
        novapergunta = input('Qual pergunta você faria para diferenciar esse animal? ')

        perguntas.append([novapergunta, animal])
        print()
        resposta = input('Quer jogar novamente? (s/n): ')
        if resposta.lower() != 's':
            print('Ok! Foi bom jogar com você!')
            break