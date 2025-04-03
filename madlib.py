# MadLib é um jogo de palavras divertido e interativo em que um jogador preenche espaços em branco em um texto com palavras aleatórias de determinadas categorias (como substantivos, verbos, adjetivos, etc.) antes de ler a história completa. Como os participantes escolhem as palavras sem conhecer o contexto exato da história, o resultado costuma ser engraçado e absurdo.

#Esse jogo é muito usado para entretenimento, aprendizado de gramática e até como ferramenta de criatividade.
import sys
sys.stdout.reconfigure(encoding="utf-8")


print('Boas vindas ao nosso jogo de MADLIB')
print()
substantivo = input('Digite um NOME: ')
adjetivo = input('Digite um ADJETIVO: ')
verbo = input('Digite um VERBO: ')
objeto = input('Digite um OBJETO: ')
profissao = input('Digite uma PROFISSÃO: ')
adjetivo2 = input('Digite um NOVO ADJETIVO: ')
numero = input('Digite um NÚMERO: ')
animal = input('Digite um ANIMAL: ')
objeto2 = input('Digite um NOVO OBJETO: ')
objeto3 = input('Digite um NOVO OBJETO: ')

print()
print('A Grande Aventura no Escritória de Tecnologia')
print()

print('Um dia, o(a) ' + substantivo + ' estava trabalhando em um projeto super ' + adjetivo + '. De repente, o computador começou a ' + verbo + ' sozinho! Sem pensar duas vezes, o(a) '  + substantivo + ' pegou seu ' + objeto + ' e começou a digitar comandos como um(a) verdadeiro(a) ' + profissao)
print()
print(substantivo + ' exclamou...')
input()
print('"Preciso consertar isso antes que o sistema fique ' + adjetivo2 + '!"')
print()
print('Depois de ' + numero + ' tentativas, finalmente o computador respondeu: "O problema foi causado por um ' + animal + ' que estava no sistema!"')
print()
print('Com isso, o problema foi resolvido, e o(a) ' + substantivo + ' ganhou o prêmio de ' + objeto2 + ' mais inovador do ano. Moral da história: sempre leve seu ' + objeto3 + ' para o escritório, porque nunca se sabe quando você vai precisar!')
