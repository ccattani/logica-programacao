estudantes = {
    1: {'nome': 'Joana', 'idade': 45, 'curso': 'Computação'},
    2: {'nome': 'Ivan', 'idade': 70, 'curso': 'Direito'},
    3: {'nome': 'João', 'idade': 12, 'curso': 'Computação'},
}

cursos = {'Computação', 'Matemática', 'Direito'}

estudantes_cursos = {
    'Computação': {1, 3},
    'Direito': {2}
}

def adicionarEstudante(matricula, nome, idade, curso):
    pessoa = {'nome': nome, 'idade': idade, 'curso': curso}
    estudantes[matricula] = pessoa
    if curso not in estudantes_cursos:
        estudantes_cursos[curso] = set()
    estudantes_cursos[curso].add(matricula)

# print(estudantes_cursos)
# adicionarEstudante(5, 'João', 89, 'Computação')
# print(estudantes_cursos)
# adicionarEstudante(6, 'Maria', 55, 'Matemática')
# print(estudantes_cursos)

print(f'Todas as pessoas matriculadas em algum curso: {estudantes_cursos['Computação'] - estudantes_cursos['Direito']}')