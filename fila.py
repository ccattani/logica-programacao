from collections import deque

def criaFila():
    return deque()

def insereNaFila(fila, elemento):
    fila.append(elemento)

def removeDaFila(fila):
    return fila.popleft()

fila = criaFila()

print(fila)
insereNaFila(fila, 8)
insereNaFila(fila, 9)
insereNaFila(fila, 10)
insereNaFila(fila, 11)
insereNaFila(fila, 12)
print(f'Removendo: {removeDaFila(fila)}')
print(f'Removendo: {removeDaFila(fila)}')
print(fila)