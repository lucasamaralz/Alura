import random
print('====================================')
print(' Jogo da Advinhação Alura com Laços ')
print('====================================')
print('Dica?: Fica entre 0 á 100\n')

class Jogada():
    def Jogo():
        numero_sorteado = random.randrange(1,100)
        rodadas = 1

        for tentativas in range (1, 6):
            print(f'Tentativa Número {rodadas} de 5')
            chute = int(input('Digite o Numero:'))

            if (chute < 1 or chute > 100):
                print('\n\n\n\nValor Inválido!\n')
                continue

            elif (rodadas == 10):
                exit('Suas tentativas acabaram, Fim de Jogo!')

            elif (chute==numero_sorteado):
                print('Você acertou! Parabéns')
                break

            elif (chute<numero_sorteado):
                print('Você errou! Seu chute foi menor!\n')

            elif (chute>numero_sorteado):
                print('Você errou! Seu chute foi maior!\n')

            rodadas = rodadas + 1

        print('\nAcabou as Tentativas!')

Jogada.Jogo()



