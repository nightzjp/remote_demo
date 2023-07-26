# -*- coding: utf-8 -*-

"""
@author: Mr_zhang
@software: PyCharm
@file: publish.py
@time: 2022/5/7 21:30
"""
import base64
import json
import time

from paho.mqtt import client as mqtt_client


class Publish:
    """消息发布者"""

    def __init__(self, client_id, host, port, keepalive=60):
        self.client_id = client_id
        self.client = None
        self.host = host
        self.port = port
        self.keepalive = keepalive
        self.username = "admin"
        self.password = "public"

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        """当代理响应连接请求时调用"""
        print("on_connect: ", client, rc)

    @staticmethod
    def on_disconnect(client, userdata, rc):
        """当与代理断开连接时调用"""
        print("on_disconnect: ", client, rc)

    @staticmethod
    def on_message(client, userdata, message):
        """当收到关于客户订阅的主题的消息时调用"""
        print("on_message: ", client, message)
        _message = json.loads(message.payload.decode())
        print(_message)
        client.disconnect()

    @staticmethod
    def on_publish(client, userdata, mid):
        """当使用使用publish()发送的消息已经传输到代理时被调用"""
        print("on_publish: ", client, userdata, mid)

    @staticmethod
    def on_subscribe(client, userdata, mid, granted_qos):
        """当代理响应订阅请求时被调用"""
        print("on_subscribe: ", client)

    @staticmethod
    def on_unsubscribe(client, userdata, mid):
        """当代理响应取消订阅请求时调用"""
        print("on_unsubscribe: ", client)

    def connect_mqtt(self):
        """连接mqtt服务器"""
        client = mqtt_client.Client(
            self.client_id, clean_session=True, protocol=mqtt_client.MQTTv311, transport="tcp"
        )
        client.username_pw_set(self.username, self.password)
        client.on_connect = self.on_connect
        client.on_disconnect = self.on_disconnect
        client.on_message = self.on_message
        client.on_publish = self.on_publish
        client.on_subscribe = self.on_subscribe
        client.on_unsubscribe = self.on_unsubscribe
        if not client.is_connected():
            client.connect(host=self.host, port=self.port, keepalive=self.keepalive)
        self.client = client

    @staticmethod
    def publish(client, topic, message):
        """发布消息"""
        result = client.publish(topic, payload=json.dumps(message), qos=0)
        status = result[0]
        if status == 0:
            print(f"send {message} to {topic}\n")
        else:
            client.loop_stop()
            print(f"failed to send message to {topic}")

    def send(self, topic, message, callback=False):
        """
        主程序运行
        :param topic: 订阅主题
        :param message: 消息
        :param callback: 是否需要返回值，默认需要
        :return:
        """
        self.publish(client=self.client, topic=topic, message=message)
        if callback:
            self.client.subscribe(self.client_id)
            self.client.loop_forever()
        else:
            self.client.loop_start()


_client_id = "mqtt-tcp-pub-{id}".format(id=time.time() * 100000)
pub = Publish(client_id=_client_id, host="192.168.2.202", port=1883, keepalive=60)
pub.connect_mqtt()

with open("cat.jpg", "rb") as f:
    image = base64.b64encode(f.read()).decode()

gps_topic = "$share/abc/$backendCsia/A0001/coordinate"
illegal_topic = "$share/abc/$backendCsia/A0001/vehicleRecord"

gps_payload = {
        "deviceNumber": "A0001",
        "messageCreateTime": int(time.time() * 1000),
        "data": {
            "longitude": "123.1",
            "latitude": "23.1",
            "speed": 23.1,
            "gpsTime": int(time.time() * 1000)
        }
    }

illegal_payload = {
        "deviceNumber": "A0001",
        "messageCreateTime": int(time.time() * 1000),
        "data": {
            "plate": "川A123456",
            "plateColor": "蓝色",
            "vehicleType": "小型车",
            "plateImage": image,
            "vehicleImage": image,
            "panoramaImage": image,
            "collectTime": int(time.time() * 1000)
        }
    }

# GPS消息测试
pub.send(topic=gps_topic, message=gps_payload)

# 违章数据测试
pub.send(topic=illegal_topic, message=illegal_payload)
