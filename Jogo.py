#Main code
import Functions as fc
import time

jogadorX = input("Nome do jogador que será o X: ")
jogadorO = input("Nome do jogador que será o O: ")
time.sleep(0.5)
print("Bem vindos ao jogo,",jogadorX, "e", jogadorO)

jogadores = [jogadorX, jogadorO]
jogo = ['X','O']
pont_jog = [0, 0]

while True:
    jogador_atual = 0
    tabuleiro = [" "]*10
    while True:
        try:
            fc.formato_velha(tabuleiro)
            posicao = int(input(f"Jogador(a) {jogadores[jogador_atual]}-{jogo[jogador_atual]}, escolha uma posição de 1 a 9: "))
        except ValueError:
            print("Use apenas numeros inteiros")
            continue
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
        
        if all(celula != " " for celula in tabuleiro[1:]):
            fc.formato_velha(tabuleiro)
            print("Empate!")
            break
        
        jogador_atual = (jogador_atual + 1) % 2
    time.sleep(0.25)
    fc.resultados(jogadorX, pont_jog, jogadorO, tabuleiro)
    
    limpar_arquivo = input("Deseja limpar o arquivo de texto(S/N)? ") 
    if limpar_arquivo == 'S':
        fc.limpar()
    
    again = input("Mais uma (S/N)? ")
    if again == 'S':
        continue
    
    else:
        break
        