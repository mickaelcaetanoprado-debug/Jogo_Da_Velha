def interface():
    print("    0   1   2")
    print("0 [{}] [{}] [{}]".format(tabuleiro[0][0], tabuleiro[0][1], tabuleiro[0][2]))
    print("1 [{}] [{}] [{}]".format(tabuleiro[1][0], tabuleiro[1][1], tabuleiro[1][2]))
    print("2 [{}] [{}] [{}]".format(tabuleiro[2][0], tabuleiro[2][1], tabuleiro[2][2]))


def verificar_vencedor():
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " ":
            return tabuleiro[0][i]

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return tabuleiro[0][2]

    return None


tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

parar = False
rodada = "X"
jogadas = 0

while parar == False:
    interface()

    linha = int(input("Digite a linha: "))
    coluna = int(input("Digite a coluna: "))

    if linha not in (0, 1, 2) or coluna not in (0, 1, 2):
        print("Posição inválida! Use valores de 0 a 2.")
        continue

    if tabuleiro[linha][coluna] != " ":
        print("Essa posição já está ocupada! Escolha outra.")
        continue

    if rodada == "X":
        tabuleiro[linha][coluna] = "X"
        jogadas += 1
        rodada = "O"
    elif rodada == "O":
        tabuleiro[linha][coluna] = "O"
        jogadas += 1
        rodada = "X"

    vencedor = verificar_vencedor()
    if vencedor is not None:
        interface()
        print("Jogador {} venceu!".format(vencedor))
        parar = True
    elif jogadas == 9:
        interface()
        print("Empate!")
        parar = True

print("Programa Encerrado!")