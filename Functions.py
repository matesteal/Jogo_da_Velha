import time

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