print('Bem-vindo ao DETRAN!')
print('Vamos descobrir se tem permissão para tirar ou não a CNH')
print()
idade = int(input('Digite sua idade: ')) #converter para int

if idade >= 18:
    print('Tem permissão para tirar a CNH!')
else: 
    print('Quando atingir a maioridade (18  anos), volte aqui!')

print()
print('FIM DO TESTE!')