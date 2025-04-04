#Estrutura de repetição 

soma = 0
n = 1

# while n <= 10:
#     soma = soma + n
#     n = n + 1
#     print(f'Soma: {soma}')
#     print(f'N: {n}')
# print()
# print('A soma dos números de 1 a 10 é: ', soma)


for i in range(1,11): #range é o intervalo; o i é os números de 1 a 10 
    soma = soma + i

# soma = sum([i for i in range(1,11)])
print('A soma dos números de 1 a 10 é: ', soma)
