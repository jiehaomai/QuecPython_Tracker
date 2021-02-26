
#定义设备与云平台通信接口
#
#通信格式 Jason
'''
{
“type”: 1,
"gps": lat,lon
}
'''

class MSG_TYPE:
    GET_GPS_MSG = 1
    GET_CELL_MSG = 2
    GET_WIFI_MSG = 3


class msg_queue_class():
    '队列类'

    def __init__(self):
        # print("初始化消息队列类")
        self.list_id = []

    def pack_msg_struct(self):
        pass

    def put_queue(self,msg):
        #print("入队")
        self.list_id.append(msg)
    def get_queue(self):
        #print("获取队列")
        msg_buff = self.list_id.pop(0)
        return msg_buff



recv_msg_queue = msg_queue_class()
pack_msg_queue = msg_queue_class()
