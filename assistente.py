print('Olá, eu sou a sua assistente, Pythrina. O que deseja fazer hoje?')

comando = input('Digite um comando: ')

match comando: 
    case 'oi' | 'olá':
        print('Oi, tudo bem?')
    case 'tchau' | 'sair' | 'fim' | 'exit':
        print('Tchau, foi um prazer te conhecer!')
    case 'piada':
        print('Sabe o que um pitinho falou para o outro? Piu HAHAHAAHAHA')
    case 'clima' | 'tempo' | 'previsão do tempo':
        print('Tá muitoooo quente!!! Use protetor solar... 🥵')
    case _:
        print('Desculpa não consegui entender o comando.')