import datetime
from random import randint
from paho.mqtt import client as mqtt_client


class Mqtt:
    def __init__(self):
        self.broker = 'broker.emqx.io'
        self.port = 1883
        self.topic = "python/mqtt"
        self.client_id = f'python-mqtt-{randint(0, 1000)}'

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                pass
            else:
                pass

        client = mqtt_client.Client(self.client_id)

        client.on_connect = on_connect
        client.connect(self.broker, self.port)
        return client

    def publish(self, client, escolha):
        if escolha == 1:
            msg_count = input("Digite seu nome: ")
        elif escolha == 2:
            msg_count = input("Digite a posição: ")
        while True:
            result = client.publish(self.topic, msg_count)
            status = result[0]
            if status == 0:
                x = 0
                return x, msg_count
            else:
                print(f"Failed to send message to topic {self.topic}")

    def subscribe_nomes(self, client: mqtt_client, lista_nomes):
        def on_message(client, userdata, msg):
            lista_nomes.append(msg.payload.decode())
            client.disconnect()

        client.subscribe(self.topic)
        client.on_message = on_message

    def subscribe_posicao(self, client: mqtt_client, lista_posicao):
        def on_message(client, userdata, msg):
            lista_posicao.append(int(msg.payload.decode()))
            print(lista_posicao)
            client.disconnect()

        client.subscribe(self.topic)
        client.on_message = on_message

    def recebe_nomes(self, lista_nomes, teste):
        self.subscribe_nomes(teste, lista_nomes=lista_nomes)
        teste.loop_forever()

    def recebe_posicao(self, teste, lista_posicao):
        self.subscribe_posicao(teste, lista_posicao=lista_posicao)
        teste.loop_forever()

    def manda_nomes(self, lista_nomes, teste, escolha):
        teste.loop_start()
        x, nome = self.publish(teste, escolha=escolha)
        if x == 0:
            teste.loop_stop()
        lista_nomes.append(nome)

    def manda_posicao(self, lista_posicao, teste, escolha):
        teste.loop_start()
        x, nome = self.publish(teste, escolha=escolha)
        if x == 0:
            teste.loop_stop()
        lista_posicao.append(int(nome))



