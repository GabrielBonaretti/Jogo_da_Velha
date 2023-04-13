from random import randint
from paho.mqtt import client as mqtt_client


class Mqtt:
    def __init__(self):
        '''

        '''
        self.broker = '10.21.160.16'
        self.port = 1883
        self.topic = "python/mqtt"
        self.client_id = f'python-mqtt-{randint(0, 1000)}'

    def connect_mqtt(self):
        '''

        :return:
        '''
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                pass
            else:
                pass

        client = mqtt_client.Client(self.client_id)

        client.on_connect = on_connect
        client.connect(self.broker, self.port)
        return client

    def publish(self, client, escolha, msg):
        '''

        :param client:
        :param escolha:
        :return:
        '''
        if escolha == 1:
            msg_count = input("Digite seu nome: ")
        elif escolha == 2:
            msg_count = msg
        while True:
            result = client.publish(self.topic, msg_count)
            status = result[0]
            if status == 0:
                x = 0
                return x, msg_count
            else:
                print(f"Failed to send message to topic {self.topic}")

    def subscribe_nomes(self, client: mqtt_client, lista_nomes):
        '''

        :param client:
        :param lista_nomes:
        :return:
        '''
        def on_message(client, userdata, msg):
            lista_nomes.append(msg.payload.decode())
            client.disconnect()

        client.subscribe(self.topic)
        client.on_message = on_message

    def subscribe_posicao(self, client: mqtt_client, lista_posicao):
        '''

        :param client:
        :param lista_posicao:
        :return:
        '''
        def on_message(client, userdata, msg):
            lista_posicao.append(int(msg.payload.decode()))
            print(lista_posicao)
            client.disconnect()

        client.subscribe(self.topic)
        client.on_message = on_message

    def recebe_nomes(self, lista_nomes, teste):
        '''

        :param lista_nomes:
        :param teste:
        :return:
        '''
        self.subscribe_nomes(teste, lista_nomes=lista_nomes)
        teste.loop_forever()

    def recebe_posicao(self, teste, lista_posicao):
        '''

        :param teste:
        :param lista_posicao:
        :return:
        '''
        self.subscribe_posicao(teste, lista_posicao=lista_posicao)
        teste.loop_forever()

    def manda_nomes(self, lista_nomes, teste, escolha, msg=''):
        '''

        :param lista_nomes:
        :param teste:
        :param escolha:
        :return:
        '''
        teste.loop_start()
        x, nome = self.publish(teste, escolha=escolha, msg=msg)
        if x == 0:
            teste.loop_stop()
        lista_nomes.append(nome)

    def manda_posicao(self, lista_posicao, teste, escolha, msg):
        '''

        :param lista_posicao:
        :param teste:
        :param escolha:
        :return:
        '''
        teste.loop_start()
        x, nome = self.publish(teste, escolha=escolha, msg=msg)
        if x == 0:
            teste.loop_stop()
        lista_posicao.append(int(nome))
