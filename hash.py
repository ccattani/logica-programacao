nomes = [
    'João',
    'Antonio',
    'Maria',
    'Emengarda',
    'Ana',
    'Anacleto',
    'Bianca',
    'José',
    'Adão',
    'Josi',
]

tabela = {}

for nome in nomes:
    qtd = nome[0]
    if qtd not in tabela:
        tabela[qtd] = []
    tabela[qtd].append(nome)
    
print(tabela)
