def formato_velha(linha):
    print(f"{linha[1]} | {linha[2]} | {linha[3]}")
    print(f"{linha[4]} | {linha[5]} | {linha[6]}")
    print(f"{linha[7]} | {linha[8]} | {linha[9]}")
    
    return f"{linha[1]} | {linha[2]} | {linha[3]}\n{linha[4]} | {linha[5]} | {linha[6]}\n{linha[7]} | {linha[8]} | {linha[9]}\n"

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

def resultados(J1, Pont, J2, Tab):
    print(f"{J1} ({Pont[0]}) X {J2} ({Pont[1]})")
    tabuleiro_str = str(formato_velha(Tab))
    
    with open('resultados.txt', 'a') as resultados:
        resultados.write(f"{J1} ({Pont[0]}) X {J2} ({Pont[1]})\n")
        resultados.write(tabuleiro_str)

def limpar():
    open('resultados.txt', 'w')