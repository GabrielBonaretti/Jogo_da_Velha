from random import randint


class Jogo():
    def __init__(self, tabuleiro='', x = True, jogador_1 = 'x', jogador_2 = 'o', escolha_jogador=0):               
        tabuleiro = [['-', '-', '-'],
                     ['-', '-', '-'],
                     ['-', '-', '-']]     
        
        self.__tabuleiro = tabuleiro
        self.__x = x
        self.__jogador_1 = jogador_1
        self.__jogador_2 = jogador_2
        self.__escolha_jogador = escolha_jogador
    
    
    def iniciar_jogo(self):
        while True:
            print("Modo de jogo:")
            print("[1]Jogo contra robo")
            print("[2]Dois jogadores")
            print("[3]Sair")
            choose = int(input("Digite o modo de jogo: "))
                        
            if choose == 1:
                self.__jogo_contra_robo()
                    
            elif choose == 2:
                self.__jogo_contra_usuarios()
                
            elif choose == 3:
                break
        
        
    def __jogo_contra_robo(self):
        self.__escolha_xoub()
        self.__print_jogo()
        
        for i in range(9):
            self.__chute_robo()
            self.__verificar_jogo()
            self.__decidindo_print()
        
            
    def __jogo_contra_usuarios(self):
        self.__escolha_xoub()
        self.__print_jogo()
        
        for i in range(9):
            self.__chute_usuario()
            self.__verificar_jogo()
            self.__decidindo_print()
                   
        
    def __escolha_xoub(self):
        while True:
            self.__jogador_1 = input("Digite qual simbolo voce deseja para o jogador 1 [x/o]: " ) 
            
            if self.__jogador_1 == 'x':
                self.__jogador_2 = 'o'
                break
            
            elif self.__jogador_1 == 'o':
                self.__jogador_2 = 'x'
                break
            
            else:
                continue
   
                
    def __print_jogo(self):
        for i in range(3):
            print(self.__tabuleiro[i])
       
            
    def __fim_jogo(self):
        self.__print_jogo()
        print("fim jogo")
        exit()
    
    
    def __decidindo_print(self):
        if self.__x is False:
            self.__fim_jogo()
        else:
            self.__print_jogo()
       
            
    def __chute_usuario(self):
        while True:
            if self.__escolha_jogador % 2 == 0:
                print("Jogador 1: ")
            elif self.__escolha_jogador % 2 == 1:
                print("Jogador 2: ")  
            
            linha = int(input("Digite a linha: ")) - 1
            coluna = int(input("Digite a coluna: ")) - 1

            if self.__tabuleiro[linha][coluna] == 'x' or self.__tabuleiro[linha][coluna] == 'o':
                print("Você é burro?")
                
            elif self.__escolha_jogador % 2 == 0:
                self.__tabuleiro[linha][coluna] = self.__jogador_1
                break
            
            elif self.__escolha_jogador % 2 == 1:
                self.__tabuleiro[linha][coluna] = self.__jogador_2
                break
    
    
    def __chute_robo(self):
        i = 0
        while True:
            linha = int(input("Digite a linha: ")) - 1
            coluna = int(input("Digite a coluna: ")) - 1

            if self.__tabuleiro[linha][coluna] == 'x' or self.__tabuleiro[linha][coluna] == 'o':
                print("Você é burro?")
                
            else:
                self.__tabuleiro[linha][coluna] = self.__jogador_1
            
            linha_sorteada = randint(0, 2)
            coluna_sorteada = randint(0, 2)

            if self.__tabuleiro[linha_sorteada][coluna_sorteada] == 'x' or self.__tabuleiro[linha_sorteada][coluna_sorteada] == 'o':
                i += 1
            else:
                self.__tabuleiro[linha_sorteada][coluna_sorteada] = self.__jogador_2
                break

            if i >= 9:
                break

    
    def __verificar_jogo(self):
        for i in range(3):
            if self.__tabuleiro[i][0] == "x" and self.__tabuleiro[i][1] == "x" and self.__tabuleiro[i][2] == "x" or self.__tabuleiro[i][0] == "o" and self.__tabuleiro[i][1] == "o" and \
                    self.__tabuleiro[i][2] == "o":
                self.__x = False

            elif self.__tabuleiro[0][i] == "x" and self.__tabuleiro[1][i] == "x" and self.__tabuleiro[2][i] == "x" or self.__tabuleiro[i][0] == "o" and self.__tabuleiro[i][
                1] == "o" and self.__tabuleiro[i][2] == "o":
                self.__x = False

        if self.__tabuleiro[0][0] == "x" and self.__tabuleiro[1][1] == "x" and self.__tabuleiro[2][2] == "x" or self.__tabuleiro[0][0] == "o" and self.__tabuleiro[1][1] == "o" and \
                self.__tabuleiro[2][2] == "o":
            self.__x = False

        elif self.__tabuleiro[0][2] == "x" and self.__tabuleiro[1][1] == "x" and self.__tabuleiro[2][0] == "x" or self.__tabuleiro[0][2] == "o" and self.__tabuleiro[1][1] == "o" and \
                self.__tabuleiro[2][0] == "o":
            self.__x = False
            
        self.__escolha_jogador += 1


