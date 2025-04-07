# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
# Use a função len(string) para saber o tamanho de um texto (número de caracteres).


nome = input('Digite seu nome: ')
while len(nome) <= 3:
    nome = input('Digite seu nome [MAIOR QUE 3 CARACTERES]: ')
    print()
    
idade = int(input('Digite sua idade: '))
while (idade <= 0) or (idade >= 150):
    idade = int(input('Digite sua idade [ENTE 0 e 150]: '))
    print()
    
salario = float(input('Digite seu salário: '))
while salario <= 0:
    salario = float(input('Digite seu salário [MAIOR QUE 0]: '))
    
sexo = input('Qual é seu sexo (f/m)? ')
while sexo.lower() != 'f' and sexo.lower() != 'm':
    sexo = input('Digite seu sexo [f OU m]: ')
    print()
    
estadoCivil = input('Qual é seu estado civil? ')
while estadoCivil.lower() != 's' and estadoCivil.lower() != 'c' and estadoCivil.lower() != 'v' and estadoCivil.lower() != 'd':
    estadoCivil = input('Digite um estado civil válido [s, c, v, d]: ')
    print()