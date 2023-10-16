def print_mapa():
    linha1 = "| {} | {} | {} |".format(mapa[0], mapa[1], mapa[2])
    linha2 = "| {} | {} | {} |".format(mapa[3], mapa[4], mapa[5])
    linha3 = "| {} | {} | {} |".format(mapa[6], mapa[7], mapa[8])
    print(f"\n{linha1}\n{linha2}\n{linha3}")


def rodada_jogador(jogador):
    print(f"Rodada de {jogador}")
    escolha = int(input("Escolha uma casa entre 1~9: "))
    if mapa[escolha - 1] == " ":
        mapa[escolha - 1] = jogador
    else:
        print("O campo ja esta sendo usado")
        rodada_jogador(jogador)


def vitoria(jogador):
    for x in range(3):
        if (
            all(mapa[casa] == jogador for casa in range(x, x + 3))
            or all(mapa[casa] == jogador for casa in range(x, x + 7, 3))
            or (x == 0 and all(mapa[casa] == jogador for casa in range(0, 9, 4)))
            or (x == 2 and all(mapa[casa] == jogador for casa in range(2, 7, 2)))
        ):
            return True
    return False


def empate(mapa):
    if " " not in mapa:
        return True


if __name__ == "__main__":
    mapa = [" " for x in range(9)]
    print(" |1|2|3|\n |4|5|6|\n |7|8|9|\n")
    while True:
        rodada_jogador("X")
        print_mapa()
        if vitoria("X"):
            print("Vitoria de X")
            break
        rodada_jogador("O")
        print_mapa()
        if vitoria("O"):
            print("Vitoria de O")
            break
        elif empate(mapa):
            print(empate)
            break
