# _*_coding:utf-8_*_
__author__ = 'kian'

import paho.mqtt.client as mqtt

mqtt_client = mqtt.Client() 

#连接成功回调函数
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("chat")
    
#断开连接回调函数
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")
    else:
        print("Disconnect mqtt server success.")

#消息接收回调函数
def on_message(client, userdata, msg):
    print("Topic:" + msg.topic+" message:" + str(msg.payload))

#消息推送回调函数
def on_publish(client, userdata, mid):
    print("Publish message susscess.")

#连接mqtt服务器
def connect(hostname, port):
    mqtt_client.on_connect = on_connect
    mqtt_client.on_disconnect = on_disconnect
    mqtt_client.on_message = on_message
    mqtt_client.on_publish = on_publish
    mqtt_client.username_pw_set("admin", "passwd")

    mqtt_client.connect(hostname, port, 60)
    mqtt_client.loop_forever()

#断开mqtt服务器
def disconnect():
    mqtt_client.disconnect()

#推送消息接口
def publish(topic, msg):
    mqtt_client.publish(topic, payload=msg, qos=0, retain=False)


