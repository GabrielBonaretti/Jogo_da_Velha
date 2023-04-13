import os
from random import randint


class Jogo:
    def __init__(self, tabuleiro='', x=True, jogador_1='x', jogador_2='o', escolha_jogador=0):
        '''
        Método construtor da classe jogo

        :param tabuleiro: tabuleiro do jogo
        :param x: variavel para decidir se apenas ira printar ou acabar  jogo
        :param jogador_1: se jogador 1 é 'x' ou 'o'
        :param jogador_2: se jogador 2 é 'x' ou 'o'
        :param escolha_jogador: contador para escolhar qual jogador jogará
        '''
        tabuleiro = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        self.__tabuleiro = tabuleiro
        self.__x = x
        self.__jogador_1 = jogador_1
        self.__jogador_2 = jogador_2
        self.__escolha_jogador = escolha_jogador

    def jogo_contra_robo(self):
        '''
        Função caso o usuário final escolha jogar contra o rôbo

        :return: jogo contra rôbo
        '''
        self.__escolha_xoub()
        self.print_jogo()

        for i in range(9):
            self.__chute_robo()
            self.verificar_jogo()
            self.decidindo_print()

        os.system('cls')

    def jogo_contra_usuarios(self):
        '''
        Função caso o usuário final escolha jogar contra outro usuário no mesmo computador

        :return: Jogo dois usuários um computador
        '''
        self.__escolha_xoub()
        self.print_jogo()

        for i in range(9):
            self.__chute_usuario()
            self.verificar_jogo()
            self.decidindo_print()

    @property
    def jogador_1(self):
        '''
        Método get da atributo jogador_1

        :return: valor jogador_1
        '''
        return self.__jogador_1.lower()

    @jogador_1.setter
    def jogador_1(self, escolha):
        '''
        Método set da atributo do jogador_1

        :param escolha: escolha se o jogador um jogara com 'x' ou 'o'
        :return: se jogador 1 escolher 'x' o jogador 2 será 'o', assim vice-versa
        '''
        if escolha == 'x':
            self.__jogador_1 = escolha
            self.__jogador_2 = 'o'
        elif escolha == 'o':
            self.__jogador_1 = escolha
            self.__jogador_2 = 'x'
        else:
            print("Tente novamente")

    def __escolha_xoub(self):
        '''
        pergunta ao usuário final qual será o símbolo que ele jogará 'x' ou  'o'
        :return: o código retornará a pergunta até que o usuário escolha o símbolo 'x' ou 'o'
        '''
        while True:
            self.jogador_1 = input("Digite qual simbolo voce deseja para o jogador 1 [x/o]: ")

            if self.__jogador_1 == 'o' or self.__jogador_1 == 'x':
                break

    def print_jogo(self):
        '''
        Printa o tabuleiro na tela
        :return: Printa o tabuleiro na tela
        '''
        for i in range(9):
            if i > 0 and i % 3 == 0:
                print()
                print("----------")

            print(self.__tabuleiro[i], end=" | ")
        print()

    def fim_jogo(self, jogador1, jogador2):
        '''
        Método para a última ação do jogo, quando uma fileira ja foi completa e o resta ápenas mostrar ao usuário

        :return: printa o tabuleiro juntamente com a mensagem fim de jogo
        '''
        self.print_jogo()
        print("fim jogo")

        if self.__escolha_jogador % 2 == 0:
            print("O {} ganhou.".format(jogador2))
        elif self.__escolha_jogador % 2 == 1:
            print("O {} ganhou.".format(jogador1))

        exit()

    def decidindo_print(self, jogador1="jogador 1", jogador2='jogador 2'):
        '''
        Decide com o valor de x se ele terminará o jogo ou apenas irá printar o tabuleiro

        :return: caso x for false o código chama o método de fim de de jogo, caso não ele so printa o tabuleiro
        '''
        if self.__x is False:
            self.fim_jogo(jogador1=jogador1, jogador2=jogador2)
        else:
            self.print_jogo()

    def __chute_usuario(self):
        '''
        Mostra que jogador deve jogar e pergunta em qual posição ele joga, além de se é possível jogar nessa
        posição, so saindo do método quando o jogador escrever uma posição válida.

        :return: método para o jogo de usuário contra usuário no mesmo computador, no qual pergunta a posição e tambem
                 verifica se é possível jogal lá
        '''
        while True:
            if self.__escolha_jogador % 2 == 0:
                print("Jogador 1: ")
            elif self.__escolha_jogador % 2 == 1:
                print("Jogador 2: ")

            posicao = int(input("Digite a posicao: "))

            if self.__tabuleiro[posicao] == 'x' or self.__tabuleiro[posicao] == 'o':
                print("Ja tem ai usuário final")
                
            elif self.__escolha_jogador % 2 == 0:
                self.__tabuleiro[posicao] = self.__jogador_1
                break

            elif self.__escolha_jogador % 2 == 1:
                self.__tabuleiro[posicao] = self.__jogador_2
                break

    def __chute_robo(self):
        '''
        Pergunta em qual posição ele joga, além de se é possível jogar nessa posição, saindo do método quando o jogador
        escrever uma posição válida. Nesse método o chute do rôbo é feito de maneira aleatória e verificada se possível
        a jogada do mesmo, caso não seja ele sorteia outro número

        :return: Método para o jogo de usuário contra rôbo no mesmo computador, no qual pergunta a posição e tambem
                 verifica se é possível jogal lá
        '''

        while True:
            posicao = int(input("Digite a posicao: "))

            if self.__tabuleiro[posicao] == 'x' or self.__tabuleiro[posicao] == 'o':
                print("Ja tem ai usuário final")

            else:
                self.__tabuleiro[posicao] = self.__jogador_1
                break

        i = 0
        while i < 9:
            posicao_sorteada = randint(0, 8)

            if self.__tabuleiro[posicao_sorteada] == 'x' or self.__tabuleiro[posicao_sorteada] == 'o':
                i += 1
            else:
                self.__tabuleiro[posicao_sorteada] = self.__jogador_2
                break

    def verificar_jogo(self):
        '''
        Esse método teste todas as possibilidades de termino do jogo da velha e adiciona um no contador em cada jogada.
        :return: Retor falso na variável x caso algum
        '''
        if self.__tabuleiro[0] == "x" and self.__tabuleiro[1] == "x" and self.__tabuleiro[2] == "x" or \
                self.__tabuleiro[0] == "o" and self.__tabuleiro[1] == "o" and self.__tabuleiro[2] == "o":
            self.__x = False

        elif self.__tabuleiro[3] == "x" and self.__tabuleiro[4] == "x" and self.__tabuleiro[5] == "x" or \
                self.__tabuleiro[3] == "o" and self.__tabuleiro[4] == "o" and self.__tabuleiro[5] == "o":
            self.__x = False

        elif self.__tabuleiro[6] == "x" and self.__tabuleiro[7] == "x" and self.__tabuleiro[8] == "x" or \
                self.__tabuleiro[6] == "o" and self.__tabuleiro[7] == "o" and self.__tabuleiro[8] == "o":
            self.__x = False

        elif self.__tabuleiro[0] == "x" and self.__tabuleiro[3] == "x" and self.__tabuleiro[6] == "x" or \
                self.__tabuleiro[0] == "o" and self.__tabuleiro[3] == "o" and self.__tabuleiro[6] == "o":
            self.__x = False

        elif self.__tabuleiro[1] == "x" and self.__tabuleiro[4] == "x" and self.__tabuleiro[7] == "x" or \
                self.__tabuleiro[1] == "o" and self.__tabuleiro[4] == "o" and self.__tabuleiro[7] == "o":
            self.__x = False

        elif self.__tabuleiro[2] == "x" and self.__tabuleiro[5] == "x" and self.__tabuleiro[8] == "x" or \
                self.__tabuleiro[2] == "o" and self.__tabuleiro[5] == "o" and self.__tabuleiro[8] == "o":
            self.__x = False

        elif self.__tabuleiro[6] == "x" and self.__tabuleiro[4] == "x" and self.__tabuleiro[2] == "x" or \
                self.__tabuleiro[6] == "o" and self.__tabuleiro[4] == "o" and self.__tabuleiro[2] == "o":
            self.__x = False

        elif self.__tabuleiro[0] == "x" and self.__tabuleiro[4] == "x" and self.__tabuleiro[8] == "x" or \
                self.__tabuleiro[0] == "o" and self.__tabuleiro[4] == "o" and self.__tabuleiro[8] == "o":
            self.__x = False

        self.__escolha_jogador += 1
        os.system('cls')

    @property
    def escolha_jogador(self):
        '''
        Método get da atributo escolha_jogador
        :return: Valor escolha_jogador
        '''
        return self.__escolha_jogador

    def jogar_mqtt(self, posicao):
        '''
        Pega a posição que recebeu do mqtt e testa se é possivel fazer a jogada.
        :param posicao: posição da jogada que é recebida pelo mqtt
        :return: o simbolo do jogador 1 ou jogador 2 (selecao feita a partir da escolha do jogador) na posição recebida
        '''
        while True:
            if self.__tabuleiro[posicao] == 'x' or self.__tabuleiro[posicao] == 'o':
                    print("Você é burro?")

            elif self.__escolha_jogador % 2 == 0:
                self.__tabuleiro[posicao] = self.__jogador_1
                break

            elif self.__escolha_jogador % 2 == 1:
                self.__tabuleiro[posicao] = self.__jogador_2
                break
    
    @property
    def teste_posicao(self):
        while True:
            try:
                posicao = int(input("Digite a posicao: "))

                if self.__tabuleiro[posicao] == 'x' or self.__tabuleiro[posicao] == 'o':
                    print("Ja tem ai usuário final")
                    
                elif posicao < 0 or posicao > 8:
                    print("Número fora do range")
                    
                else:
                    return posicao
                    break
                
            except:
                print("Só número")
