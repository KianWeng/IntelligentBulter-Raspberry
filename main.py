#_*_coding:utf-8_*_
__author__ = 'kian'

from threading import Thread
from mqtt import connect
from mqtt import publish
from yeelight import Yeelight

def main():
    #连接MQTT服务器
    connect("45.32.7.217", 1883)

    #探测yeelight灯
    yeelight = Yeelight()
    detection_thread = Thread(target=yeelight.bulbs_detection_loop)
    detection_thread.start()

    while True:
        str = input()
        if str:
            publish("chat", str)

    yeelight.RUNNING = False
    detection_thread.join()


if __name__ == '__main__':
    main()
