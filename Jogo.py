import Functions as fc
import time

jogador1 = input("Nome do jogador 1: ")
jogador2 = input("Nome do jogador 2: ")
time.sleep(0.5)
print("Bem vindos jogadores,",jogador1, "e", jogador2)

tabuleiro = [" "]*10
jogadores = [jogador1, jogador2]
jogador_atual = 0

fc.formato_velha(tabuleiro)
posicao = int(input(f"Jogador(a) {jogadores[jogador_atual]}, escolha uma posição de 1 a 9: "))

while True:
    if tabuleiro[posicao] != "":        
        print("Essa posição já está ocupada.")
        continue
    
    tabuleiro[posicao] = jogadores[jogador_atual]
    
    if fc.checar_vencedor(tabuleiro, jogadores[jogador_atual]):
        fc.formato_velha(tabuleiro)
        print(f"Jogador(a) {jogadores[jogador_atual]} venceu!")
        break
    if all(celula != " " for celula in tabuleiro):
        fc.formato_velha(tabuleiro)
        print("Empate!")
        break
    
    jogador_atual = (jogador_atual + 1) % 2