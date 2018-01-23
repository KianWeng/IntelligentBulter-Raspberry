#_*_coding:utf-8_*_
__author__ = 'kian'
from mqtt import connect
from mqtt import publish

def main():
    connect("45.32.7.217", 1883)
    while True:
        str = input()
        if str:
            publish("chat", str)

if __name__ == '__main__':
    main()
