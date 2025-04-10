lista = None

def exibeLista():
    if not lista:
        print('Lista vazia!')
        return
    elemento = lista
    
    while elemento != None:
        print(f'{elemento['valor']}', end=' ')
        elemento = elemento['próximo']

    print('.')

def adicionaNoFim(elemento):
    global lista
    if not lista:
        lista = {'valor': elemento, 'próximo': None}
        return
    atual = lista
    while atual['próximo']:
        atual = atual['próximo']
    atual['próximo'] = {'valor': elemento, 'próximo': None}


exibeLista()
print('Adicionando o 5...')
adicionaNoFim(5)
exibeLista()
print('Adicionando o 8...')
adicionaNoFim(8)
print('Adicionando o 13...')
adicionaNoFim(13)
exibeLista()

# print(lista)