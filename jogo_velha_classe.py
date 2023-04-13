import os
from random import randint


class Jogo:
    def __init__(self, tabuleiro='', x=True, jogador_1='x', jogador_2='o', escolha_jogador=0):
        tabuleiro = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        self.__tabuleiro = tabuleiro
        self.__x = x
        self.__jogador_1 = jogador_1
        self.__jogador_2 = jogador_2
        self.__escolha_jogador = escolha_jogador

    def jogo_contra_robo(self):
        self.__escolha_xoub()
        self.print_jogo()

        for i in range(9):
            self.__chute_robo()
            self.verificar_jogo()
            self.decidindo_print()

        os.system('cls')

    def jogo_contra_usuarios(self):
        self.__escolha_xoub()
        self.print_jogo()

        for i in range(9):
            self.__chute_usuario()
            self.verificar_jogo()
            self.decidindo_print()

    @property
    def jogador_1(self):
        return self.__jogador_1.lower()

    @jogador_1.setter
    def jogador_1(self, escolha):
        if escolha == 'x':
            self.__jogador_1 = escolha
            self.__jogador_2 = 'o'
        elif escolha == 'o':
            self.__jogador_1 = escolha
            self.__jogador_2 = 'x'
        else:
            print("Tente novamente")

    def __escolha_xoub(self):
        while True:
            self.jogador_1 = input("Digite qual simbolo voce deseja para o jogador 1 [x/o]: ")

            if self.__jogador_1 == 'o' or self.__jogador_1 == 'x':
                break

    def print_jogo(self):
        for i in range(9):
            if i > 0 and i % 3 == 0:
                print()
                print("----------")

            print(self.__tabuleiro[i], end=" | ")
        print()

    def __fim_jogo(self):
        self.print_jogo()
        print("fim jogo")
        exit()

    def decidindo_print(self):
        if self.__x is False:
            self.__fim_jogo()
        else:
            self.print_jogo()

    def __chute_usuario(self):
        while True:
            if self.__escolha_jogador % 2 == 0:
                print("Jogador 1: ")
            elif self.__escolha_jogador % 2 == 1:
                print("Jogador 2: ")

            posicao = int(input("Digite a posicao: "))

            if self.__tabuleiro[posicao] == 'x' or self.__tabuleiro[posicao] == 'o':
                print("Você é burro?")

            elif self.__escolha_jogador % 2 == 0:
                self.__tabuleiro[posicao] = self.__jogador_1
                break

            elif self.__escolha_jogador % 2 == 1:
                self.__tabuleiro[posicao] = self.__jogador_2
                break

    def __chute_robo(self):
        i = 0
        while True:
            posicao = int(input("Digite a posicao: "))

            if self.__tabuleiro[posicao] == 'x' or self.__tabuleiro[posicao] == 'o':
                print("Você é burro?")

            else:
                self.__tabuleiro[posicao] = self.__jogador_1
                break

        while i < 9:
            posicao_sorteada = randint(0, 8)

            if self.__tabuleiro[posicao_sorteada] == 'x' or self.__tabuleiro[posicao_sorteada] == 'o':
                i += 1
            else:
                self.__tabuleiro[posicao_sorteada] = self.__jogador_2
                break

    def verificar_jogo(self):
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
        return self.__escolha_jogador

    def jogar_mqtt(self, posicao):
        while True:
            if self.__tabuleiro[posicao] == 'x' or self.__tabuleiro[posicao] == 'o':
                    print("Você é burro?")

            elif self.__escolha_jogador % 2 == 0:
                self.__tabuleiro[posicao] = self.__jogador_1
                break

            elif self.__escolha_jogador % 2 == 1:
                self.__tabuleiro[posicao] = self.__jogador_2
                break