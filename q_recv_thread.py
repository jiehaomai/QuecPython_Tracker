#*******sys python文件*********
import utime
import _thread
#*******sys python文件*********

#*******user python文件*********
from usr import q_msg_queue
from usr import q_mqtt
#*******user python文件*********


class recv_thread_class():

    def recv_callback(self,topic, msg):
        q_msg_queue.recv_msg_queue.put_queue(msg)

    def recv_thread_func(self,thread_name,thread_id):
        while True:
            utime.sleep_ms(1)
            q_mqtt.mqtt.wait_msg()  # 阻塞函数，监听消息

    def run(self):
        _thread.start_new_thread(self.recv_thread_func, ("recv_thread", 1))


recv_thread = recv_thread_class()