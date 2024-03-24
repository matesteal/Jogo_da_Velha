import math

def formato_velha(linha):
    print(f"{linha[1]} | {linha[2]} | {linha[3]}")
    print(f"{linha[4]} | {linha[5]} | {linha[6]}")
    print(f"{linha[7]} | {linha[8]} | {linha[9]}")

def checar_vencedor(linhas, jogador):
    for i in range(1, 9, 3):
        if all(linhas[i+j] == jogador for j in range(3)):
            return True
    for i in range(1, 4):
        if all(linhas[i+j] == jogador for j in range(0, 7, 3)):
            return True
    if all(linhas[i] == jogador for i in range(1, 10, 4)) or all(linhas[i] == jogador for i in range(3, 8, 2)):
        return True
    return False








#Em testes
def Media(): 
    jogador1 = 0
    jogador2 = 0
    rodada = 0

    while True:
        rodadas = int(input("melhor de... "))
        if rodadas % 2 != 0:
            break
        else:
            print("Apenas valores Impares")
    valor_dividido = rodadas / 2
    valor_melhor_de = math.ceil(valor_dividido)

    while jogador2 < valor_melhor_de and jogador1 < valor_melhor_de:
        if rodada >= rodadas:
            break