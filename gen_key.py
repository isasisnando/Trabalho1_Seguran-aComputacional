"""
GERAÇÃO DE CHAVE S-DES
Esse algoritmo de geração de chave segue o passo a passo descrito no material fornecido (G-SDES)
A função principal é a função gen, que recebe uma chave de 10 bits (string) e retorna duas subchaves de 8 bits (lista de strings)
Dentro dela, são usadas duas funções auxiliares:
    - ls_1: rotação circular à esquerda de 1 bit, separadamente na primeira e na segunda metades de uma string de 10 bits
    - p8: seleciona e permuta 8 bits de uma string de 10 bits
Todas as permutações foram feitas conforme o arquivo G-SDES
"""

def ls_1(p):
    l = p[1:5] + p[0] # primeiros 5 bits
    r = p[6:] + p[5] # últimos 5 bits
    return l+r

def p8(p):
    return p[5] + p[2] + p[6] + p[3] + p[7] + p[4] + p[9] + p[8]

def gen(k):
    p10 = k[2] + k[4] + k[1] + k[6] + k[3] + k[9] + k[0] + k[8] + k[7] + k[5] # permuta os bits de k
    p1 = ls_1(p10) # left shift circular na permutação gerada
    k1 = p8(p1) # seleciona e permuta os bits para gerar k1
    p2 = ls_1(ls_1(p1)) # left shift circular duplo
    k2 = p8(p2) # seleciona e permuta os bits para gerar k2
    return [k1, k2]

#CASO DE TESTE:
# k = "1010000010"
# print(gen(k))