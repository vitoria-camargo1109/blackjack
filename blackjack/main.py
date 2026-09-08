import random
print("----Bem-vindo ao jogo de Blackjack!----\n")

'''
print("Regras do jogo:\n")
print("1. O objetivo é ter um valor de carta mais próximo de 21 possível, sem exceder.")
print("2. As cartas numéricas valem o valor indicado.")
print("3. As cartas figura (Valete, Dama, Rei) valem 10.")
print("4. O Ás pode valer 1 ou 11, dependendo do contexto.")
print("5. Se o jogador ultrapassar 21, ele perde.")
print("6. Se o dealer ultrapassar 21, o jogador ganha.")
print("7. Se o jogador tiver um valor mais alto que o dealer sem ultrapassar 21, ele ganha.")
print("8. Se o dealer e o jogador tiverem o mesmo valor, é um empate.")
'''

naipes = ['♥', '♦', '♣', '♠']
cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
#cartas_valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1 or 11}
def criar_baralho():
    baralho = [(c,n) for n in naipes for c in cartas]
    random.shuffle(baralho)
    return baralho

def valor_carta(carta):
    c = carta[0]
    if c in ['J','Q','K']:
        return 10
    if c == 'A':
        return 11
    return int (c)

def valor_mao(mao):
    total = sum(valor_carta(c) for c in mao)
    #Ajusta Áses se estourar 21
    ases = sum(1 for c in mao if c[0] == 'A')
    while total > 21 and ases:
        total -= 10
        ases -= 1
    return total

baralho = criar_baralho()
mao_jogador = [baralho.pop(), baralho.pop()]
print('Sua mão:', mao_jogador, 'total', valor_mao(mao_jogador))
