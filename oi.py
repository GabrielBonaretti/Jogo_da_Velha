class Cliente:
    def __init__(self, posicao = 'x'):
        """
        Instancia um objeto do tipo Cliente
        :param nome: str
        """
        self.__posicao = posicao

    @property
    def posicao(self):
        return self.__posicao.upper()

    @posicao.setter
    def posicao(self, chute):    
        if self.__posicao != '':
            print("nao")
        else:
            self.__posicao = chute


if __name__ == "__main__":
    j = Cliente(posicao='')
    j.posicao = 'o'        
    print(j.posicao)
        