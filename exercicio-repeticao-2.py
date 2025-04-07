# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input('Digite o nome de usuário: ')
senha = input('Digite sua senha: ')

while senha == nome:
    print('Senha inválida, não pode ser a mesma do usuário.')
    print()
    senha = input('Digite uma senha válida: ')

print('Cadastro concluído com sucesso!')