def olaMundo():
    print('Olá, mundo!')

olaMundo()

def olaPessoa(nome):
    print(f'Olá, {nome}')

olaPessoa('Cheyenne')

def dobro(numero):
    return numero * 2

print(dobro(4) + 2)

def multiplicaDoisNumeros(a, b = 2):
    """" Multiplica dois números """
    return a * b

print(multiplicaDoisNumeros(3, 4))
print(multiplicaDoisNumeros(3))

x = 5 #Variável global
def soma():
    x = 10 # Variável local
    print(x)
    return x + 1

soma()
print(x)
