# Aprenda a resolver o problema do 'Sapo na Lagoa'! Descubra como um sapo pode atravessar pedras com saltos de 1 ou 2, identificando o padrão da sequência de Fibonacci.

def contar_caminhos(num_pedras):
    if num_pedras <= 1:
        return 1
    else: 
        return contar_caminhos(num_pedras - 1) + contar_caminhos(num_pedras - 2)

print(contar_caminhos(9))

# Irá pegar qual soma anterior você irá somar, nesse caso do 9 pegaria a soma que deu quando foi 8 e 7 e daria o resultado que nesse caso é 55.