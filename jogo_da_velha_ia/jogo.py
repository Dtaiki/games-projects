from collections import Counter


casa_vazia = 0
jogadorX = 1
jogadorO = -1


def jogador(mapa):
    count = Counter(mapa)
    jogadasX = count[1]
    jogadasO = count[-1]

    if jogadasX + jogadasO == 9:
        return None
    elif jogadasX > jogadasO:
        return jogadorO
    else:
        return jogadorX


def resultado(s):
    for casa in range(3):
        if s[3 * casa] == s[3 * casa + 1] == s[3 * casa + 2] != casa_vazia:
            return s[3 * casa]
        if s[casa] == s[casa + 3] == s[casa + 6] != casa_vazia:
            return s[casa]

    if s[0] == s[4] == s[8] != casa_vazia:
        return s[0]
    if s[2] == s[4] == s[6] != casa_vazia:
        return s[2]

    if jogador(s) is None:
        return 0

    return None


def novo_mapa(mapa, jogada):
    (jogador, lugar) = jogada
    mapa_copia = mapa.copy()
    mapa_copia[lugar] = jogador
    return mapa_copia


def print_mapa(mapa):
    nmapa = ["X" if x == 1 else "O" if x == -1 else " " for x in mapa]
    linha1 = "| {} | {} | {} |".format(nmapa[0], nmapa[1], nmapa[2])
    linha2 = "| {} | {} | {} |".format(nmapa[3], nmapa[4], nmapa[5])
    linha3 = "| {} | {} | {} |".format(nmapa[6], nmapa[7], nmapa[8])
    print(f"\n{linha1}\n{linha2}\n{linha3}")


def minimax(mapa):
    acoes = acao_mapa(mapa)
    uteis = []
    for acao in acoes:
        copia_mapa = novo_mapa(mapa, acao)
        uteis.append((acao, util(copia_mapa, 1)))
    if len(uteis) == 0:
        return ((0, 0), (0, 0))
    lista = sorted(uteis, key=lambda l: l[0][1])
    acao = min(lista, key=lambda l: l[1])
    return acao


def acao_mapa(mapa):
    jogada = jogador(mapa)
    lista_acoes = [(jogada, i) for i in range(len(mapa)) if mapa[i] == casa_vazia]
    return lista_acoes


def util(mapa, custo):
    term = resultado(mapa)
    if term is not None:
        return (term, custo)

    action_list = acao_mapa(mapa)
    utils = []
    for action in action_list:
        new_s = novo_mapa(mapa, action)
        utils.append(util(new_s, custo + 1))

    score = utils[0][0]
    idx_cost = utils[0][1]
    play = jogador(mapa)
    if play == jogadorX:
        for i in range(len(utils)):
            if utils[i][0] > score:
                score = utils[i][0]
                idx_cost = utils[i][1]
    else:
        for i in range(len(utils)):
            if utils[i][0] < score:
                score = utils[i][0]
                idx_cost = utils[i][1]
    return (score, idx_cost)


if __name__ == "__main__":
    mapa = [casa_vazia for _ in range(9)]
    print(" |1|2|3|\n |4|5|6|\n |7|8|9|\n")
    while resultado(mapa) is None:
        jogada = jogador(mapa)
        if jogada == jogadorX:
            print("Rodada de X")
            escolha = int(input("Escolha uma casa entre 1~9: ")) - 1
            if not mapa[escolha] == casa_vazia:
                print(print("O campo ja esta sendo usado"))
                continue
            mapa = novo_mapa(mapa, (1, escolha))
            print_mapa(mapa)
        else:
            print("O computador esta fazendo sua jogada")
            action = minimax(mapa)
            mapa = novo_mapa(mapa, action[0])
            print_mapa(mapa)
    ganhador = util(mapa, 1)[0]
    if ganhador == jogadorX:
        print("Voce ganhou")
    elif ganhador == jogadorO:
        print("Voce perdeu")
    else:
        print("Foi um empate")
