from random import randint


def print_jogo(jogo):
    for i in range(len(jogo)):
        print(jogo[i])


def fim_jogo(jogo):
    print_jogo(jogo=jogo)
    print("fim jogo")
    exit()


def decidindo_print(x, jogo):
    if x is False:
        fim_jogo(jogo)
    else:
        print_jogo(jogo)


def chute_usuario(jogo, b_ou_x):
    while True:
        linha = int(input("Digite a linha: ")) - 1
        coluna = int(input("Digite a coluna: ")) - 1

        if jogo[linha][coluna] == 'x' or jogo[linha][coluna] == 'o':
            print("Você é burro?")
        else:
            jogo[linha][coluna] = b_ou_x
            break


def chute_robo(jogo):
    i = 0
    while True:
        linha_sorteada = randint(0, 2)
        coluna_sorteada = randint(0, 2)

        if jogo[linha_sorteada][coluna_sorteada] == 'x' or jogo[linha_sorteada][coluna_sorteada] == 'o':
            i += 1
        else:
            jogo[linha_sorteada][coluna_sorteada] = 'o'
            break

        if i >= 9:
            break


def verificar_jogo(jogo):
    x = True

    for i in range(3):
        if jogo[i][0] == "x" and jogo[i][1] == "x" and jogo[i][2] == "x" or jogo[i][0] == "o" and jogo[i][1] == "o" and \
                jogo[i][2] == "o":
            x = False

        elif jogo[0][i] == "x" and jogo[1][i] == "x" and jogo[2][i] == "x" or jogo[i][0] == "o" and jogo[i][
            1] == "o" and jogo[i][2] == "o":
            x = False

    if jogo[0][0] == "x" and jogo[1][1] == "x" and jogo[2][2] == "x" or jogo[0][0] == "o" and jogo[1][1] == "o" and \
            jogo[2][2] == "o":
        x = False

    elif jogo[0][2] == "x" and jogo[1][1] == "x" and jogo[2][0] == "x" or jogo[0][2] == "o" and jogo[1][1] == "o" and \
            jogo[2][0] == "o":
        x = False

    return x


def main():
    jogo = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]
    print("O jogo começou.")
    print_jogo(jogo=jogo)

    
    print("Modo de jogo:")
    print("[1]Jogo contra robo")
    print("[2]Dois jogadores")
    choose = int(input("Digite o modo de jogo: "))
                
    if choose == 1:
        for i in range(9):
            chute_usuario(jogo=jogo)

            chute_robo(jogo=jogo)

            x = verificar_jogo(jogo=jogo)

            decidindo_print(x=x, jogo=jogo)
    elif choose == 2:
        for i in range(9):
            if i % 2 == 0:
                print("Jogador 1: ")
                chute_usuario(jogo=jogo, b_ou_x='x')
                x = verificar_jogo(jogo=jogo)
                decidindo_print(x=x, jogo=jogo)
                
            elif i % 2 == 1:
                print("Jogador 2: ")
                chute_usuario(jogo=jogo, b_ou_x='o')
                x = verificar_jogo(jogo=jogo)
                decidindo_print(x=x, jogo=jogo)
            

if __name__ == "__main__":
    main()
