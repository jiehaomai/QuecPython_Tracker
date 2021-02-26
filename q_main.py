# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#*******sys python文件*********
import utime
import checkNet
#*******sys python文件*********

#*******user python文件*********
from usr import q_recv_thread
from usr import q_prase_thread
from usr import q_send_thread
from usr import q_gps
from usr import q_mqtt
#*******user python文件 ********


PROJECT_NAME = "QuecPython_Tracker_Mqtt"
PROJECT_VERSION = "1.0.0"

def init():
    print("init")

    #wait network connect
    checknet = checkNet.CheckNetwork(PROJECT_NAME, PROJECT_VERSION)
    checknet.wait_network_connected()

    #init mqtt
    print("init mqtt")
    q_mqtt.mqtt.mqtt_set_recv_callback()
    q_mqtt.mqtt.connect()
    q_mqtt.mqtt.sub_topic(b"quec/868540051778302/down")


    #gps_uart init
    print("init uart")
    gps_uart = q_gps.Uart2_Class()
    gps_uart.run()

    #run thread
    print("init thread")
    q_recv_thread.recv_thread.run()
    q_prase_thread.prase_thread.run()
    q_send_thread.send_thread.run()

    print("init thread ok")


#add by mjh

init()

while 1:
    utime.sleep_ms(1)
    while 1:
        pass
    pass





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
