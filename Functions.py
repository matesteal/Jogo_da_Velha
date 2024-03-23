def Media():
    import math
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