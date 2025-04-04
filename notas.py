print('APROVADO, REPROVADO OU RECUPERAÇÃO - NOTAS')
print('--------------------------------------------------')
nota = int(input('Digite sua nota: '))
print()

if nota >= 7:
    print('Aprovado!')
elif nota < 5:
    print('Reprovado!')
else:
    print('Recuperação... ')
        
print()
print('BORA ESTUDAAAAR! :)')