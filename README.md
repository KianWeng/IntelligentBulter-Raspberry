# IntelligentBulter-Raspberry
这是运行在Raspberry Pi上的智能管家服务，通过获取移动端(app)发出的mqtt消息
来控制家庭的智能设备。

MQTT协议定义了两个个主题：
	/dev2app/${device_id}：设备推送消息到移动端
	/app2dev/${device_id}: 接收移动端发送的消息
移动端可以通过扫描设备的二维码获取到设备的device_id

推送的消息采用json，不同的设备有不同的json格式：
1.yeelight灯的格式参照如下：
{
    "type":light,
    "id":1,
    "method":set_power,
    "params":["on","smooth",500]
}
