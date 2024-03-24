import Functions as fc
import time
import sys

jogadorX = input("Nome do jogador que será o X: ")
jogadorO = input("Nome do jogador que será o O: ")
time.sleep(0.5)
print("Bem vindos jogo,",jogadorX, "e", jogadorO)

jogadores = [jogadorX, jogadorO]
jogo = ['X','O']
pont_jog = [0, 0]
jogador_atual = 0

while True:
    tabuleiro = [" "]*10
    while True:
        fc.formato_velha(tabuleiro)
        posicao = int(input(f"Jogador(a) {jogadores[jogador_atual]}-{jogo[jogador_atual]}, escolha uma posição de 1 a 9: "))
        time.sleep(0.5)

        if tabuleiro[posicao] != " ":        
            print("Essa posição já está ocupada.")
            time.sleep(0.1)
            continue
        
        tabuleiro[posicao] = jogo[jogador_atual]
        
        if fc.checar_vencedor(tabuleiro, jogo[jogador_atual]):
            fc.formato_velha(tabuleiro)
            print(f"Jogador(a) {jogadores[jogador_atual]}-{jogo[jogador_atual]} venceu!")
            pont_jog[jogador_atual] += 1
            break
        
        if all(celula != " " for celula in tabuleiro):
            fc.formato_velha(tabuleiro)
            print("Empate!")
            break
        
        jogador_atual = (jogador_atual + 1) % 2
    again = input("Mais uma (S/N)? ")
    if again == 'S':
        time.sleep(0.25)
        continue
    else:
        time.sleep(0.25)
        with open('Resultado.txt','w') as arquivo_salvo:
            sys.stdout = arquivo_salvo
            print(f"{jogadorX} ({pont_jog[0]}) X {jogadorO} ({pont_jog[1]})")
            fc.formato_velha(tabuleiro)
            break