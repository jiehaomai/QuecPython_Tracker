from usr import q_msg_queue
import utime
import _thread
import ujson

class prase_thread_class():


    def prase_date(self,msg):
        # do something
        print("prase msg: ",msg)

        dict = ujson.loads(msg)
        msg_type = dict.get("type")
        if msg_type == q_msg_queue.MSG_TYPE.GET_GPS_MSG:
            # 拼接gps数据包
            # GpsMsgFormat = "{\"msg_type\":{type},\"gps\":{lat},{lon}}"
            GpsMsgPacket = "{\"type\":1,\"gps\":1111.1111,2222.2222}"
            q_msg_queue.pack_msg_queue.put_queue(GpsMsgPacket)
        else:
            print("type: ",msg_type)



    def prase_thread_func(self,thread_name,thread_id):
        while 1:
            utime.sleep_ms(1)
            if len(q_msg_queue.recv_msg_queue.list_id) > 0:
                msg = q_msg_queue.recv_msg_queue.get_queue()
                self.prase_date(msg)

    def run(self):
        _thread.start_new_thread(self.prase_thread_func, ("prase_thread", 2))

prase_thread = prase_thread_class()