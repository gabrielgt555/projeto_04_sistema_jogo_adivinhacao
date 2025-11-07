import random

MIN_NUMERO = 1
MAX_NUMERO = 100
MAX_TENTATIVAS = 10
PONTUACAO_BASE = 100
PERCA = 10

jogadores = {
    "gabrielgt555": {"nome": "Gabriel"},
    "dnathanael30": {"nome": "Diego"},
    "vetin": {"nome": "Enzo"},
}

def escolher_jogador():
    print("JOGADORES DISPONÍVEIS")
    for usuario, dados in jogadores.items():
        print(f"{dados['nome']} @{usuario}")
    print()

    while True:
        usuario = input("Digite o usuário para jogar: ")
        if usuario in jogadores:
            return usuario
        else:
            print("Usuário não encontrado. Tente novamente.\n")


def gerar_numero_secreto():
    return random.randint(MIN_NUMERO, MAX_NUMERO)


def calcular_pontuacao(tentativas):
    pontos = PONTUACAO_BASE - (tentativas - 1) * PERCA
    if pontos < 0:
        pontos = 0
    return pontos


def jogar_partida(usuario):
    """Executa uma partida completa para o jogador escolhido."""
    nome = jogadores[usuario]["nome"]
    numero_secreto = gerar_numero_secreto()
    tentativas = 0

    print(f"Bem-vindo, {nome} (@{usuario})!")
    print(f"Tente adivinhar o número entre {MIN_NUMERO} e {MAX_NUMERO}.")
    print("Você tem no máximo", MAX_TENTATIVAS, "tentativas.")

    while tentativas < MAX_TENTATIVAS:
        entrada = input(f"Tentativa {tentativas + 1}: ")

        chute = int(entrada)
        if chute < MIN_NUMERO or chute > MAX_NUMERO:
            print(f"Digite um número entre {MIN_NUMERO} e {MAX_NUMERO}.\n")
            continue

        tentativas += 1

        if chute == numero_secreto:
            print("\nParabéns! Você acertou o número!")
            pontos = calcular_pontuacao(tentativas)
            print(f"Você usou {tentativas} tentativa(s).")
            print(f"Sua pontuação foi: {pontos} pontos.")
            return

        elif chute < numero_secreto:
            print("O número secreto é MAIOR que isso.\n")
        else:
            print("O número secreto é MENOR que isso.\n")

    print("\n Fim de jogo! Você não acertou o número.")
    print(f"O número secreto era: {numero_secreto}.")
    print("Pontuação: 0 pontos.")


def main():
    print("JOGO DE ADIVINHAÇÃO")

    usuario = escolher_jogador()
    jogar_partida(usuario)

    print("\nObrigado por jogar! :)")


if __name__ == "__main__":
    main()
