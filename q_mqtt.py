'''
@Author: Baron
@Date: 2020-04-24
@LastEditTime: 2020-04-24 17:06:08
@Description: example for module umqtt
@FilePath: example_mqtt_file.py
'''
#*******sys python文件*********
from umqtt import MQTTClient
import utime
import log
import checkNet
#*******sys python文件*********

#*******user python文件*********
from usr import q_recv_thread
#*******user python文件*********


'''
下面两个全局变量是必须有的，用户可以根据自己的实际项目修改下面两个全局变量的值，
在执行用户代码前，会先打印这两个变量的值。
'''

# 设置日志输出级别
log.basicConfig(level=log.INFO)
mqtt_log = log.getLogger("MQTT")

class Mqtt_Class():

    def __init__(self):
        # 创建一个mqtt实例
        self.client_id = "868540051778302"
        self.downtopic = "quec/868540051778302/down"
        self.uptopic = "quec/868540051778302/up"
        self.mqttserver = "southbound.quectel.com"
        self.mqttport = 1883
        self.uername = "868540051778302"
        self.passwd = "d40332b8211097ffbb0e2645c2efec95"
        self.mqtt_client = MQTTClient(self.client_id, self.mqttserver, self.mqttport,self.uername,self.passwd)

    def mqtt_recv_callback(self,topic, msg):
        print("Subscribe Recv: Topic={},Msg={}".format(topic.decode(), msg.decode()))
        q_recv_thread.recv_thread.recv_callback(topic, msg.decode())

    def mqtt_set_recv_callback(self):
        # 设置消息回调
        self.mqtt_client.set_callback(self.mqtt_recv_callback)

    def connect(self):
        #建立连接
        self.mqtt_client.connect()

    def sub_topic(self, topic):
        # 订阅主题
        self.mqtt_client.subscribe(topic)

    def put_msg(self, msg, qos=0):
        # 发布消息
        self.mqtt_client.publish(self.uptopic, msg, qos)

    def wait_msg(self):
        self.mqtt_client.wait_msg()

    def disconnect(self):
        # 关闭连接
        self.mqtt_client.disconnect()



mqtt = Mqtt_Class()