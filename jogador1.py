import os
import time

from jogo_velha_classe import Jogo
from mqtt_classe import Mqtt


def main():
    while True:
        jogo_objeto = Jogo()
        mqtt_objeto = Mqtt()
    
        print("Modo de jogo:")
        print("[1]Jogo contra robo")
        print("[2]Dois jogadores")
        print("[3]Dois jogadores, dois pc's")
        print("[4]Sair")
        choose = int(input("Digite o modo de jogo: "))
        os.system('cls')

        if choose == 1:
            jogo_objeto.jogo_contra_robo()

        elif choose == 2:
            jogo_objeto.jogo_contra_usuarios()

        elif choose == 3:
            jogo_objeto.print_jogo()
            lista_nomes = []
            lista_posicao = []

            while len(lista_nomes) < 2:
                recebe3 = mqtt_objeto.connect_mqtt()
                mqtt_objeto.recebe_nomes(lista_nomes=lista_nomes, teste=recebe3)
                manda3 = mqtt_objeto.connect_mqtt()
                mqtt_objeto.manda_nomes(lista_nomes=lista_nomes, teste=manda3, escolha=1)

            for i in range(9):
                lista_posicao.clear()
                escolha_jogador = jogo_objeto.escolha_jogador

                if escolha_jogador % 2 == 0:
                    print("Vez do jogador {}".format(lista_nomes[escolha_jogador % 2]))
                    recebe4 = mqtt_objeto.connect_mqtt()
                    mqtt_objeto.recebe_posicao(teste=recebe4, lista_posicao=lista_posicao)

                elif escolha_jogador % 2 == 1:
                    print("Vez do jogador {}".format(lista_nomes[escolha_jogador % 2]))
                    posicao = jogo_objeto.teste_posicao
                    manda4 = mqtt_objeto.connect_mqtt()
                    mqtt_objeto.manda_posicao(lista_posicao=lista_posicao, teste=manda4, escolha=2, msg=posicao)

                posicao = lista_posicao[0]
                jogo_objeto.jogar_mqtt(posicao=posicao)
                jogo_objeto.verificar_jogo()
                jogo_objeto.decidindo_print(jogador1=lista_nomes[1], jogador2=lista_nomes[0])

            jogo_objeto.print_jogo()  
            time.sleep(2)
            os.system('cls')

        elif choose == 4:
            break


if __name__ == "__main__":
    main()
