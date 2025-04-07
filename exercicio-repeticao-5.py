# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7

# Vou montar a tabuada de 5 começando em 4 e terminando em 7:
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

tabuada = int(input('Montar a tabuado do número: '))
inicio = int(input('A tabuada deve começar pelo número: '))
fim = int(input('A tabuada deve terminar no número: '))

if inicio > fim: 
    print('O início tem que ser menor que o fim da tabuada que deseja!')
    print()
    inicio = int(input('A tabuada deve começar pelo número: '))
    fim = int(input('A tabuada deve terminar no número: '))
    print()
    for cont in range(inicio - 1, fim):
        print('%d X %d = %d' %(tabuada, cont + 1, tabuada * (cont +1)))

