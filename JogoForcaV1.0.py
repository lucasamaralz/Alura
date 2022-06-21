import random

def Forca():
    print('Bem-Vindo ao Jogo da Forca!')
    print('Escolha o Tema: (1) Carros (2) Comidas (3) Cores')
    escolha = input('Digite o numero: ')

    carros = ["gol", "parati", "saveiro", "fox", "astra", "omega"]
    cores = ["azul", "verde", "rosa", "vermelho", "cinza"]
    comidas = ["macarrao","bolo","pizza","chocolate","pimenta","lasanha"]

    if (escolha == "1"):
        palavra_secreta = random.choice(carros).upper()

    elif (escolha == "2"):
        palavra_secreta = random.choice(comidas).upper()

    elif (escolha == "3"):
        palavra_secreta = random.choice(cores).upper()

    else:
        print('Valor Incorreto, Tente Novamente!')

    letras_acertadas = ["_" for letra in palavra_secreta]

    print(letras_acertadas)

    inforcou = False
    acertou = False

    erros = 0

    while(not acertou and not inforcou):

        chute = input('Digite a letra: ').upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra

                index += 1
            print(letras_acertadas)

        else:
            erros += 1
            print(f'Você errou! Tentativas restantes {6 - erros}')

        inforcou = erros == 6
        acertou = not "_" in letras_acertadas

    if(acertou):
        print('Parabéns você acertou a palavra secreta!')
    else:
        print('Você Perdeu :( Tente Novamente!')


Forca()