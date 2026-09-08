print("----Bem-vindo ao jogo de Blackjack!----\n")

print("Regras do jogo:\n")
print("1. O objetivo é ter um valor de carta mais próximo de 21 possível, sem exceder.")
print("2. As cartas numéricas valem o valor indicado.")
print("3. As cartas figura (Valete, Dama, Rei) valem 10.")
print("4. O Ás pode valer 1 ou 11, dependendo do contexto.")
print("5. Se o jogador ultrapassar 21, ele perde.")
print("6. Se o dealer ultrapassar 21, o jogador ganha.")
print("7. Se o jogador tiver um valor mais alto que o dealer sem ultrapassar 21, ele ganha.")
print("8. Se o dealer e o jogador tiverem o mesmo valor, é um empate.")

cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
cartas_valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1 or 11}


