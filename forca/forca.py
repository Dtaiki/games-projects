import os
import random

chutes = []
chutesCertos = []
forca = [
    """
 
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
 
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]


def palavras():
    dir = os.getcwd()
    arquivo = os.path.join(dir, "palavras.txt")
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arquivo:
            palavras = [linha.strip() for linha in arquivo]
            palavra = random.choice(palavras).upper()
            print(palavra)
            return palavra
    else:
        print(f"O arquivo {arquivo} não foi encontrado.")


def tabela_print():
    print(forca[cont], end="")
    print(f"letras erradas: {chutes}")
    for letra in palavraSecreta:
        if letra in chutesCertos:
            print(letra, end="")
        else:
            print("_", end="")
    print()


def tentativa():
    chute = input("Digite uma palavra: ").upper()
    chute = chute[0]
    if chute in chutes:
        print(f'A letra "{chute}" ja foi utilizada')
        return tentativa()
    elif chute in palavraSecreta:
        chutesCertos.append(chute)
        return 0
    else:
        chutes.append(chute)
        return 1


def correcao():
    for letra in palavraSecreta:
        if letra not in chutesCertos:
            return False
    print(f"Voce venceu, a palavra era {palavraSecreta}")
    return True


if __name__ == "__main__":
    palavraSecreta = palavras()
    print("Jogo da Forca".center(50))
    cont = 0
    while True:
        tabela_print()
        if cont == 6:
            print(f"Voce perdeu, a palavra era {palavraSecreta}")
            break
        cont += tentativa()
        if correcao():
            break
    print("FIM")
