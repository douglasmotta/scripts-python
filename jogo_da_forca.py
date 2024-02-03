import random

def pegar_palavra_secreta():
    with open("palavras.txt", "r", encoding="utf-8") as arquivo:
        palavras_potencial = [linha.strip() for linha in arquivo]

    palavra_secreta = random.choice(palavras_potencial)

    return palavra_secreta

def pegar_palpite():
    palpite = input("Digite uma letra: ")

    return palpite

def avaliar_palpite(palavra_secreta, letras_acertadas, palpite):
    if palpite in palavra_secreta:
        for indice, letra in enumerate(palavra_secreta):
            if letra == palpite:
                letras_acertadas[indice] = palpite

    else:
        print("errou")

def jogar():
    print("======= Jogo da Forca =======")

    ## definir uma palavra secreta
    palavra_secreta = pegar_palavra_secreta()
    letras_acertadas = ["_" for _ in palavra_secreta]

    ## definir uma quantidade máxima de tentativas
    tentativa_max = 7
    tentativas_usadas = 0
    venceu = False

    # ======= loop =======
    while tentativas_usadas < tentativa_max:
        print(f"TENTATIVAS RESTANTES : {tentativa_max - tentativas_usadas}")
        # verificar se o usuário deve sair do loop
        tentativas_usadas += 1

        print(" ".join(letras_acertadas))

        # pegar um palpite do usuário
        palpite = pegar_palpite()

        # avaliar o palpite do usuário
        avaliar_palpite(palavra_secreta, letras_acertadas, palpite)

        # avaliar se o usuário já acertou a palavra
        if "_" not in letras_acertadas:
            venceu = True
            print(" ".join(letras_acertadas))
            break
    # ======= loop =======
        
    # avaliar se o usuário ganhou ou não o jogo
        if venceu:
            print("Parabéns, você venceu!")
        else:
            print(f"Que pena, você perdeu. A palavra era -> {palavra_secreta}")


if __name__ == "__main__":
    jogar()
